import pickle
from grep import coroutine


@coroutine
def sendto(f):
    try:
        while True:
            item = yield
            pickle.dump(item, f)
            f.flush()
    except GeneratorExit:  # StopIteration
        f.close()


@coroutine
def recvfrom(f, coro):
    try:
        while True:
            item = pickle.load(f)
            coro.send(item)
    except EOFError:
        coro.close()
