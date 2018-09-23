import follow


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


if __name__ == '__main__':
    logfile = open('access-log', 'r')
    generator_1 = follow.follow(logfile)
    generator_2 = grep('python', generator_1)
    for line in generator_2:
        print(line)
    logfile.close()

