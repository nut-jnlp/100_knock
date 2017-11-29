reverse_string
def kadai0(s):
    txt=''
    for i in xrange(len(s)-1, -1, -1):
        txt += s[i]
    return txt

#1 split_string: MPyaktQrBoilk RCSahr
def kadai1(s):
    txt=''
    for i in xrange(1, len(s), 2):
        txt += s[i]
    return txt

#2 join string: Partrol and Car
def kadai2(s1,s2):
    txt=''
    for i in xrange(0, len(s1), 1):
        txt += s1[i]
    for i in xrange(0, len(s2), 1):
        txt += s2[i]
    return txt

#3 Tokenize and statistical: Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.
def kadai3(s):
# menthod 1
    txt = []
    i,j=0,0

    while (1):
        txt1 = ''
        while (s[i]!=' ')and(s[i]!=',')and(s[i]!='.')and(s[i]!=':'):
            txt1+=s[i]
            i+=1
        if txt1!='': txt.append(txt1)
        i += 1
        if i >= len(s): break
    print ('-- menthod 1')
    print txt
# menthod 2
#    print ('-- menthod 2')
    import re
#    print re.split('[, .]+',s)
# menthod 3 need Natural Language Toolkit
#    print ('-- menthod 3')
#    import nltk
#    print nltk.tokenize(s)

##--- word counter
    word_count = []
    for w in txt:
        word_count.append(len(w))
 #   print word_count

    return txt

#4 Tokenize and : Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.
def kadai4(s):
    txt = kadai3(s)
    Word_char = {}
    pos = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for i in xrange(len(txt)):
        word = txt[i]
        if i+1 in pos:
            Word_char[word[0]] = i + 1
        else:
            Word_char[word[0:2]] = i + 1
    print Word_char
    return Word_char

#5 n-gram 'I am an NLPer'
def kadai5(txt, n):
    txt_copy = []
    txt_gram = []
    txt_copy[:] = txt
    txt_copy.insert(0, '/Str_begin/')
    txt_copy.append('/Str_end/')
    for i in xrange(len(txt_copy)):
        first_char=i
        last_char=i+n-1
        if last_char>=len(txt_copy):
            break
        txt_gram.append(''.join(txt_copy[first_char:last_char+1]))
    print txt_gram
    return txt_gram

#6
def kadai6(txt, n):
    txt1='paraparaparadise'
    txt2='paragraph'
    X=set(kadai5(txt1,n))
    Y=set(kadai5(txt2,n))
    print 'X: %s' %X
    print 'Y: %s' %Y
    print 'union:           %s' % X.union(Y)
    print 'intersection:    %s' % X.intersection(Y)
    print 'difference:      %s' % X.difference(Y)
    print 'bi-gram "se" is ' + ('in' if 'se' in X else 'not in') + ' X'
    print 'bi-gram "se" is ' + ('in' if 'se' in Y else 'not in') + ' Y'

#7 input and output
def kadai7():
    x,y,z = raw_input("enter x,y,z: ").split()
    print unicode(y) + ' when ' + unicode(x) + ' is ' + unicode(z)

#8 cipher
def kadai8(txt):
    char_fix = ""
    for char in txt:
        if char.islower():
            char_fix += chr(219-ord(char))
        else:
            char_fix += char
    print char_fix

    return char_fix

#9 Typoglycemia I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind.
def kadai9(txt):
    import random
    words=kadai3(txt)
    word_shuffle = []

    for word in words:
        if len(word)>=4:
            need_shuffle_word = list(word[1:-1])
            random.shuffle(need_shuffle_word)
            word = word[0] + ''.join(need_shuffle_word) + word[-1]
        word_shuffle.append(word)

    print word_shuffle

#main
def main():
    s="I couldn't believe that I could actually understand what I was reading: the phenomenal power of the human mind."
    kadai9(s)

if __name__ == '__main__':
    main()
