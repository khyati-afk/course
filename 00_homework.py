

def calculate_mean(*numbers):
    if not numbers:
        return None 
    return sum(numbers) / len(numbers)

print(calculate_mean(1, 2, 3, 4, 5, 6))

'*******************************************************************************'

def youngest_students(**students):
    if not students:
        return None  
    
    min_age = min(students.values())  
    youngest = [name for name, age in students.items() if age == min_age]  
    
    return youngest if len(youngest) > 1 else youngest[0] 

print(youngest_students(A=18, B=13, C=8, D=6))  

'********************************************************************************'

def calculate_percentages(total_marks, *student_marks):
    if total_marks == 0:
        return []  
    return list(map(lambda marks: (marks / total_marks) * 100, student_marks))

print(calculate_percentages(20, 16, 8, 13, 18, 17, 19, 13))  

'*********************************************************************************'

def number_series(start=1, step=1, stop=None):
    current = start - step  

    def next_number():
        nonlocal current
        current += step
        if stop != None and current > stop:
            return None
        return current

    return next_number

series1 = number_series(5,-1,1) 
print(series1())  
print(series1())  
print(series1())  
print(series1())  
print(series1())  
print(series1())  
print(series1())  


