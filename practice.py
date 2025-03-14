vowels=['a','e','i','o','u']
string = "Hello, i am Shuji"
string = string.lower()
print(string)
vcount = 0
acount = 0
for i in string:
    if i in vowels:
        vcount+=1
    elif i.isalpha():
        acount+=1
print(vcount,acount)