'''from subprocess import call

call(["python"])'''


'''import os
print(os.environ)'''

import os


def ReadLastCommand():
    homedir = os.path.expanduser('~')
    file = open(homedir+'/.bash_history','r')
    lines = file.readlines()
    file.close()
    lastCommand = lines[-1].split('\n')[0]
    return lastCommand


