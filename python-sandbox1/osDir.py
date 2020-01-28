import os

def print_directory_contents(sPath="."):
    print(os.listdir(sPath))
    for sChild in os.listdir(sPath):
        print('sPath = {} , sChild = {}'.format(sPath,sChild))
        sChildPath = os.path.join(sPath,sChild)
        print('sChildPath = {}'.format(sChildPath))
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print('else = ' + sChildPath)

str1 = 'Hello World!!!'
dirInfo = '.'
print(os.listdir(dirInfo))
print(os.system('pwd'))
print(os.replace(str1,'?'))