#zombie process
import multiprocessing
import os
import time

def child_process():
    print(f"[Child] PID: {os.getpid()} - Exiting immediately.")
    return

def create_zombie_simulation():
    print(f"[Parent] PID: {os.getpid()} - Creating a child process...\n")

    p = multiprocessing.Process(target=child_process)
    p.start()

    print(f"[Parent] Child PID: {p.pid}")
    print(f"[Parent] Simulating zombie (child exited, but parent hasn’t joined yet)...\n")

    time.sleep(5)  
    print(f"[Parent] Cleaning up the zombie by joining child process.")
    p.join()

    print(f"[Parent] Child {p.pid} cleaned up properly.\n")

if __name__ == "__main__":
    create_zombie_simulation()


#orphan process
import multiprocessing
import os
import time

def child_process():
    print(f"[Child] PID: {os.getpid()} - Parent may exit soon.")
    time.sleep(5)
    print(f"[Child] PID: {os.getpid()} - Still running after parent exited.\n")

def create_orphan_simulation():
    print(f"[Parent] PID: {os.getpid()} - Creating a child process...\n")

    p = multiprocessing.Process(target=child_process)
    p.start()

    print(f"[Parent] Exiting immediately. Child ({p.pid}) becomes orphan-like.")
    return

if __name__ == "__main__":
    create_orphan_simulation()
