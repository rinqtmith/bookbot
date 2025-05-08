def count_words(text: str) -> int:
    words = text.split()

    return len(words)


def count_characters(text: str) -> dict[str, int]:
    characters: dict[str, int] = {}

    for c in text:
        if c.isalpha():
            if c.lower() in characters:
                characters[c.lower()] += 1
            else:
                characters[c.lower()] = 1

    return characters


def print_characters(characters: dict[str, int]) -> list[dict[str, str | int]]:
    formatted_characters: list[dict[str, str | int]] = []

    for c in characters:
        formatted_characters.append({"name": c, "count": characters[c]})

    formatted_characters.sort(reverse=True, key=lambda x: x["count"])

    return formatted_characters
