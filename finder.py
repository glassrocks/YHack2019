""" Module for finding new images in a folder """
import os
from time import sleep

def image_finder(directory, file_list=[]):
    """ Finds new files in a directory,
        returns a tuple: (found_files[], file_list[]) """

    # Get files currently in the directory
    cur_files = os.listdir(directory)

    # Remove desktop.ini from file list
    if "desktop.ini" in cur_files:
        cur_files.remove("desktop.ini")

    # If the file list is empty,
    if not file_list:
        # Return no files found and the current file list
        return (None, cur_files)

    # If the file list isn't empty
    new_files = []
    # Loop through each file in current file list
    for file in cur_files:
        # If the file isn't in the file list
        if file not in file_list:
            # Add it to the new files list
            new_files.append(file)

    '''# If new files list is empty
    if not new_files:
        # Return no new files found and the current file list
        return (None, cur_files)'''

    # If there is new files, return them and the current files list
    return (new_files, cur_files)



'''if __name__ == "__main__":
    current_files = []
    new_files = []
    while(True):
        new_files, current_files = image_finder(
            file_list=current_files)
        if new_files:
            print("{0}".format(new_files))
        #print("{0}".format(current_files))
        sleep(5)'''

# not used with integration with main.py
if __name__ == "__main__":
    current_files = []
    new_files = []
    image_folder = os.getcwd() + "/images"
    while(True):
        new_files, current_files = image_finder(
            directory=image_folder,
            file_list=current_files)
        if new_files:
            print("{0}".format(new_files))
        #print("{0}".format(current_files))
        sleep(5)