import time
import os


# tail -f
def follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
     logfile = open('access-log', 'r')
     for line in follow(logfile):
         print(line)
     logfile.close()
