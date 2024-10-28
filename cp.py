import subprocess

def copy_file(source_path, destination_path):
    try:
        # Use subprocess to run the cp command
        subprocess.run(['cp', source_path, destination_path], check=True)
        print(f"File copied from {source_path} to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error copying file: {e}")

# Example usage
source_file = '/path/to/source/file.txt'
destination_file = '/path/to/destination/file.txt'
copy_file(source_file, destination_file)