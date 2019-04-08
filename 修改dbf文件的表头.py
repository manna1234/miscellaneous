# coding: UTF-8

import os
import os.path
import struct


def modify_header(file, start, value):
    f = open(file, 'rb+')
    # byte=start
    f.seek(0,0)
    temp = f.read(2)
    print(temp)
    f.seek(0,0)
    f.write(value)
    f.close


for root, dirs, files in os.walk('d:\data\m'):
    for file in files:
        if 'dbf' in os.path.splitext(file)[1][1:]:
            print(file)
            modify_header(os.path.join(root, file), 0, b'\x03')