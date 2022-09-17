from datetime import datetime
from importlib.util import find_spec
from random import random


import random
import datetime
from xmlrpc.client import SafeTransport

a = {random.randint(0,100000000) for i in range(0, 1000000)}

b = [random.randint(0,100000000) for i in range(100)]

start = datetime.datetime.now()

for temp in b:
    if temp in a:
        print(f'temp:{temp} in a')


finish = datetime.datetime.now()


record = (finish-start).total_seconds()
print(record)