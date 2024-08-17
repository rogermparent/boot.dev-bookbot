def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    countedChars = char_count(text)
    for countedChar in countedChars:
        print(f"The '{countedChar["char"]}' character was found {countedChar["number"]} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["number"]

def char_count(text):
    dict = {}
    for rawChar in text:
        char = rawChar.lower()
        if(char in dict):
            dict[char] = dict[char]+1
        else:
            dict[char] = 1
    sortableChars = []
    for char in dict:
        sortableChars.append({"char": char, "number": dict[char]})
    sortableChars.sort(reverse=True, key=sort_on)
    return sortableChars

main()