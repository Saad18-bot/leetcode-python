s = "()[]{}{[]}"
stk = []
for i in range(len(s)):

    if s[i] == "(":
        stk.append("(")

    elif s[i] == "[":
        stk.append("[")

    elif s[i] == "{":
        stk.append("{")

    elif s[i] == ")" :
        if not stk or stk[-1] != "(":
            print("Invalid Parentheses")
            exit()
        stk.pop()

    elif s[i] == "]":
        if not stk or stk[-1] != "[":
            print("Invalid Parentheses")
            exit()
        stk.pop()

    elif s[i] == "}":
        if not stk or stk[-1] != "{":
            print("Invalid Parentheses")
            exit()
        stk.pop()

if stk == []:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")