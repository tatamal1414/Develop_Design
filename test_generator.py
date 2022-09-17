from datetime import datetime


import datetime

def try_generator():
    for data in (1,2,3,4,5):
        yield data

def main():
    for data in ():
        print(data)
        if data > 2:
            break




list = [i for i in range(100000000)]
gen = (i for i in range(100000000))
# try_generator() == gen

start = datetime.datetime.now()

for i in gen:
    print(i)
    if i >= 3:
        break

finish = datetime.datetime.now()

recode = (finish - start).total_seconds()
print(str(recode) + "秒")
# 0.000055
# 0.000058