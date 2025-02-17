def remove_character_from_a_string(string1,char_to_remove):
    remove_char= string1.replace(char_to_remove," ")
    return remove_char
string1 = "Hello I am here."
char_to_remove = 'e'
result=remove_character_from_a_string(string1, char_to_remove)
print(result)
