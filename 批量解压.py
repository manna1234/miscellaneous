# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:43:17 2017

@author: manna
## python 3.5.4 测试通过。
"""


import os
import time
import threading
import subprocess

# reload(sys)
# sys.setdefaultencoding('utf-8')


def find(name, *types):
    for root, dirs, files in os.walk(name):
        for f in files:
            if os.path.isfile(os.path.join(root, f)) and os.path.splitext(f)[1][1:] in types:
                print(os.path.join(root, f))


def unzip(name, *types):
    # print(name)
    for root, dirs, files in os.walk(name):
        for f in files:
            # print(f)
            if os.path.isfile(os.path.join(root, f)) and os.path.splitext(f)[1][1:] in types:
                print(os.path.join(root, f))
                unzip_command = u'"C:\\Program Files\\7-Zip\\7z.exe" x -y {} "-o{}\\*" -r'.format(os.path.join(root, f), unzip_dir)
                # unzip_command= u'"unzip.exe" {} -d {}*'.format(os.path.join(root,f), unzip_dir)
                print(unzip_command)
                if os.system(unzip_command):
                    if subprocess.call(unzip_command, shell=True):
                        print(u'upzip successful!!!')


if __name__ == '__main__':
    source_dir = "."
    unzip_dir = '.'  # 创建解压缩文件存储路径
    t1 = time.time()
    # 加入线程，搜索D盘 以.rar、7z\.zip结尾的文件
    t = threading.Thread(target=unzip, args=(source_dir, "zip", "7z"))
    t.start()
    t.join()
    # 计算执行时间
    print(time.time()-t1)
