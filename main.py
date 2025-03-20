def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    count_words = len(words)
    return count_words


def main():  
    print(f"{count_words(get_book_text())} words found in the document")
main()