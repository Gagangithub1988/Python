list=["a","e","i","o","u","A","E","I","O","U"]
def vowel(str):
    if str in list:
        print("The letter is vowel")

    else:
        print("The letter isn't vowel")

vowel("o")


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('E'))

def check(n):
    list=[1, 5, 8, 3]
    return n in list
print(check(2))