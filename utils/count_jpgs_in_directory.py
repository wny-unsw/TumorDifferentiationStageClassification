import os

def count_jpgs_in_directory(directory):
    jpg_count = 0

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a .jpg file
            if file.lower().endswith('.jpg'):
                jpg_count += 1
    
    return jpg_count

# Replace 'your_directory_path' with the path to the directory you want to search

print(count_jpgs_in_directory('./ColHis-IDS'))
print(count_jpgs_in_directory('./ColHis-IDS_restructured'))