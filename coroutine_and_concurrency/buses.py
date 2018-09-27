from grep import coroutine


@coroutine
def buses_to_dicts(coro):
    while True:
        event, value = yield
        if event == 'start' and value[0] == 'bus':
            busdict = {}
            fragments = []
            while True:
                event, value = yield
                if event == 'start':
                    fragments = []
                elif event == 'text':
                    fragments.append(value)
                elif event == 'end':
                    if value != 'bus':
                        busdict[value] = ''.join(fragments)
                    else:
                        coro.send(busdict)
                        break


@coroutine
def filter_on_field(fieldname, value, target):
    while True:
        d = yield
        if d.get(fieldname) == value:
            target.send(d)


@coroutine
def bus_locations():
    while True:
        bus = yield
        print("%(route)s,%(id)s, %(direction)s , %(latitude)s, %(longitude)s" % bus)


if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler
    xml.sax.parse('allroutes.xml',
                  EventHandler(
                      buses_to_dicts(
                          filter_on_field("route",
                                          '147',
                                          filter_on_field('revenue',
                                                          'true',
                                                          bus_locations()))
                      )
                  ))

    from coexpat import expat_parse
    expat_parse(open('allroutes.xml'),
                buses_to_dicts(
                          filter_on_field("route",
                                          '147',
                                          filter_on_field('revenue',
                                                          'true',
                                                          bus_locations()))
                      ))
