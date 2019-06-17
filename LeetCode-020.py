s = "()[]{}"
mapping = {")": "(",
           "]": "[",
           "}": "{"
           }
stack = []
for char in s:
    if char in mapping:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if top != mapping[char]:
                print(False)
    else:
        stack.append(char)
print(not stack)


