import os
import time
import multiprocessing

def child_task(index):
    print(f"[Child {index+1}]")
    print(f"  PID        : {os.getpid()}")
    print(f"  Parent PID : {os.getppid()}")
    print(f"  Message    : Hello! I am Child {index+1}\n")
    time.sleep(1)

def task1_create_processes(n=3):
    print(f"[Parent] PID: {os.getpid()} - Creating {n} child processes...\n")

    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=child_task, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        print(f"[Parent] Child with PID {p.pid} has terminated.")

if __name__ == "__main__":
    task1_create_processes(n=3)
