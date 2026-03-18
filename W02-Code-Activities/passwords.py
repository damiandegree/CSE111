LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]



def word_in_file(filename, word,case_sensitive=False):

        with open(filename, "r", encoding="utf-8") as file:
         
         for i in file:
            list_word = i.strip()

            if word == list_word:
                return True
        return False


def word_has_character(word, character_list):

    for i in list(word):
        word_letter = i.strip()

    for j in character_list:
            character = j
            if word_letter == character:
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

def password_strength(password, min_length=10, strong_length=16):
    
    if word_in_file("wordlist.txt",password,case_sensitive=False):
        print("Password is a dictionary word, is not secure.")
        return 0
    if word_in_file("toppasswords.txt",password,case_sensitive=False):
        print("Your password is like other password, is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short.")
        return 1
    if len(password) > strong_length:
        print("Password is long and secure")
        return 5
    
    complexity = word_complexity(password)

    strengh = 1 + complexity

    return strengh


def main():
    while True:
        password = input("Enter password ('Q' to quit): ")
        if password.lower() == 'q':
            print("Goodbye!")
            break
        
        strengh = password_strength(password)
        print(f"Strength level: {strengh}")

if __name__ == "__main__":
    main()

    