#one.py

def func():
    print('Func() in one.py')

print('Top level in one.py')

if __name__ == '__main__':
    print('one.py is being run directly!')
else:
    print('one.py has been imported!')