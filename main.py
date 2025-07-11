import sys
from stats import count_words
from stats import count_each_character
from stats import sort_character_dictionary

def get_book_text(filepath):
    result = ""
    with open(filepath) as f:
        result = f.read()
    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_location = sys.argv[1]
    
    book_text = get_book_text(book_location)
    count_of_words = count_words(book_text)
    count_of_characters = count_each_character(book_text)
    sorted_character_list = sort_character_dictionary(count_of_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")
    
    for character in sorted_character_list:
        if character["character"].isalpha():
            print(f"{character["character"]}: {character["count"]}")
    
    print("============= END ===============")


main()