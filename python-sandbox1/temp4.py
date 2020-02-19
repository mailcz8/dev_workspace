import os
import re
import random

file_path = os.path.join(os.path.abspath('testdata'),'test-temp1.txt')

text = '''
FAILED: C20183: Liftgate Warning Notification
FAILED: C53546: Battery available Range View
PASSED: P63591: Sunday fun
FAILED: C79117: Battery In Charging State
Passed: C59610: Vehicle Closure Warning Notification
FAILED: C82760: Gear Position (PRND) View
'''

def get_real_tc_list(tc_list):
    total_tc_list = []
    new_tc_list = []
    tc_id = ''
    for i in tc_list.split('\n'):
        if i != '':
            k = i.split()
            tc_id = k[1]
            if tc_id not in total_tc_list:
                total_tc_list.append(tc_id)
                new_tc_list.append(i)
    return new_tc_list

def replace_string(str_to_replace=''):
    search_str = '[0-9]{5}'
    for i in text.split('\n'):
        re_ser = re.search(search_str, i)
        re_match = re.match(search_str, i)
        ran_five_digs = random.randint(10000, 99999)
        i = re.sub(search_str,str(ran_five_digs), i.rstrip())
        print(i)
        # if re.search(search_str, i):
        #     print(i)
        # elif i != '':
        #     print("This string does not containt {}".format(str_to_replace))
        #     print(i)
replace_string()

random_string = '  this is goodbye'

# Leading whitepsace are removed
print('line 1:',random_string.rstrip())

# Argument doesn't contain 'd'
# No characters are removed.
print('line 2:',random_string.rstrip('good'))

print('line 3:',random_string.rstrip('sid oo'))

website = 'www.programiz.com/'
print('line 4:',website.rstrip('m/.'))