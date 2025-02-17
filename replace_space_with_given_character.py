def replace_space_with_given_character(string1,char_to_replace_in_position_of_a_space):
    res = ''
    for i in string1:
        if i == ' ':
            i = char_to_replace_in_position_of_a_space
        res+=i
    return res
string1 = "HEllo all, I am Shruthi"
char = 't'
result_after_replacing = replace_space_with_given_character(string1,char)
print(result_after_replacing)