#You are a junior software developer working for a cellular phone service provider. 
# Your company employs hundreds of workers ranging from customer support to cell tower engineers. 
# The security team has recently discovered a breach of security that they attribute to users 
# using easy to guess passwords. To help train users to create better passwords, management 
# has asked your team to create a password strength checker. This tool will allow employees 
# to get feedback on the strength of their passwords.

#I opened the files.
with open("wordlist.txt", "r", encoding="utf-8") as dictionary_list,open("toppasswords.txt", "r", encoding="utf-8") as toppasswords_lits:

#In the following lines I defined the functions:

def main():
#Provides the user input loop. The loop asks the user for a password to test. 
# If that password is anything but "q" or "Q" call the password_strength function and report 
# the results to the user. If the user enters "q" or "Q", quit the program.
    password = input("Enter a password to test. Type Q to quit the programm: ")
    #I have to add the loop but I organized the requirements
    print(password)


def world_in_file(word,filename,case_sensitive):
    pass
def word_has_character(word,character_list):
    pass                    
def word_complexty(word):
    pass
def password_strenght(password,min_lenght,strong_length):
    pass

if __name__ == "__main__":
    main()