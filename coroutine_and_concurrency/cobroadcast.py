from grep import coroutine
from copipe import grep
from cofollow import follow, printer


@coroutine
def broadcast(coros):
    while True:
        line = yield
        for coro in coros:
            coro.send(line)


if __name__ == '__main__':
    f = open('access-log', 'r')
    p = printer()
    follow(f, broadcast(
        (
            grep('python', p),
            grep('ply', p),
            grep('swig', p)

        )))
    f.close()