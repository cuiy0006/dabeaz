def countdown(n):
    while n >= 0:
        newvalue = yield n
        if newvalue is not None:
            n = newvalue
        else:
            n -= 1


if __name__ == '__main__':
    c = countdown(5)
    for n in c:
        print(n)
        if n == 5:
            c.send(3)


# first yield 5
# second, c.send(3), newvalue = 3, n = 3
# third yield 3, newvalue = None, n -= 1, n = 2
# fourth yield 2, newvalue = None, n -= 1, n = 1
# fourth yield 1, newvalue = None, n -= 1, n = 0, end
