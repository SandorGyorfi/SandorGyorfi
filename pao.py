file_paths = [
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\views.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\urls.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\tests.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\models.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\apps.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\admin.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\services\\templates\\services\\services.html",
    "C:\\ServerMini\\www.sandorgyorfi.com\\static\\css\\custom.css",
    "C:\\ServerMini\\www.sandorgyorfi.com\\static\\js\\custom.js",
    "C:\\ServerMini\\www.sandorgyorfi.com\\templates\\base.html",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\admin.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\apps.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\models.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\tests.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\urls.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\views.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\home\\templates\\home\\home.html",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\admin.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\apps.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\models.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\tests.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\urls.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\views.py",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\templates\\blog\\blogpost_list.html",
    "C:\\ServerMini\\www.sandorgyorfi.com\\blog\\templates\\blog\\blogpost_detail.html"
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
