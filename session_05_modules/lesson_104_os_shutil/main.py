
import os
import shutil

original_path = '/mnt/sdb1/Annotations'
new_path = '/mnt/sdb1/Annotations2'

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f'Path {new_path} already exist')

for root, directories, files in os.walk(original_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)

        # shutil.move(old_file_path, new_file_path)
        # print(f'File {file} moved with sucess')
        os.remove(old_file_path)
        print(f'Files in {old_file_path} removed')
