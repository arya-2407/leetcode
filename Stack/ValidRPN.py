def evalRPN(tokens: list[str]) -> int:
        stack=[]
        for token in tokens:
            #print(stack) debugging 
            #print(token) debuggind
            if token=="+":
                in_2 = stack.pop()
                in_1 = stack.pop()
                result = in_1 + in_2
                stack.append(result) 
            elif token=="-":
                in_2 = stack.pop()
                in_1 = stack.pop()
                result = in_1 - in_2
                stack.append(result)
            elif token=="*":
                in_2 = stack.pop()
                in_1 = stack.pop()
                result = in_1 * in_2
                stack.append(result)
            elif token=="/":
                in_2 = stack.pop()
                in_1 = stack.pop()
                result = int(float(in_1) / in_2)
                stack.append(result)
            else:
                stack.append(int(token))
            print(stack)
        return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = evalRPN(tokens)
print("Expected : 22")
print("Got " + str(res))