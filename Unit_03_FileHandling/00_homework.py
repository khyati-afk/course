def find(word, filePath):
    try:
        with open(filePath, "r", encoding="utf-8") as file:
            for line in file:
                if word in line:
                    return True
        return False
    except FileNotFoundError:
        print("File not found.")
        return False


def count(word, filePath):
    try:
        with open(filePath, "r", encoding="utf-8") as file:
            return sum(line.count(word) for line in file)
    except FileNotFoundError:
        print("File not found.")
        return 0


def find_n_replace(old_word, new_word, filePath):
    try:
        with open(filePath, "r") as infile, open("temp.txt", "w") as outfile:
            for line in infile:
                updated_line = line.replace(old_word, new_word)
                outfile.write(updated_line)
        with open("temp.txt", "r") as outfile, open(filePath, "w") as outfile:
            for line in outfile:
                outfile.write(line)
        print(f"Replaced all occurrences of '{old_word}' with '{new_word}'.")
    except FileNotFoundError:
        print("File not found.")


# usage:
print(find("the", "ugh.txt"))
print(count("the", "ugh.txt"))
print(find_n_replace("the", "that", "ugh.txt"))
