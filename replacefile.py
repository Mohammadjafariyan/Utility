import os
import shutil
import psutil
import ctypes

new_file_path="Test.Shell.dll"

target_dir ="./"

file_to_replace="Test.Shell.dll"

def kill_process_using_file(filepath):
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            open_files = proc.info['open_files'] or []
            for open_file in open_files:
                if open_file.path == filepath:
                    print(f"Terminating process {proc.info['name']} (PID {proc.info['pid']}) using the file.")
                    proc.terminate()  # Or use proc.kill() if terminate doesn't work
                    proc.wait()  # Wait for the process to fully terminate
                    return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return False


for dirpath,dirnames,filenames in os.walk(target_dir):
    for filename in filenames :
        if(filename== file_to_replace):

            file_path = os.path.join(dirpath,filename)

            print(f"replacing : {file_path}")

            # Attempt to kill any process using the file
            if not kill_process_using_file(file_path):
                print(f"No process found using the file: {file_path}")
            else:
                print(f"Process using the file was terminated: {file_path}")

            # Now attempt to replace the file
            try:
                shutil.copy2(new_file_path, file_path)
                print(f"Replaced: {file_path}")
            except PermissionError as e:
                print(f"Failed to replace {file_path} due to: {e}")



print(" replace ment completed " )
