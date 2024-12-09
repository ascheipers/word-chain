import argparse
from typing import Set

from word_chain import word_chain

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Word chain.")
    parser.add_argument("search_words_file", help="The file with the start and end word")
    parser.add_argument("dict_words_file", help="The file with dictionary of available words")
    args = parser.parse_args()

    start_word, end_word = None, None
    dict_words = set()

    with open(args.search_words_file) as search_words_file:
        start_word = search_words_file.readline().strip().lower()
        end_word = search_words_file.readline().strip().lower()

    if not start_word or not end_word:
        print("No start or end word in search_words_file.")
        exit(-1)

    with open(args.dict_words_file) as dict_words_file:
        while line := dict_words_file.readline():
            dict_words.add(line.strip().lower())

    if len(dict_words) == 0:
        print("No words in dict_words_file.")
        exit(-1)

    try:
        wc = word_chain(start_word, end_word, dict_words)
        print("\n".join(wc))
    except Exception as e:
        print(e)
