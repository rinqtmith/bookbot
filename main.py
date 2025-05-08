from stats import count_words, count_characters


def get_book_text(filepath: str) -> str:
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main() -> None:
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    characters = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(characters)


main()
