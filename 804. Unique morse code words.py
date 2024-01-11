class Solution(object):
    def uniqueMorseRepresentations(self, words):
        char=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new=[]
        for word in words:
            newword=""
            word=word.upper()
            for letters in word:
                newword+=char[ord(letters)-65]
            new.append(newword)
        return len(set(new))
