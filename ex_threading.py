from threading import Thread
import time

test = 0

def thread_func():
	global test
	print("thread start:")
	time.sleep(1)
	test += 1
	
	print("thread finish:")
	
def thread2_func():
	global test
	print("thread 2 start:")
	time.sleep(2)
	print(test)
	print("thread 2 finish:")
	
if __name__ == "__main__":
	Thread(target = thread_func , args = ()).start()
	Thread(target = thread2_func , args = ()).start()
