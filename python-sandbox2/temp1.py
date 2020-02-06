import time
import re

words=('Hello','Welcome','to','GeeksforGeeks',"Monkiy")
num=(1,2,3,5,7)

data = """bob
  123 -- things  
stuff after that line"""

def find_str(ser_str):
    re1 = re.search(r'{}'.format(ser_str),  data)
    re2 = re.search(r'{}'.format(ser_str), data).group(1)
    print(type(re1), re1)
    print(type(re2), re2)

    for ser_str in data.splitlines():
        # print(ser_str)
        if ' -- ' in ser_str:
            print(ser_str.strip())
            print(ser_str.strip().split(' -- ', 1)[1])

find_str('--(.*.*)')