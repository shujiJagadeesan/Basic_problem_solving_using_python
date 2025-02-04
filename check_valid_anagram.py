def check_valid_anagram(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    char_counts = [0] * 26
    len_of_string_1 = len(string_1)
    for i in range(len_of_string_1):
        char_counts[ord(string_1[i]) - ord('a')] += 1
        char_counts[ord(string_2[i]) - ord('a')] -= 1
    return all(count == 0 for count in char_counts)
string_1 = "bat"
string_2 = "tab"
are_anagrams = check_valid_anagram(string_1,string_2)
if(are_anagrams):
    print("They are anagrams")
else:
    print("They are not anagrams")
