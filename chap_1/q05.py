#! usr/bin/env python
# _*_ cording utf-8 _*_

sentence = "I am an NLPer"

def n_gram(sentence):
    #単語bi_gram
    result = []
    word_list = sentence.split()
    for i in range(len(word_list)):
        bi_gram = (word_list[i:i+2])
        result.append(bi_gram)
    print("単語bi_gram\n{0}\n".format(result))

    #文字bi_gram
    result = []
    word_list = sentence.replace(" ", "")
    for i in range(len(word_list)):
        bi_gram = (word_list[i:i+2])
        result.append(bi_gram)
    print("文字bi_gram\n{0}".format(result))

n_gram(sentence)
