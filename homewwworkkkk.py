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
        with open(filePath, "r", encoding="utf-8") as file:
            content = file.read()

        updated_content = content.replace(old_word, new_word)

        with open(filePath, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"Replaced all occurrences of '{old_word}' with '{new_word}'.")
    except FileNotFoundError:
        print("File not found.")


# Example usage
print(count("the", "ugh.txt"))
