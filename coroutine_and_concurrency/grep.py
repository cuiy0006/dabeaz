
def coroutine(func):
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return start


@coroutine
def grep(pattern):
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('Generator closed!')


if __name__ == '__main__':
    g = grep('python')
    g.send('python, but no, but yeah, but no')
    g.send('A series of tubes')
    g.send('python generators rock')
    g.close()
