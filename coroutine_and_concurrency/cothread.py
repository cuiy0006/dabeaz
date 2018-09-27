from grep import coroutune
from queue import Queue
from threading import Thread


@coroutune
def threaded(coro):
    messages = Queue()

    def run_target():
        while True:
            item = messages.get()
            if item is GeneratorExit:
                coro.close()
                return
            else:
                coro.send(item)
    Thread(target=run_target).start()
    try:
        while True:
            item = yield
            messages.put(item)
    except GeneratorExit:
        messages.put(GeneratorExit)
