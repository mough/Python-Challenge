# root = Logger()
#
# def dictConfig(d):
#     # configures the root logger according to data in d
#
# def getLogger(name, level=DEBUG)


import argparse

parser = argparse.ArgumentParser(description='testing making a command line tool')

parser.add_argument('non-optional', help='some non-optional argument')

parser.add_argument('-f', '--flag', action='store_true', help='some_flag', default=True)


def main(nonoptional, flag=False):
    if flag:
        print('the flag was set')
    else:
        print('nonoptional = %s' % nonoptional)

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    print(type(args))
    print(dir(args))
    main(nonoptional=args.nonoptional, flag=args.flag)
