from stats import count_words, count_character, print_report

def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def main():  
    #print(f"{count_words(get_book_text())} words found in the document")
    #print(count_character(get_book_text()))
    print_report(count_words(get_book_text()), count_character(get_book_text()))
    
main()