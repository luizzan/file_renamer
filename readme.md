# Rename files in folders and subfolders

This is a script I have created mainly to help me rename photos in folders.

Copy the file_renamer.py file into the folder in which the files are stored.<br>
Run in the terminal using

```python3 file_renamer.py```

If run in default mode (as above), it will rename the files as `PREFIX_NUMBER.EXT`.<br>
`NUMBER` will start at zero and increment by one for each file. To change `PREFIX` or the starting `NUMBER`, run the script using

```python3 file_renamer.py config```

It will ask for `PREFIX` than the starting `NUMBER`. Any of those can be skipped.

## Subfolders

If there are any subfolders containing files the script will rename the files as `PREFIX_SUBFOLDER_NUMBER.EXT` then move the files to the main folder and delete the subfolders.<br>
(This last "feature" is here because I needed to rename my photos in subfolders to upload to Google Photos)