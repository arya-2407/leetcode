def isValid(s : str) -> bool:
    stack = []
    for c in s:
        if c in ['(','{','[']:
            stack.append(c)
        else:
            if len(stack)==0:
                return False
            else:
                if c==')':
                    check = stack.pop()
                    if check!='(':
                        return False
                elif c=='}':
                    check = stack.pop()
                    if check!='{':
                        return False
                else:
                    check = stack.pop()
                    if check!='[':
                        return False
    if len(stack)==0:
        return True
    else:
        return False

test_1 = "([])" #Valid
test_2 = "(]" #Invalid

print(isValid(test_1)) #True
print(isValid(test_2)) #False
print(isValid("")) #True