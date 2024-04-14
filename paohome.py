file_paths = [
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\admin.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\apps.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\models.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\views.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\urls.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\templates\home\home.html"
]

def print_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            header = f"\n\n{'='*10} START OF {file_path} {'='*10}\n\n"
            footer = f"\n\n{'='*10} END OF {file_path} {'='*10}\n\n"
            content = file.read()
            
            print(header)
            print(content)
            print(footer)
            
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")

for path in file_paths:
    print_file_content(path)