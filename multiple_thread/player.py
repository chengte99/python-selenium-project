from time import ctime, sleep
import threading

def superplayer(file_, time):
    for i in range(2):
        print('Start player %s %s' % (file_, ctime()))
        sleep(time)

threads = []

lists = {'kevin':2, 'jason':3, 'ppap':4}
files = range(len(lists))

for file_, time in lists.items():
    t = threading.Thread(target=superplayer, args=(file_, time))
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('all end: %s' % ctime())
