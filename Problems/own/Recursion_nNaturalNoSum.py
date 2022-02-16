Var = 0


def trail(a):
    if a < 0:
        return 0
    else:
        return a + trail(a-1)


x = trail(5)
print(x)