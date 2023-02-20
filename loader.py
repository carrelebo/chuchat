

#modules and variables imports
import sys
from chuchat import shell

#dir PATH
sys.path.append('./navtive')
sys.path.append('./external')

programs = ['help', 'exit', 'clear']

def initializer(shell):

    for i in range(0, len(programs)):
        if programs[i] == shell:
            __import__(programs[i])
            break
        else:
            print("programme inexistant")

initializer(shell)