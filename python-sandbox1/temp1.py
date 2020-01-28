import time

words=('Hello','Welcome','to','GeeksforGeeks',"Monkiy")
num=(1,2,3,5,7)

def myFun(sr,*args):
    print('args =',args)
    for arg in args:
        print('arg =', arg)
        # print(arg)
        for i in arg:
            print(i)
            if sr in i.lower():
                print(sr,'found in',i)
            else:
                print(sr,'not found in',i)
# myFun('e')
# myFun('e',(words))
# myFun('Hello',('Hello', 'WelcomeH', 'GeeksHGeeks'))

# def num_pi(n):
#     list=[]
#     for i in range(1,n+1):
#         list.append(i)
#         print(list)

def run_time(k):
    for k in range(times):
        run_time = time.strftime("%Y/%m/%d_%H:%M:%S",time.localtime())
        print("Executing {0} run at {1}".format(k+1,run_time))
        try:
            print('run can sig {} time'.format(k))
        except Exception as e:
            print(e)

def spy_game(num):
    spy = []
    for i in num:
        if i in (0,7):
            spy.append(str(i))
    return ''.join(spy)=='007'

def spy_pop(num):
    code = [0,0,7,'x']
    for i in num:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1

# print(spy_pop([1,2,0,3,5,8,0,4,5,2,7]))
# print(spy_pop([1,7,2,0,3,5,8,0,4,5,2]))
# spy_game([0,7,0])
# spy_game([0,7])
# spy_game([0,0,7])


def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []
# print(twoSum([2, 7, 11, 15], 9))

def make_chocolate(small, big, goal):
    total_big = big*5
    if goal-total_big == 0:
        return 0
    elif goal > total_big:
      if (goal-total_big) <= small:
        return goal-total_big
      else:
        return -1
    elif goal < total_big:
      res = [i for i in range(big,-1,-1) if goal >= (i * 5)]
      if goal-res[0]*5 == 0:
          return 0
      elif goal-res[0]*5 <= small:
        return goal-res[0]*5
      else:
        return -1
print(make_chocolate(1, 2, 5))

def check(big,goal):
    res = [i for i in range(big, -1, -1) if goal >= (i * 5)]
    return res[0]
print(check(2,4))