from stats import word_count

def get_book_text(filepath):
    result = ""
    with open(filepath) as f:
        result = f.read()
    return result


def main():
    count_of_words = word_count(get_book_text("books/frankenstein.txt"))
    print(f"{count_of_words} words found in the document")


main()