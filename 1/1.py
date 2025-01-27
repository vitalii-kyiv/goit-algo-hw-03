from utils import file_generator
from pathlib import Path
import sys
import os
import shutil

os.makedirs('dist', exist_ok=True)
dist = Path('dist')

def files_copy_by_extension(source_path, destination_path=dist):
    for element in source_path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            files_copy_by_extension(element, destination_path)  
        elif element.is_file():
            file_extension = element.suffix.lower()
            extension_folder = Path(destination_path) / file_extension[1:]  
            extension_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(element), str(extension_folder / element.name))
            print(f"Moved file: {element.name} to folder: {extension_folder}")

def delete_source_folder(path):
    
    if path.exists() and path.is_dir():
        shutil.rmtree(path)  
        print(f"Removed folder: {path}")

def main():
    if len(sys.argv) < 2:
        print("You should enter path to source directory")
        sys.exit(1)
    source_path = Path(sys.argv[1])

    if not source_path.exists():
        print("There is no such path")
        sys.exit(1)

    if not source_path.is_dir():
        print(f"{source_path} is not directory")
        sys.exit(1)

    if not os.listdir(source_path):
        file_generator(source_path)

    files_copy_by_extension(source_path)

    delete_source_folder(source_path)

if __name__ == "__main__":
    main()
