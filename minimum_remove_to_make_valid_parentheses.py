def minRemoveToMakeValid(self, s):
    stack = []
    n = len(s)
    s = list(s)

    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if stack: 
                stack.pop()
            else:
                s[i] = ""
    
    for j in stack:
        s[j] = ""
    
    return "".join(s)