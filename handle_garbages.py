import os
import shutil

folder_path = "your_folder_path"  # Enter the path to the "saved" folder here
shift_folder_path = "your_shift_folder_path"  # Enter the path to the "garbages" folder here

# Check for unnecessary .txt and .json files and delete them
for file in os.listdir(folder_path):
    if file.endswith(".txt") or file.endswith(".json"):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)
        print(f"{file} is successfully deleted.")

# This section creates the "garbages" folder if you have not created it before
if not os.path.exists(shift_folder_path):
    os.makedirs(shift_folder_path)

jpg_files = set()
mp4_files = set()

# Collecting .jpg and .mp4 files in the saved folder
for file in os.listdir(folder_path):
    if file.endswith(".jpg"):
        jpg_files.add(file.split(".jpg")[0])  # We remove the .jpg extension and add only the file name
    elif file.endswith(".mp4"):
        mp4_files.add(file.split(".mp4")[0])  # We remove the .mp4 extension and add only the file name

# Check for .jpg and .mp4 files with the same name and move .jpg files to the "garbages" folder
for file in jpg_files.intersection(mp4_files):
    jpg_file_path = os.path.join(folder_path, file + ".jpg")
    if os.path.exists(jpg_file_path):
        target_path = os.path.join(shift_folder_path, file + ".jpg")
        shutil.move(jpg_file_path, target_path)
        print(f"{file}.jpg moved to {shift_folder_path} folder.")



# If you want to delete the files directly instead of moving them to another folder, you can run this instead of the code above. 
# (I still recommend running the code above first, just in case there are photos you might need)
'''
# Check for .jpg and .mp4 files with the same name and delete .jpg files
for file in jpg_files.intersection(mp4_files):
    jpg_file_path = os.path.join(folder_path, file + ".jpg")
    if os.path.exists(jpg_file_path):
        os.remove(jpg_file_path)
        print(f"{file}.jpg deleted.")
'''