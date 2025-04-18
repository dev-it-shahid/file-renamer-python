import os

def rename_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    for count, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]
        new_name = f"file_{count}{file_ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f'Renamed: {filename} ➜ {new_name}')


folder_path = r"D:\Projects\Freelance\Projects\file-renamer\demo"
rename_files_in_folder(folder_path)
