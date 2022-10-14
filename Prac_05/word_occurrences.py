"""
Word Occurrences
Estimate: 30 minutes
Actual:   25 minutes 42 seconds
"""


def main():
    string = input("String input: ")
    word_to_count = covert_string_to_dictionary(string)
    # print(word_to_count)
    print_formatted_output(word_to_count)


def print_formatted_output(word_to_count):
    max_word_length = max(list(len(word) for word in word_to_count.keys()))
    max_count_length = max(list(len(str(count)) for count in word_to_count.values()))
    for word, count in word_to_count.items():
        print(f"{word:{max_word_length}}: {count:{max_count_length}}")


def covert_string_to_dictionary(string):
    collection_of_words = string.split(" ")
    word_to_count = {}
    for word in collection_of_words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    word_to_count = {word: word_to_count[word] for word in sorted(word_to_count)}
    return word_to_count


main()
