import os
import time
import string
from sys import argv

def main(file_prefix='', start_number=0):

    """
    Renames the files in the current folder and the files in the subfolders (one level).
    Start number is used only on the main folder.
    Copies the files in the subfolders to the current folder.
    Deletes the subfolders.
    """

    initial_file_count = 0

    if file_prefix == '':
        file_prefix = os.path.split(os.getcwd())[1]

    # Rename files in the main folder
    main_folder = os.getcwd()
    initial_file_count += _rename_files(main_folder, file_prefix, start_number)

    # Rename files in the subfolders
    subfolders = sorted([s for s in os.listdir() if os.path.isdir(s) and not s.startswith('.')])
    for subfolder in subfolders:
        subfolder_file_prefix = file_prefix + '_' + subfolder
        subfolder_path = os.path.join(os.getcwd(), subfolder)
        initial_file_count += _rename_files(subfolder_path, subfolder_file_prefix)
        os.rmdir(subfolder)

    final_files = [f for f in os.listdir() if os.path.isfile(f) and not f.startswith('.') and f != argv[0]]
    final_file_count = len(final_files)

    print('\nInitial file count:', initial_file_count)
    print('Final file count:', final_file_count)


def _rename_files(folder_path, file_prefix, start_number=0):

    if start_number > 0:
        start_number -= 1  # Start at the correct number (and > 0)

    folder_name = os.path.split(folder_path)[1]

    # Initial state
    file_list = []
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path) and not f.startswith('.') and f != argv[0]:
            file_list.append(file_path)
    initial_count = len(file_list)
    print('Renaming {} files in {}.'.format(initial_count, folder_name))

    # Rename files
    suffix = start_number
    for f in file_list:
        extension = os.path.splitext(f)[1]

        suffix += 1
        new_file_name = file_prefix + '_' + str(suffix).zfill(4) + extension
        os.rename(f, new_file_name)
        time.sleep(0.1)

    return initial_count


if __name__ == '__main__':

    """
    On the terminal run
    $ python file_renamer.py
    to use the standard configs or
    $ python file_renamer.py config
    to select a file prefix and start number
    """

    file_prefix, start_number = '', 0

    if len(argv) > 1:
        assert argv[1] == 'config', "Use 'config' to customize the parameters."

        file_prefix = input('File prefix: (Enter to use folder name)\n') or file_prefix
        
        start_number = input('Start number: (Enter to use 0)\n') or str(start_number)
        error_msg = 'Start number must be a positive integer.'
        assert start_number.isdigit(), error_msg
        start_number = int(start_number)

    main(file_prefix, start_number)
