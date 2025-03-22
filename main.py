from stats import count_words, count_character, print_report
import sys

def get_book_text(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def main():  
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>",sys.argv[0])
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>",sys.argv[0])
        sys.exit(1)

    bookpath = sys.argv[1]
    print_report(count_words(get_book_text(bookpath)), count_character(get_book_text(bookpath)),bookpath)
    
main()