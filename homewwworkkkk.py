def find(word, filePath):
    try:
        with open(filePath, "r", encoding="utf-8") as file:
            content = file.read()
            return word in content
    except FileNotFoundError:
        print("File not found.")
        return False


def count(word, filePath):
    try:
        with open(filePath, "r", encoding="utf-8") as file:
            content = file.read()
            return content.count(word)
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


print(count("the", "ugh.txt"))
