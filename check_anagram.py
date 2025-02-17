string1 = "mada"
string2 = "dama"
if len(string1) != len(string2):
    print("They are not anagram")
else:
    if sorted(string1) == sorted(string2):
        print("They are anagram")