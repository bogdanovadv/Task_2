def magic(N):
    a = [[None] * N for i in range(N)]
    x, y, dx, dy = 0, 0, 1, 0
    for i in range(N ** 2):
        a[y][x] = i + 1
        line = x + dx if dx else y + dy
        if line < 0 or line == N or a[y + dy][x + dx] != None:
            dx, dy = -dy, dx
        x += dx
        y += dy

    for y in range(N):
        for x in range(N):
            space = len(str(N ** 2)) - len(str(a[y][x])) + 1
            print(*[a[y][x]], end=space * (" "))
        print()
        # print(*[a[y][x] for x in range(N)])

try:
    N = int(input("Введите число N, где 4<=N<=1000: "))
    if 4 <= N and N <= 1000:
        magic(N)
    else: print("Число не соответствует условию")
except ValueError:
    print("Введено не целое число")