# string1 = "Hello, My name is Tino"
# char_to_count = 'e'
# count = 0
# for i in string1:
#     if i == char_to_count:
#         count+=1
# print(count)

#
string = "Hello world ll"
char = 'l'
freq = {}
for i in string:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq.get(char,0))
# print(string.count(char))




