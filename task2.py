2. Automated Backup Solution:


import shutil
import os
import datetime

def backup_directory(source_dir, dest_dir):
    try:
        # Create a timestamp for the backup folder
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_dir = os.path.join(dest_dir, f'backup_{timestamp}')
        os.makedirs(backup_dir)

        # Copy the contents of the source directory to the backup directory
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, backup_dir)
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, os.path.join(backup_dir, item))

        print("Backup successful!")
    except Exception as e:
        print("Backup failed:", e)

if __name__ == "__main__":
    # Specify source and destination directories
    source_directory = "/path/to/source"
    destination_directory = "/path/to/backup"

    # Perform backup
    backup_directory(source_directory, destination_directory)

