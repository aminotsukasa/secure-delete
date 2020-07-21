#!/usr/bin/env python3
# 引数で渡されたファイルをランダムデータで上書きしてから削除する
# undelete対策
import sys,os,random,struct

def writeRandom(file):
    size = os.stat(file).st_size
    print(str(size) + (' byte'))
    for i in range(3):
        with open(file, mode='wb') as f:
            while size > f.tell():
                f.write(struct.pack("B", random.randint(0, 255)))
#                print('byte='+str(f.tell()))
            f.flush()
            os.fsync(f.fileno())

for arg in sys.argv[1:]:
    if (os.path.isfile(arg)):
        print(arg)
        writeRandom(arg)
        os.unlink(arg)
