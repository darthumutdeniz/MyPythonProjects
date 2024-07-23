def PascalTree(n):
    pascallines = [[1]]
    for i in range(1, n + 1):
        pascallines.append([])
        for j in range(0, len(pascallines[i - 1]) + 1):
            if j < 1 or j == len(pascallines[i - 1]):
                pascallines[i].append(1)
            else:
                newNum = pascallines[i - 1][j - 1] + pascallines[i - 1][j]
                pascallines[i].append(newNum)
    return pascallines


n = int(input("Kaç satır"))
tree = PascalTree(n)
for i in range(0, len(tree)):
    print("", end="")
    for f in range(0, len(tree) - i):
        print(" ", end="")
    for j in range(0, len(tree[i])):
        print(tree[i][j], end="")
        if not i == len(tree) - 1 and not j == len(tree[i])-1:
            allLenghts = []
            for l in range(i, len(tree)):
                allLenghts.append(len(str(tree[l][j+1])))
                maxnum = max(allLenghts)
            for k in range(0,maxnum):
                print(" ", end="")
        else:
            print(" ", end="")
    print("")