class Args(object):
    def first(self):
        print('This is ', __class__, __file__)

    def s_args1(self, *args):
        print(type(args), len(args))
        print(args)
        if len(args) == 1:
            for i in args:
                print(sum(i) * 0.5)
        else:
            print(sum(args) * 0.5)

    def s_args2(self, *args):
        print(type(args), args, 'total =', len(args))
        k = []
        for i in args:
            if i % 2 == 0:
                k.append(i)
        print(k)
        return k

    def s_args3(self, *args):
        for arg in args:
            print(arg)
        # return k

    def ss_kwargs1(self, **kwargs):
        print(type(kwargs), kwargs, 'total =', len(kwargs))
        if 'fruit' in kwargs:
            print('My fruit of choice is {}'.format(kwargs['fruit']))
        else:
            print('I don\'t find any fruit here')

    def ss_kwargs2(self, *args, **kwargs):
        print('I wrould like {} {}'.format(args[0], kwargs['food']))

    def ss_kwargs3(self, *args, **kwargs):
        print(args)
        print(kwargs)
        for i in args:
            print(i)
        for i in kwargs:
            print('My {} of choice is {}'.format(i, kwargs[i]))

    def change_letter_casing(self, str):
        newStr = []
        str = list(str)
        for i in range(len(str)):
            if i % 2 == 0:
                newStr.append(str[i].upper())
            else:
                newStr.append(str[i].lower())
        print(''.join(newStr))

if __name__ == '__main__':
    x=(20,30,40,50,60,70,90)
    word=('Hello', 'Welcome', 'to', 'GeeksforGeeks')

    ar = Args()
    ar.s_args3((word))
    ar.s_args3('Hello', 'Welcome', 'to', 'GeeksforGeeks')