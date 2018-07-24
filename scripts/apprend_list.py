import time
import random
colors = ['R',  'G',  'B'  'Y']



def append_list ():	
	n = random.randint (0 , 3)
	colors.append(colors [ n ] )
  	print colors [ i ].lower ( )
   	time.sleep(1)

if  __name__ == '__main__':
   try:
        append_list()
   except KeyboardInterrupt:
	print "Good Bye"
