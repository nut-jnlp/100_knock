#! usr/bin/env python
# _*_ cording utf-8 _*_

sentence = "I am an NLPer"

def n_gram(sentence):
    #単語bi_gram
    bi_gram = sentence.split()
    print(bi_gram)

    #文字bi_gram
    bi_gram = []
    word_list = sentence.replace(" ", "")
    bi_gram = list(word_list)
    print(bi_gram)

n_gram(sentence)
