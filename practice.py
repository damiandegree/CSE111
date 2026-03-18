LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

word= input("word: ")
 
def word_has_character(word, character_list):

    for i in list(word):
        word_letter = i
        if word_letter in character_list:
            return True
    return False 

def word_complexity(word):
        complexity_value = 0
        if word_has_character(word, LOWER): 
            complexity_value += 1
        if word_has_character(word, UPPER): 
            complexity_value += 1
        if word_has_character(word, DIGITS): 
            complexity_value += 1
        if word_has_character(word, SPECIAL): 
            complexity_value += 1
        return complexity_value

print(word_complexity(word))