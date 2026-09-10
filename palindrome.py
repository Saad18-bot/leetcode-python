
while True:
    n = input("Enter a number:  ") 
    if (n[::] == n[::-1]):
        print("Number is a palindrome!!")
        break
    else:
        print("Number is not a palindrome!!")
        continue