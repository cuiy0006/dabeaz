def countdown(n):
    print('Counting down from %d' % n)
    for i in range(n):
        yield i

    print('Done count down')


if __name__ == '__main__':
    for i in countdown(10):
        print(i)
