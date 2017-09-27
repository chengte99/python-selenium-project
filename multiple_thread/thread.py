from time import sleep, ctime
import threading

def music(func, loop):
    for i in range(loop):
        print('I was listening %r! %r' % (func, ctime()))
        sleep(2)

def movie(func, loop):
    for i in range(loop):
        print('I was watching %r! %r' % (func, ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=('kevin', 2))
threads.append(t1)
t2 = threading.Thread(target=movie, args=('jason', 3))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print('all end:', ctime())
