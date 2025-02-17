def check_given_character_is_a_vowel_or_not(char_to_check):
    vowels = ['a','e','i','o','u']
    char_to_check = char_to_check.lower()
    if char_to_check in vowels:
        print("It is a vowel")
    elif char_to_check.isalpha():
        print("It is a consonant")
    else:
        print("It is other than vowel or a consonant")
char_to_check = 'E'
check_given_character_is_a_vowel_or_not(char_to_check)
