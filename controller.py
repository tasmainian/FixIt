from subprocess import call
import sys
import matcher

def Control():
    correctCommand = matcher.Match()
    choose = input('Did you mean '+correctCommand+' ? (yes or no) ')
    if (choose == 'yes'):
        call(correctCommand.split(' '))
    else:
        sys.exit(1)

