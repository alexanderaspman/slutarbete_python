import shutil
import os

def copy_file(source_path, destination_path):
    # Check if the source file exists
    if not os.path.exists(source_path):
        print(f"Source file does not exist: {source_path}")
        return

    try:
        # Use shutil to copy the file
        shutil.copy(source_path, destination_path)
        print(f"File copied from {source_path} to {destination_path}")
    except FileNotFoundError as e:
        print(f"Error copying file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
source_file = 'c:/path/to/source/file.txt'
destination_file = 'c:/path/to/destination/file.txt'

copy_file(source_file, destination_file)
