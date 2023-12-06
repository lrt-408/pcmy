from multiprocessing import Process 
import os

def mpDemo(p_name):
    print(f"{p_name}进程ID：{os.getppid()}")


#class MyProcess(Process):
#    def __init__(self,p_name):
#        Process.__init__(self)
#        self.p_name=p_name
#        self.p_id=p_id

if __name__ == '__main__':
    p = Process(target=mpDemo,args={'mp_1',})
    p.start()
    #等待子进程完事再退出主进程
    p.join()
    print("Done")