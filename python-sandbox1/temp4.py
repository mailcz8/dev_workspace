import os

file_path = os.path.join(os.path.abspath('testdata'),'test-temp1.txt')

text = '''
FAILED: C62702: HV Charging, Battery In Charging State

FAILED: C62679: Vehicle Closure, Liftgate Ajar Warning Notification

FAILED: C62650: Drivetrain, Gear Position (PRND) View

FAILED: C62659: HV Battery, Available Range View

FAILED: C62702: HV Charging, Battery In Charging State

FAILED: C62679: Vehicle Closure, Liftgate Ajar Warning Notification

FAILED: C62650: Drivetrain, Gear Position (PRND) View
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

for i in get_real_tc_list(text):
    print(i)
