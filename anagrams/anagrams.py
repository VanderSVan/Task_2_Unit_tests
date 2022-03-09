def remove_non_letters(word: str):
    if not isinstance(word, str):
        raise TypeError('word must be a string')
    list_only_letters = [symbol for symbol in word if symbol.isalpha()]
    return list_only_letters


def word_processing(word: str):
    """
    Reverse only letters in the word.
    :return: string
    """
    reversed_word_as_list = []
    list_only_letters = remove_non_letters(word)
    for symbol in word:
        if symbol.isalpha():
            reversed_word_as_list.append(list_only_letters.pop())
        else:
            reversed_word_as_list.append(symbol)
    reversed_word = ''.join(reversed_word_as_list)
    return reversed_word


def reverse_text(text: str):
    """
    Reverse letters of the words.
    All non-letter symbols stay on the same places.
    :return: string
    """
    if not isinstance(text, str):
        raise TypeError('word must be a string')
    list_words = text.split(' ')
    reversed_list = []
    for word in list_words:
        reversed_list.append(word_processing(word))
    reversed_text = ' '.join(reversed_list)
    return reversed_text


if __name__ == '__main__':
    input_text = 'a1bcd efg!h'  # write your text
    print(reverse_text(input_text))
