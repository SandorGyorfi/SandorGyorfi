import subprocess

file_paths = [
    "C:/ServerMini/www.sandorgyorfi.com/paohome.py",
    "C:/ServerMini/www.sandorgyorfi.com/paoblog.py",
    "C:/ServerMini/www.sandorgyorfi.com/paoservices.py"
]

for path in file_paths:
    try:
        result = subprocess.run(['python', path], capture_output=True, text=True)
        print(f"\n\n{'='*10} START OF {path} {'='*10}\n\n")
        print(result.stdout)
        print(f"\n\n{'='*10} END OF {path} {'='*10}\n\n")
    except Exception as e:
        print(f"Failed to run {path}: {e}")