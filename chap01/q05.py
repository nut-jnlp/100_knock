# coding: utf-8


def sentence_to_words(sentence):
    return sentence.replace(".", "").replace(",", "").split()


def ngram(n, words):
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]


sentence = "I am an NLPer"

words = sentence_to_words(sentence)
word_bigram = ngram(2, words)
chara_bigram = ngram(2, sentence)

print("単語bi-gram: ", end="")
print(word_bigram)
print("文字bi-gram: ", end="")
print(chara_bigram)
