import sys
print(sys.argv[0],sys.argv[1],sys.argv[2]) #print filename arg1 arg2
print('Welcome {}.Enjoy {} challenge!'.format(sys.argv[1],sys.argv[2]))
print(sys.maxsize) #largest integer variable can take
print(sys.path) #know environment path
print(sys.version) #know version of python
sys.exit() #exit sys

#at index 0 always name of the script
#at index 1 the argument passed from command line
#Useful Commands
#sys.exit(),sys.maxsize(),sys.path,sys.version