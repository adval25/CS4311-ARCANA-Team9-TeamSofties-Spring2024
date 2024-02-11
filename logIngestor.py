# Ingests logs from directory and returns lists with log directories
import os
path = os.getcwd()
folder_name = 'pdrr'
file_path = os.path.join(path, folder_name)

def get_wlogs(): # Returns a list of file paths for White team logs
    wlogs_dir = [] # final list that will be returned with directories of all white team logs
    white_sd_list = [] # contains a list of sub-directories for folders labeled "white"

    # populates list with "white" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'white' in subdirs:
            white_sd_list.append(os.path.join(dirpath, 'white'))

    # compiles a list of file paths for all "white" team log files
    for dir in white_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    wlogs_dir.append(fp)

    return wlogs_dir

def get_blogs(): # Returns a list of file paths for Blue team logs
    blogs_dir = [] # final list that will be returned with directories of all blue team logs
    blue_sd_list = [] # contains a list of sub-directories for folders labeled "blue"

    # populates list with "blue" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'blue' in subdirs:
            blue_sd_list.append(os.path.join(dirpath, 'blue'))

    # compiles a list of file paths for all "white" team log files
    for dir in blue_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    blogs_dir.append(fp)

    return blogs_dir

def get_rlogs(): # Returns a list of file paths for Red team logs
    rlogs_dir = [] # final list that will be returned with directories of all red team logs
    red_sd_list = [] # contains a list of sub-directories for folders labeled "red"

    # populates list with "red" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'red' in subdirs:
            red_sd_list.append(os.path.join(dirpath, 'red'))

    # compiles a list of file paths for all "red" team log files
    for dir in red_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    rlogs_dir.append(fp)

    return rlogs_dir