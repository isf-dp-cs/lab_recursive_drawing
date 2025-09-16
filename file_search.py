import os

def find_file(folder, target):
    """Recursively locates a specific file inside the specified folder.
    Parameters: 
        folder (string): filepath of the folder to search
        target (string): name of the file to find
    """
    folder = os.path.abspath(folder) # Get the folder's absolute path.

    # Loop over every file and subfolder in the folder:
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        

        # TODO: add the base case
        
        # TODO: add the recursive case


def print_python_files(folder):
    """Recursively prints the names of all python files in a folder.
    Parameter: 
        folder (string): filepath of the folder to search
    """

    folder = os.path.abspath(folder) # Use the folder's absolute path.

    # loop over every file and subfolder in the folder:
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        

        # TODO: add the base case
        
        # TODO: add the recursive case




print('Printing all python files on Desktop...')
desktop_path = os.path.expanduser('~/Desktop') # start at the desktop
print_python_files(desktop_path) # call recursive function
print('----------all done---------\n')


print('Find a filepath by filename...')
desktop_path = os.path.expanduser('~/Desktop') # start at the desktop
find_file(desktop_path, "file_search.py") # call recursive function
print('----------all done---------\n')
