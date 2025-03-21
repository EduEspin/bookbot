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
