import os

def find_file(folder, target):
    """Recursively locates a specific file inside the specified folder.
    Parameters: 
        folder (string): filepath of the folder to search
        target (string): name of the file to find
    """
    folder = os.path.abspath(folder) # Use the folder's absolute path.

    # Loop over every file and subfolder in the folder:
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        
        # base case (it's a file)
        if os.path.isfile(filepath):
            if target == name.lower():
                print(filepath)
                
        # recusive case (it's a folder)
        elif os.path.isdir(filepath):
            find_file(filepath, target)

def print_python_files(folder):
    """Recursively prints the names of all python files in a folder.
    Parameters: 
        folder (string): filepath of the folder to search
    """

    folder = os.path.abspath(folder) # Use the folder's absolute path.

    # loop over every file and subfolder in the folder:
    for name in os.listdir(folder):
        filepath = os.path.join(folder, name)
        # base case (it's a file)
        if os.path.isfile(filepath):
            # check if it's a python file
            if '.py' in name:
                print(name)
        # recusive case (it's a folder)
        elif os.path.isdir(filepath):
            print_python_files(filepath) # recursive call



print('Print all python files on Desktop')
desktop_path = os.path.expanduser('~/Desktop')
print_python_files(desktop_path)


print('\nFind a filepath by filename')
filename = "file_search.py" # file you're searching for
desktop_path = os.path.expanduser('~/Desktop') # start at the desktop
find_file(desktop_path, filename) # call recursive function