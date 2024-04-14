import sqlite3

file_paths = [
    "C:\\ServerMini\\www.sandorgyorfi.com\\db.sqlite3"
]

def print_tables(file_path):
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table_name in tables:
            print(f"\n\n{'='*10} START OF {table_name[0]} {'='*10}\n\n")
            cursor.execute(f"SELECT * FROM {table_name[0]};")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print(f"\n\n{'='*10} END OF {table_name[0]} {'='*10}\n\n")

        conn.close()
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")

for path in file_paths:
    print_tables(path)