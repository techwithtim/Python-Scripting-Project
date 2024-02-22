# importing a bunch of modules for what we're going to use
import os
import json
import shutil
from subprocess import PIPE, run
import sys

'''
Info on the imported modules:

os - operating system
json - how we're going to work with json files
shutil - using copy/overwrite operations
subprocess/PIPE , subprocess/run - allows up to run any terminal command that we want
    which we can use to compile and run the GO code 
sys - allows us access to the command line arguments
'''

'''We'll be passing arguments for our final project result
python get_game_data.py /data /games_folder
'/data' will be our source directory argument
'/games_folder' will be our dest directory argument

'''
#We create this constant variable to specify the key we're
# looking for when searching directories containing games
GAME_DIR_PATTERN = "game"

def find_all_game_paths(source):
    game_paths = []

    # os.walk(), recursively looks through root directory, directories, and files
    # checkout https://docs.python.org/3/library/os.html for more info
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        # We only need this to loop once, so we include a break
        break
    return game_paths

def get_name_from_paths(paths, to_strip):
    new_names = []

    # os.path.split within this for loop will return both 
    # the before path and the path we want.
    # Since we don't care about the before path, we just use an _ here
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def clean_up(path):
    if os.path.exists(path):
        os.rmdir(path)

def main(source, dest):
    # Using the os module to get a pwd, then we join it 
    # with the destination directory
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    dest_path = os.path.join(cwd, dest)

    game_paths = find_all_game_paths(source_path)
    #print(game_paths)
    new_game_dirs = get_name_from_paths(game_paths, "_game")
    #new_game_dirs = get_name_from_paths(game_paths, GAME_DIR_PATTERN)
    print("Game directories: ", new_game_dirs)

    create_dir(dest_path)

def copy_and_overwrite(source, dest):
    

# Only want to execute the main script, if we're running this python file directly
# The following line checks if we ran the file directly
# Otherwise, Everything will be run, even if we did not want it to
if __name__ == "__main__":
    args = sys.argv
    print("arguments: ", args)

    #Make sure we have a valid amount of arguments
    if len(args) != 3:
        raise Exception('You only need to pass a source and destination directory as arguments')
    
    #Save the arguments
    source, dest = args[1:]
    clean_up(args[2])
    main(source, dest)


    

