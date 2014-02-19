import sys
import string
import itertools


# Numbers < Uppercase < Lowercase
characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
my_alphabet = [c for c in characters]

def custom_key(word):
    weight = []
    for char in word:
        weight.append(my_alphabet.index(char))
        # the first chars in my_alphabet have a lower weight than the later,
        #     the sort function sorts by an ascending order.
    return weight

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:

        for test in test_cases:
            if test == "\n":
                pass
            if test[-1] == "\n":
                test = test[:-1]

            perms = list(itertools.permutations(test))
            str_list = ["".join(s) for s in perms]
            # sort by the characters string
            # Numbers < Uppercase < Lowercase
            str_list.sort(key=custom_key)
            print(",".join(str_list))