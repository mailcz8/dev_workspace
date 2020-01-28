import re
import time

print(time.strftime('%Y%m%d-%H:%M:%S'))
# print(time.strftime("%y%m%d%H%M.%S",time.localtime()))
# print(time.strftime("%m%d%H%M%Y.%S",time.gmtime()))

a = 'sundaymondayfriday'
b = 'day'
c = 'day'
ser = re.search(b, a)
mat = re.match(c, b)
fall = re.findall(b, a)
sergroup = re.search(b, a).group(0)

# print(ser, bool(ser), ser.start(), ser.end())
# print(sergroup)
# print(mat, bool(mat))
# print(fall, len(fall))
# print("="*3,re.search('mon|fri',a))

# a = 'Sunday monday_friday!@#$%Tuesday!@#$%^&*(@#$%!@#$%^&#@$%^&'
# print(re.findall('\w\w\w\w', a))
# print(re.findall('\w\w\W', a))
# print(re.search(r'\w+\W+\w+', a).group())
#
# a = 'abcde         fghijk'
# print(re.search('\w+\W+\w+', a).group())
# print(re.search('\w{3}', a).group())
#
# a = 'aaaaa     aaaaa'
# print(re.search('\w{2,4}\W{1,}\w{3}', a).group())

a = '23adgasd FDGDFG@$%^*&  341234'
# print(re.findall('\d+', a))
# print(re.search('\D+', a).group())
# print(re.findall('\s+', a))
# print(re.findall('\S+', a))

a = '''Python Regular expressions -part #4 
someone@emailaddress.com - 
Character Sets - Custom@Character.io sets
'''
print(re.findall(r'\S+', a), len(re.findall(r'\S+', a)))
a = '_'.join(re.findall(r'\S+', a))
a = a.split('_')
k = []
for i in a:
    i = i.strip('-').lower()
    if i != '':
        k.append(i)

k = '''Python Regular expressions -P,art #4 
someone@emailaddress.com - who i,s there to work@king.org
Character Sets :- Cus23_tom@Character.ok sets
'''
print(re.findall('\S+@\S+\.\w{2,3}', k))
print(re.search('.+', k).group())
print(re.findall('[A-Z,\s.]', k), len(re.findall('[A-Z,:.]', k)))

s = re.findall('[A-Z,\s.]', k)
print(s, len(s))

myL = [1, 2, 3, 4, 5]
my_nums = (x*x for x in myL)
print(list(my_nums))
for i in my_nums:
    print(i)
