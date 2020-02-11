#!/usr/bin/python

def longestCommonPrefix(strs):
    if not strs: return ""
    if len(strs) == 1: return strs[0]

    strs.sort()
    result = ""
    a = strs[0]
    b = strs[-1]
    for x, y in zip(strs[0], strs[-1]):
        if x == y:
            result += x
        else:
            break
    return result

def test_zip():
    name = ['flymonkey','flyturkey','flpig','flyazk']
    longestCommonPrefix(['monday'])
    print(longestCommonPrefix(name))
    name.sort()
    for k in zip(name):
        print(k)
        for i in k:
            print(i)

def zip_fun():
    name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
    roll_no = [4, 1, 3, 2]
    marks = [40, 50, 60, 70]

    # using zip() to map values
    mapped = zip(name, roll_no, marks)
    for m in mapped:
        print('mapped =', m)
        # if 'Astha' in m[0]:
        #     print(m)
    print(len(m),type(m))
# zip_fun()

# converting values to print as set
roll_no = [43, 1, 3, 299, 3, 3, 5, 7, 99]
roll_no2 = ['cat','zoo','Cat','k','b','z']
# print(set(roll_no2))


# printing resultant values
# print("The zipped result is : ", end="")
# print(mapped)

tup1 = ('physics', 'chemistry', 2000, "world", 1997);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup_emp = ()

tup_to_list = [i for i in tup1 if isinstance(i, str)]
print(type(tup_to_list), tup_to_list)
s = ''.join(' '.join(tup_to_list))
print(type(s), s)