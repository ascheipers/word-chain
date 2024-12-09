from typing import Set, List


class NoChainException(Exception):
    pass


class InvalidArgumentException(Exception):
    pass


def differs_by_one_char(s1, s2):
    if len(s1) != len(s2):
        return False

    diff_count = sum(1 for a, b in zip(s1, s2) if a != b)
    return diff_count == 1


def word_chain(start_word: str, end_word: str, dict_words: Set[str]) -> List[str]:
    if not start_word or len(start_word) == 0:
        raise InvalidArgumentException("Start word needs to be a string of length > 0.")

    if not end_word or len(end_word) == 0:
        raise InvalidArgumentException("End word needs to be a string of length > 0.")

    if len(start_word) != len(end_word):
        raise InvalidArgumentException("Start and end words must have the same length.")

    dict_words = set(item for item in dict_words if item != start_word and item != end_word)

    if not dict_words or len(dict_words) == 0:
        raise NoChainException("No chain exists.")

    if differs_by_one_char(start_word, end_word):
        return [start_word, end_word]


    for next_word in dict_words:
        if differs_by_one_char(start_word, next_word):
            try:
                chain = word_chain(next_word, end_word, set(item for item in dict_words if item != next_word))
                return [start_word] + chain
            except NoChainException:
                continue

    raise NoChainException("No chain exists.")