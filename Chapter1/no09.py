# -*- coding:utf-8 -*-

import random

s = u"I couldn't believe that i could actually understand what I was reading : the phenomenal power of the human mind ."

def main():
    words = []
    for word in s.split(" "):
        if len(word) <= 4:
            words.append(word)
        else:
            random_words = list(word[1:-1])
            random.shuffle(random_words)
            words.append(word[:1] + "".join(random_words) + word[-1:])
    print s
    print " ".join(words)

if __name__ == "__main__":
    main()
