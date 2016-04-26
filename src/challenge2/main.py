#!/usr/bin/env python


def print_output_line(case, words):
    print("Case #" + str(case) + ": " + words[0][0] + " " + str(words[0][1]) + ","
          + words[1][0] + " " + str(words[1][1]) + ","
          + words[2][0] + " " + str(words[2][1]))


def get_words_from_text_file(filename):
    f = open(filename, 'r')
    return [x for y in [l.split() for l in f.readlines()] for x in y]


def get_effective_words(words, start, end):
    return words[start - 1:end]


def get_most_frequency_words(words, num_of_words):
    return sorted([(w, words.count(w)) for w in set(words)], key=lambda z: z[1], reverse=True)[:num_of_words]


def main():
    # Reading the manuscript
    words = get_words_from_text_file('corpus.txt')

    # Treating cases
    num_of_cases = int(raw_input())
    for i in range(num_of_cases):
        # Getting start and end
        edges = raw_input()
        start = int(edges.split()[0])
        end = int(edges.split()[1])

        # Retrieving most frequency words
        effective_words = get_effective_words(words, start, end)
        most_frequency = get_most_frequency_words(effective_words, 3)

        print_output_line(i+1, most_frequency)


if __name__ == '__main__':
    main()
