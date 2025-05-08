def count_words(text: str) -> int:
    words = text.split()

    return len(words)


def count_characters(text: str) -> dict[str, int]:
    characters: dict[str, int] = {}

    for c in text:
        if c.lower() in characters:
            characters[c.lower()] += 1
        else:
            characters[c.lower()] = 1

    return characters
