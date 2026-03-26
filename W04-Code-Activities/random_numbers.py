import random

def main():
    numbers =[51.2,30,9,2.5,7]
    print(f"Numbers {numbers}")
    
    # Call the append_random_numbers function to
    # add one random number to the numbers list.
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # Call the append_random_numbers function to add
    # three random numbers to the numbers list.
    append_random_numbers(numbers, 2)
    print(f"numbers {numbers}")

    # Create a list to store random words.
    words = []

    # Call the append_random_words function
    # to add one random word to the list.
    append_random_words(words)
    print(f"words {words}")

    # Call the append_random_words function
    # to add five random words to the list.
    append_random_words(words, 100)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    """Append quantity random numbers onto the numbers list.
    The random numbers are between 0 and 100, inclusive.
    Parameters
        numbers_list: A list of numbers where this function will
            append random numbers.
        quantity: The number of random numbers that this function
            will append onto numbers_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the numbers_list.
    """
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):
    """Append quantity randomly chosen words onto the words list.
    Parameters
        words_list: A list of words where this function will
            append random words.
        quantity: The number of random words that this function
            will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """

    # A list of words to randomly choose from.
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak",
        "sunshine", "toothbrush", "tree", "truth", "walk", "water"
    ]

    # Randomly choose quantity words and append them onto words_list.
    for _ in range(quantity):
        word = random.choice(candidates)
        words_list.append(word)


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
