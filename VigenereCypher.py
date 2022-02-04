#Task: produce a program that can encrypt and decrypt a string using a Vigenere cypher
# A Vignere cypher uses a secret key to encode a string
#  
import re


class Vigenere_cipher(object):
    def __init__(self):
        self.tabularecta = self.createtabularecta() #Dunder method to initialize objects within vigenerecipher class

    def createtabularecta(self): #generates a tabular recta with unicode
        tabularecta = []
        for r in range(0, 26): #generates the rows in the tabula recta
            offset = 0
            row = []
            for column in range(0, 26):
                row.append(chr(r + 65 + offset))
                offset += 1
                if offset > (25 - r):
                    offset = offset - 26
            tabularecta.append(row)
        return tabularecta #returns a tabula recta object
    
    def encipher(self, plaintext, keyword):
        plaintext = self.processplaintext(plaintext) #calls the processplaintextfunction to be defined later
        keywordrepeated = self.getkeywordrepeated(keyword, len(plaintext)) #loops the keyword if the plaintext is longer than the keyword
        cyphertext = [] #new list for outputted encoded test

        for index, letter in enumerate(plaintext):
            plaintextindex = ord(letter.upper()) - 65 #finds index in tabula recta of plaintext characters
            keywordindex = ord(keywordrepeated[index]) - 65 # finds index in tabula recta of keyword characters by converting characters to unicode and adjusting
            encypheredletter = self.tabularecta[keywordindex][plaintextindex]
            cyphertext.append(encypheredletter)
        return "".join(cyphertext)

    def decipher(self, cyphertext, keyword):
        keywordrepeated = self.getkeywordrepeated(keyword, len(cyphertext))
        decypheredtext = []

        for index, letter in enumerate(cyphertext):
            keywordindex = ord(keywordrepeated[index]) - 65
            decypheredletter = chr(self.tabularecta[keywordindex].index(letter) + 65)
            decypheredtext.append(decypheredletter)
        return "".join(decypheredtext)
    
    def processplaintext(self, plaintext):
        plaintext = plaintext.upper()
        plaintext = re.sub("[^A-Z]", "", plaintext)
        return plaintext
    
    def getkeywordrepeated(self, keyword, length):
        keyword = keyword.upper()
        keywordrepeated = []
        keywordlength = len(keyword)
        keywordindex = 0

        for i in range(0, length):
            keywordrepeated.append(keyword[keywordindex])
            keywordindex += 1
            if keywordindex > keywordlength - 1:
                keywordindex = 0
        return "".join(keywordrepeated)

vc = Vigenere_cipher()

def encypher():
    plaintext = input("Please input string to be enciphered: ")
    keyword = input("Please input key: ")
    return f"Encoded text: {vc.encipher(plaintext, keyword)}"

def decypher():
    enciphered = input("Please input encyphered string: ")
    keyword = input("Please input keyword: ")
    return f"Decoded text: {vc.decipher(enciphered, keyword)}"


def cypherdemo():
    print("-------------------")
    print("| Vigenere Cipher |")
    print("-------------------\n")

    while True:
        start = input("""What would you like to do?: 
        1. Encode
        2. Decode\n""")
        if start == "1":
            print(encypher())
        elif start == "2":
            print(decypher())
        else:
            print("invalid")

cypherdemo()