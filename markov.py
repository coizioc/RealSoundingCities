import random

import json


class Markov():
    def __init__(self, text, state_len=2):
        self.text = text
        self.state_len = state_len
        if type(text) == dict:
            self.corpus = text
        else:
            self.corpus = self.get_corpus(text)

    def get_corpus(self, text):
        """This method converts a text into a text model."""
        corpus = {}
        for word in text.split('\n'):
            # Convert word into list of chars preceded by the start tag and
            # proceeded by the end tag.
            chars = ['START'] + [c for c in word] + ['END']
            # tup is the size self.state_len + 1. tup[:-1] will become the key
            # and tup[-1] its respective value.
            for tup in zip(*self.__get_zip(chars)):
                key = tup[:-1]
                if key not in corpus:
                    corpus[key] = []
                corpus[key] += [tup[-1]]
        return corpus

    def __get_zip(self, words):
        zip_list = []
        for i in range(0, self.state_len + 1):
            zip_list.append(words[i:])
        return zip_list

    def get_word(self):
        """This function generates a word based off of its text model."""
        word = ""
        iterations = 0
        while True:
            # Word is a list of characters beginning with the start tag. These will be joined
            # at the end.
            word = list(random.choice([key for key in self.corpus if key[0] == 'START']))

            # Until the end tag is found, find the next char from the corpus.
            while True:
                curr_char = random.choice(self.corpus[tuple(word[-self.state_len:])])
                if curr_char != 'END':
                    word += [curr_char]
                else:
                    break
            word = "".join(word[1:])
            if word not in self.text.splitlines():
                break
            iterations += 1
            if iterations == 100:
                break
        return word

    def to_json(self, fp):
        json.dump(self.corpus, fp)
