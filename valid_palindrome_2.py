s = "A man, a plan, a canal: Panama"

sen = ""

for i in range(len(s)):

    if s[i].isalnum() == True:
        sen = sen + s[i].lower()
print(sen)
if sen == sen[::-1]:
    print("Its a palindrome!!")
else:
    print("Its not a palindrome!!")