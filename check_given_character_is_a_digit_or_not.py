def check_given_character_is_a_digit_or_not(char_to_check):
    # if char_to_check.isdigit():
    if char_to_check >='0' and char_to_check <='9':
        return True
    else:
        return False
char_to_check = '8'
result = check_given_character_is_a_digit_or_not(char_to_check)
print(result)