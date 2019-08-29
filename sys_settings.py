import os, fnmatch
import os.path

# This is to get the directory that the program  
# is currently running in. 

# dir_path = os.path.dirname(os.path.realpath(__file__)) 

def sys_file_search(dir_path, f_path):
    for root, dirs, files in os.walk(dir_path):
        for f_path in files:
            if f_path.endswith('.png'):
                img = root + '/' + str(f_path)