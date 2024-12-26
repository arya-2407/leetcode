def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [(p,s) for p,s in zip(position,speed)]
    stack = []
    pair.sort(reverse=True)

    for p,s in pair:
        stack.append((target-p) / s)
        if len(stack)>=2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

target=10
position=[4,1,0,7]
speed=[2,2,1,1]
res = carFleet(target,position,speed)
print("Expected : 3")
print("Got : " + str(res))  