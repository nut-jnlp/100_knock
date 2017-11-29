#kadai30 u'表層形    0/品詞,1/品詞細分類1,2/品詞細分類2,3/品詞細分類3,4/活用形,5/活用型,6/原形,7/読み,8/発音'
def morp_read(doc_artical):
    doc_open = open(doc_artical)
    doc_artical = [line.rstrip() for line in doc_open.readlines()]
    doc_open.close()

    sentences = []
    morphemes = []
    for line in doc_artical:
        if line in 'EOS':
            if len(morphemes) > 0:
                sentences.append(morphemes)
                morphemes=[]
        else:
            surface, elements = line.split('\t')
            elements = elements.split(',')
            morphemes.append({'surface':surface, 'base':elements[6], 'pos':elements[0], 'pos1':elements[1]})
            #print('%s   %s,%s,%s' % (surface, elements[6], elements[0], elements[1]),'\n')
    return sentences

#kadai31
def verb_extr(sentences):
    for sentence in sentences:
        for morphemes in sentence:
            if morphemes['pos']=='動詞':
                print(morphemes['surface'])

#kadai32
def verb_extr(sentences):
    for sentence in sentences:
        for morphemes in sentence:
            if morphemes['pos']=='動詞':
                print(morphemes['base'])

#kadai33
def CustomNoun_extr(sentences,noun):
    for sentence in sentences:
        for morphemes in sentence:
            if (morphemes['pos']=='名詞')and(morphemes['pos1']==noun):
                print(morphemes['surface'])

#kadai34
def CompoundNoun_extr(sentences):
    for words in sentences:
        for i in range(1, len(words)-1):
            if words[i]['surface']=='の' and words[i-1]['pos']=='名詞'and words[i+1]['pos']=='名詞':
                print('%sの%s'%(word[i-1]['surface'],word[i+1]['surface']))

#kadai35
def NounConection_extr(sentences):
    noun = []
    phrase = []
    for sentence in sentences:
        sentence.append({'pos':''})
        for word in sentence:
            if word['pos']=='名詞':
                noun.append(word['surface'])
            else:
                if len(noun) > 1:
                    phrase.append(''.join(noun))
                    print(''.join(noun))
                noun = []
    return phrase

#kadai36
def WordFrequency_extr(sentences):
    WordFreq = {}

    for sentence in sentences:
        for words in sentence:
            word = words['base']
            if word!='*'and word!='「'and word!='？'and word!='」'and word!=' 'and word!='。'and word!='、':
                if word in WordFreq.keys():
                    WordFreq[word] += 1
                else:
                    WordFreq[word] = 1

    sort_word = sorted(WordFreq.keys(), key=lambda x:WordFreq[x],reverse=True)
    for word in sort_word:
        print (word,WordFreq[word])

    return WordFreq

#kadai37
import numpy as np
import matplotlib.pyplot as plt
def TopWordFrequency(sentences):
    WordFreq = WordFrequency_extr(sentences)
    sort_word = sorted(WordFreq.keys(), key=lambda x:WordFreq[x],reverse=True)

    TopWord = sort_word[0:10]
    TopFreq = []
    for i in range(0,10,1):
        TopFreq.append(WordFreq[TopWord[i]])

    n_group = len(TopWord)

    index = np.arange(n_group)
    width = 0.5
    plt.bar(index, TopFreq, width,
            alpha=0.5,
            color='b')

    plt.xlabel('Words')
    plt.ylabel('Word frequencies')
    plt.title('Top 10 highest-frequency words')
    #plt.xticks(index + width/2, TopWord)
    plt.show()

#kadai38
import math
def histogram(sentenses):
    WordFreq = WordFrequency_extr(sentenses)
    sort_word = sorted(WordFreq.keys(), key=lambda x:WordFreq[x],reverse=True)
    TopWord = sort_word[0:len(sort_word)]
    TopFreq = []
    for i in range(0,len(sort_word)-1,1):
        TopFreq.append(WordFreq[TopWord[i]])

    log_freq = map( lambda x: math.log(x), TopFreq)


    plt.hist(list(log_freq), bins = 15, orientation='horizontal')
    plt.xlabel('Words frequency')
    plt.ylabel('Word number')
    plt.title('histogram')
    plt.show()

#kadai39
def zipf(sentences):
    WordFreq = WordFrequency_extr(sentences)
    sort_word = sorted(WordFreq.keys(), key=lambda x:WordFreq[x],reverse=True)
    Word = sort_word[0:len(sort_word)]
    WordRange = range(1,len(sort_word))
    SortFreq = []
    for i in range(0,len(sort_word)-1,1):
        SortFreq.append(WordFreq[Word[i]])

    x = WordRange
    y = SortFreq

    plt.scatter(x, y)
    plt.show()


def main():
    doc_dest = '/home/viet/Documents/neko.txt.mecab'
    sentences = morp_read(doc_dest)
    #verb_extr(sentences)
    #CustomNoun_extr(sentences,'サ変接続')
    #CompoundNoun_extr(sentences)
    #NounConection_extr(sentences)
    #WordFrequency_extr(sentences)
    #TopWordFrequency(sentences)
    #histogram(sentences)
    zipf(sentences)

if __name__ == '__main__':
    main()