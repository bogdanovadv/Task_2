
def balance(myStr, brackets):
    openList = ["[","{","("]
    closeList = ["]","}",")"]
    for x in openList[::-1]:
        if not x in brackets:
            pos = openList.index(x)
            openList.pop(pos)
            closeList.pop(pos)
    print(openList)
    print(closeList)
    stack= []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                print(stack[len(stack)-1], " -3- ", myStr.index(stack[len(stack)-1]))
                print(i, " -4- ", myStr.index(i))
                return False, (i, myStr.index(i)), (stack[len(stack)-1], myStr.index(stack[len(stack)-1]))
    if len(stack) == 0:
        return True, None, None

print(balance("(a+[b*c]-{d/3})", "(["))
print(balance("(a+[b*c)-17]", "(["))
print(balance("(a+[b*c)-17]", "["))