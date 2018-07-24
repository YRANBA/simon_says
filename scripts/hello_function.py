import time 


def hello ():
   while True:  
  	print "Hello World!"
   	time.sleep(1)

if  __name__ == '__main__':
   try:
        hello()
   except KeyboardInterrupt:
	print "Good Bye"
