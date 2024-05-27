with open("history.txt", "r") as file:
    for line in file:
        print(line.strip())

def search_file(filename, word):
    with open(filename, "r") as file:
        for line in file:
            if word.lower() in line.lower():
                print(word)
    return False

filename = "history.txt"
word = "well"
search_file(filename, word)



