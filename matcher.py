import difflib
import logger


def Match():
    my_str = logger.ReadLastCommand()
    scriptParts = my_str.split(' ')
    command = scriptParts[0]
    str_list = ['python' , 'apt-get', 'git', 'brew', 'nano']
    best_match = difflib.get_close_matches(command,str_list,1)[0]
    scriptParts[0] = best_match
    return ' '.join(scriptParts)
