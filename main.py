import sys

from stats import count_words, count_characters, print_characters


def get_book_text(filepath: str) -> str:
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    characters = count_characters(book_text)
    printed_characters = print_characters(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in printed_characters:
        print(f"{character['name']}: {character['count']}")


main()
