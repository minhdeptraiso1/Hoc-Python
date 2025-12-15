def read_file_content(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()


def count_word_frequency(text: str) -> dict[str, int]:

    text = text.lower()

    punctuation = ".,;:?!()[]"
    for char in punctuation:
        text = text.replace(char, ' ')

    words = text.split()

    frequency = {}
    for word in words:
        word = word.strip()
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


def get_top_words(frequency: dict[str, int], top_n: int = 10) -> list[tuple[str, int]]:
    words_list = list(frequency.items())

    n = len(words_list)
    for i in range(n):
        for j in range(i + 1, n):
            if words_list[i][1] < words_list[j][1]:
                words_list[i], words_list[j] = words_list[j], words_list[i]

    return words_list[:top_n]