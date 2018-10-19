import controller
import shortcut
import sys
from subprocess import call

import os

#shortcut the user enters
sc = sys.argv[1]
#last argument the user enters
arg = sys.argv[-1]

if sc == "fixit":
    controller.Control()

elif sc != "fixit":
    shortcut.Key(sc,arg)
