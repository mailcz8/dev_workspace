a = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2'
def long_dir(str):
  re = []
  a = str.split('\n')
  for i in a:
    k = i.split()
    for i in k:
      f = i.split('.ext')
      # print(f)
      re.append(f[0])
  return re
print(long_dir(a))

class Apple(object):
  def reverse(x):
    re1 = []
    re = []
    flag = True
    for i in x:
      try:
        val = isinstance(int(i), int)
      except:
        re.append(i)
      else:
        if val == True:
          re1.append(i)
        a = ''.join(re1)[::-1]
        re.append(a)
    b = ''.join(re)
    return b
  # print('Inline:',reverse('-123.678'))

if __name__ == '__main__':
  x = Apple
  k = x.reverse('-123.678')
  print(k)
  # print(reverse('-123.678'))

  k = ['dir', 'subdir1', 'file1', 'subsubdir1', 'subdir2', 'subsubdir2']
  for i in k:
    if 'dir' not in i:
      print(i)

def romanToInt(s):
  """
  :type s: str
  :rtype: int
  """
  if not s:  # in case of 0
    return 0
  dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  n = len(s)
  k = s[n - 1]
  total = dic[s[n - 1]]
  for i in range(n - 1, 0, -1):
    current = dic[s[i]]
    prev = dic[s[i - 1]]
    # total += prev if prev >= current else -prev
    if prev >= current:
      total += prev
    else:
      total -= prev
  return total
print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXC'))
print(3,58,1990)


def longestCommonPrefix(strs):
  """
  :type strs: List[str]
  :rtype: str
  """
  prefix = []
  num = len(strs)
  for x in zip(*strs):
    if len(set(x)) == 1:
      prefix.append(x[0])
    else:
      break
  return "".join(prefix)

day_mapping = {
        "monday" : {'weekday':'workday'},
        "tuesday" : {'weekday':'workday'},
        "wednesday" : {'weekday':'workday'},
        "thursday" : {'weekday':'workday'},
        "friday" : {'weekday':'workday'}
    }

day_mapping['satursday'] = {'weekend':'non-workday'}
day_mapping['sunday'] = {'weekend':'non-workday'}

err_code = 2
code = '2'
print(eval(code, str(err_code )))
