from grep import coroutine
from cofollow import follow, printer

@coroutine
def grep(pattern, coro):
    while True:
        line = yield
        if pattern in line:
            coro.send(line)


if __name__ == '__main__':
    f = open('access-log', 'r')
    follow(f, grep('python', printer()))
    f.close()
