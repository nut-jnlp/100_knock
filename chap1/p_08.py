# -*- coding: UTF-8 -*-

def ciper(word):

    chars = [chr(219-ord(char)) if char.islower() else char for char in word]
    return (''.join(chars))

english_message = "This is a message"
cryped_message = ciper(english_message)
print(english_message, cryped_message, ciper(cryped_message), sep=' -> ')
