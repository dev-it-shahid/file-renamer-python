# 🗂️ File Renamer Script

This is a simple Python automation script that renames all files in a folder to a consistent format like:
file_1.txt, file_2.txt, file_3.txt, ...


## 📌 Features

- Automatically renames all files in a given folder
- Keeps original file extensions
- Renames files using a numbered format (`file_1.ext`, `file_2.ext`, etc.)
- Prevents accidental renaming of directories

---

## 🚀 How It Works

1. List all files in the folder
2. Ignore subdirectories
3. Rename each file in order using a loop

---

## 📂 Example

### 🔸 Before:
hello.txt notes.pdf img.png

### 🔸 After running the script:
file_1.txt notes.pdf file_2.png

---

## 🤔
## Run the script
``` python 
python file_renamer.py
```


🧑‍💻 Tech Used
Python 3

Built-in os module

📎 Notes
This script modifies file names, so make sure to use it on test folders first.

You can customize the prefix by editing the line:

```python
new_name = f"file_{count}{file_ext}"
```

✅ Author
Name: Shahid Laskar

GitHub: https://github.com/dev-it-shahid

