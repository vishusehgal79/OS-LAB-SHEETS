import multiprocessing
from subtask2 import system_process
if __name__ == '__main__':
	print("System Starting...")
	p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
	p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
	p1.start()
	p2.start()
	
    # Wait for processes to complete
	p1.join()
	p2.join()
	print("System Shutdown.")
