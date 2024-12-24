def dailyTemperatures(temps: list[int]) -> list[int]:
    res = [0]*len(temps)
    stack=[]

    for i,t in enumerate(temps):
        while stack and t>stack[-1][0]:
            stackT,stackI = stack.pop()
            res[stackI] = i - stackI
        stack.append((t,i))
    return res

temps = [73,74,75,71,69,72,76,73]
res = dailyTemperatures(temps)
print("Expected : [1, 1, 4, 2, 1, 1, 0, 0]" )
print(f"Got : {res}")