#!/usr/bin/env python3

import sys
from subprocess import call

#shortcut the user enters
sc = sys.argv[1]
#last argument the user enters
arg = sys.argv[-1]

#displays different shortcuts for commands
if sc == "menu":
    sys.stdout.write("ShortCut Options\ng1 - git tag \tg2 - git show 'tag' \ts1 -  ssh 'username'@moore.mcmaster.ca\n")

elif sc == "g1":
    call(["git", "tag"])

elif sc == "g2":
    call(["git", "show", arg])

elif sc == "s1":
    user = arg + "@moore.mcmaster.ca"
    call(["ssh", user])
    
