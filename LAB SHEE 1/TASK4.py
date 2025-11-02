import psutil
import os
import sys

def print_proc_status(proc):
    print("\n Process Status Info:")
    print(f"  Name          : {proc.name()}")
    print(f"  PID           : {proc.pid}")
    print(f"  Status        : {proc.status()}")
    print(f"  Memory (MB)   : {proc.memory_info().rss / 1024 / 1024:.2f}")
    print(f"  CPU Percent   : {proc.cpu_percent(interval=0.1)}%")

def print_exe_path(proc):
    print("\n Executable Path:")
    try:
        print(f"  {proc.exe()}")
    except Exception as e:
        print(f" Failed to get executable path: {e}")

def print_open_files(proc):
    print("\n Open Files:")
    try:
        files = proc.open_files()
        if files:
            for f in files:
                print(f"  - {f.path}")
        else:
            print("  (No open files found)")
    except Exception as e:
        print(f" Failed to list open files: {e}")

def main():
    if len(sys.argv) > 1:
        try:
            pid = int(sys.argv[1])
            proc = psutil.Process(pid)
        except Exception as e:
            print(f" Invalid PID: {e}")
            return
    else:
        proc = psutil.Process(os.getpid())  # default to current process

    print_proc_status(proc)
    print_exe_path(proc)
    print_open_files(proc)

if __name__ == "__main__":
    main()
