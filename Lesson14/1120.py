
import threading as th
import time


def my_thread(a):
    print("start")
    time.sleep(a)
    print(a)
    print("end")

print(th.enumerate())
t1 = th.Thread(target=my_thread, args=(5,))
t2 = th.Thread(target=my_thread, args=(2,))
#print(th.active_count())
#print(th.enumerate())#主线程线程ID-10984

t1.daemon=True
t1.start()
#t1.join()
print(th.enumerate())
#t2.daemon=True
t2.start()
print(th.enumerate())

print("main thread end")