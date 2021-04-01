def matcher(text, brackets):
    brackets_open = ["[","{","(", "<"]
    brackets_close = ["]","}",")",">"]
    for x in brackets_open[::-1]:
        pos = brackets_open.index(x)
        if (not x in brackets) and (not brackets_close[pos] in brackets):
            brackets_open.pop(pos)
            brackets_close.pop(pos)
    list = []
    for i in text:
        if i in brackets_open:
            list.append(i)
        elif i in brackets_close:
            pos = brackets_close.index(i)
            if ((len(list) > 0) and (brackets_open[pos] == list[len(list)-1])):
                list.pop()
            else:
                return False, (i, text.index(i)), (list[len(list)-1], text.index(list[len(list)-1]))
    if len(list) == 0:
        return True, None, None

text = input("Введите выражение: ")
brackets = input("Введите скобки: ")
x, y, z = matcher(text, brackets)
print(f'{x}, {y}, {z}')

#x, y, z = matcher("(a+[b*c]-{d/3})", "([")
#print(f'{x}, {y}, {z}')
#x, y, z = matcher("(a+[b*c)-17]", "([")
#print(f'{x}, {y}, {z}')
#x, y, z = matcher("(a+[b*c)-17]", "[")
#print(f'{x}, {y}, {z}')
