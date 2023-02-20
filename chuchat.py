#modules and variables imports
import sys

#dir PATH
sys.path.append('./native')
sys.path.append('./external')
#-------------------------

#program list
programs = ['help', 'exit', 'clear']
#-----------

#loader
def load(shell):

    for i in range(0, len(programs)):
        if programs[i] == shell:
            __import__(programs[i])
            break
        else:
            print("programme inexistant")
#----------------

#chuchat
print("taper '/help' pour connaître la liste des commandes")
def app():
    global shell
    while True :
        
        shell = input("chuchat $ ")
        load(shell)
        app()
        
app()
#----------------
        
        
#shell() # launch the app

"""
TO DO :
a  better program loader - Make !!! :D
imports; call programme by functions and conditions - Make B) 

- Help display program - Make :)

- Account system program 
- Create room program
- Enter in room program + chat system + 'a' update system

- Data system in many files or one single file

- More beautiful interface
"""
