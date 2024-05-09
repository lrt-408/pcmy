import os
import time
import shutil
import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        try:
            # 创建in和out文件夹
            if not os.path.exists('in'):
                os.makedirs('in')
            if not os.path.exists('out'):
                os.makedirs('out')

            while True:
                # 扫描in文件夹
                files = os.listdir('in')
                for file in files:
                    if file == 'exit.txt':
                        print("Found exit.txt. Exiting the process.")
                        return
                    else:
                        file_path = os.path.join('in', file)
                        if os.path.isfile(file_path):
                            shutil.copy(file_path, 'out')
                            print(f"Copied {file} from in to out folder")

                # 休眠1秒
                time.sleep(1)

        except Exception as e:
            print("An error occurred:", e)

if __name__ == '__main__':
    my_process = MyProcess()
    my_process.start()