import time
from grep import coroutine


def follow(thefile, coro):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        coro.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


if __name__ == '__main__':
    f = open('access-log', 'r')
    follow(f, printer())
    f.close()
