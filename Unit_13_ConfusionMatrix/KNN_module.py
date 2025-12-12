import matplotlib.pyplot as plt

class Point:
    def __init__(self, vals, label=None):
        if(vals):
            self.dims = len(vals)   # Number of dimensions
            self.vals = vals        # List of values
            self.label = label      # Label / Class / Category
        else:
            # raiseError
            pass

    def __str__(self):
        ans = "("
        for val in self.vals:
            ans += str(val) + ", "
        ans += str(self.label) + ")"
        return ans
    
    def __sub__(self, other):
        if(self.dims != other.dims):
            # raiseError
            return None
        
        sum = 0
        for i in range(self.dims):
            sum += (self.vals[i] - other.vals[i])**2
        return sum**(1/2)
    
class KNN:
    colors = ['r', 'g', 'b', 'y', 'm', 'c']
    def __init__(self, k):
        self.k = k
        self.points = []
        self.labels = []
        self.dims = None
        self.cmap = {}

    def update_points(self, points):
        if(self.dims == None):
            self.dims = points[0].dims
            
        for p in points:
            if(p.dims != self.dims):
                # raiseError
                continue
            self.points.append(p)
            if(p.label not in self.labels):
                self.labels.append(p.label)
        
        self.update_cmap()

    def update_cmap(self):
        self.cmap = {}
        for i in range(len(self.labels)):
            self.cmap[self.labels[i]] = self.colors[i]
     
    def predict(self, point, plot=False):
        if(not self.points):
            return None
        distances = []
        for p in self.points:
            label = p.label
            dist = point - p
            index = len(distances)
            distances.append((dist, label))
            while(index > 0 and distances[index-1][0] > distances[index][0]):
                temp = distances[index]
                distances[index] = distances[index-1]
                distances[index-1] = temp
                index -= 1
            if(len(distances) > self.k):
                distances.pop()
        votes = {}
        for dist, label in distances:
            if(label in votes):
                votes[label] += 1
            else:
                votes[label] = 1
        max_votes = 0
        max_label = None
        for label in votes:
            if(votes[label] > max_votes):
                max_votes = votes[label]
                max_label = label

        if (plot == True and self.dims == 2):
            plt.scatter(point.vals[0], point.vals[1], color='k', marker='x')
            labelSet = set()
            for p in self.points:
                if(p.label in labelSet):
                    plt.scatter(p.vals[0], p.vals[1], color=self.cmap[p.label])
                else:
                    plt.scatter(p.vals[0], p.vals[1], color=self.cmap[p.label], label=p.label)
                    labelSet.add(p.label)
            plt.legend()
            plt.grid(axis='both', linestyle='--')
            plt.show()
            
        return max_label