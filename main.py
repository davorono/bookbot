def main():
    book_path = "books/frankenstein.txt"
    report(book_path)


def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    lower_book = book.lower()
    char_count = {}
    for char in lower_book:
        if char.isalpha():
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        else:
            pass
    
    return char_count

def report(book_path):
    with open(book_path) as book:
        book_contents = book.read()

        print(f"--- Begin report of {book_path} ---")
        print(f"{word_count(book_contents)} words found in the document")

        letter_list = list(letter_count(book_contents).items())
        for letter in letter_list:
            print(f"The '{letter[0]}' character was found {letter[1]} times")

        print("--- End Report ---")


        


if __name__ == '__main__':
    main()
