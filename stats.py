def count_words(book):
    words = book.split()
    count_words = len(words)
    return count_words

def count_character(book):
    characters = list(book.lower())
    character_list = {}
    for c in characters:
        if c not in character_list:
            character_list[c] = 1
        else:
            character_list[c] += 1
    return character_list



def print_report(words,characters):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {words} total words")
    print("--------- Character Count -------")
    sorted_characters = dict(sorted(characters.items(), key=lambda x:x[1], reverse=True))
   
    for c, n  in sorted_characters.items():
        string = str(c)
        if string.isalpha():
            print(f"{c}: {n}")
    print("============= END ===============")    