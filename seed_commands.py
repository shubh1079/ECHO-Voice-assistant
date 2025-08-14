import os
import sqlite3
from typing import List, Tuple

DB_PATH = os.path.join(os.path.dirname(__file__), "echo.db")


def expand(path: str) -> str:
    # Expand %USERNAME% and other env vars
    return os.path.expandvars(path)


def insert_if_missing(cursor: sqlite3.Cursor, table: str, name: str, value_col: str, value: str) -> bool:
    cursor.execute(f"SELECT 1 FROM {table} WHERE LOWER(name) = LOWER(?) LIMIT 1", (name,))
    if cursor.fetchone():
        return False
    cursor.execute(f"INSERT INTO {table} (name, {value_col}) VALUES (?, ?)", (name, value))
    return True


def seed_sys_commands(cursor: sqlite3.Cursor) -> Tuple[int, int]:
    username = os.environ.get("USERNAME", "")

    apps: List[Tuple[str, str]] = [
        ("notepad", "notepad.exe"),
        ("calculator", "calc.exe"),
        ("paint", "mspaint.exe"),
        ("wordpad", "wordpad.exe"),
        ("file explorer", "explorer.exe"),
        ("command prompt", r"C:\\Windows\\System32\\cmd.exe"),
        ("powershell", r"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"),
        ("snipping tool", r"C:\\Windows\\System32\\SnippingTool.exe"),
        ("chrome", r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
        ("edge", r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"),
        ("firefox", r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"),
        ("vscode", r"C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"),
        ("teams", r"C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart Teams.exe"),
        ("zoom", r"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"),
        ("spotify", r"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Spotify\\Spotify.exe"),
        ("whatsapp", r"C:\\Users\\%USERNAME%\\AppData\\Local\\WhatsApp\\WhatsApp.exe"),
        ("telegram", r"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"),
        ("discord", r"C:\\Users\\%USERNAME%\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"),
        # Office (may vary by install)
        ("excel", r"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"),
        ("word", r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"),
        ("powerpoint", r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"),
        ("outlook", r"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"),
    ]

    inserted = 0
    skipped = 0
    for name, path in apps:
        path_final = expand(path)
        if insert_if_missing(cursor, "sys_command", name, "path", path_final):
            inserted += 1
        else:
            skipped += 1
    return inserted, skipped


def seed_web_commands(cursor: sqlite3.Cursor) -> Tuple[int, int]:
    sites: List[Tuple[str, str]] = [
        ("google", "https://www.google.com"),
        ("youtube", "https://www.youtube.com"),
        ("gmail", "https://mail.google.com"),
        ("drive", "https://drive.google.com"),
        ("calendar", "https://calendar.google.com"),
        ("maps", "https://maps.google.com"),
        ("whatsapp web", "https://web.whatsapp.com"),
        ("github", "https://github.com"),
        ("stackoverflow", "https://stackoverflow.com"),
        ("linkedin", "https://www.linkedin.com"),
        ("twitter", "https://twitter.com"),
        ("reddit", "https://www.reddit.com"),
        ("netflix", "https://www.netflix.com"),
        ("prime video", "https://www.primevideo.com"),
        ("hotstar", "https://www.hotstar.com"),
        ("canva", "https://www.canva.com"),
        ("speedtest", "https://www.speedtest.net"),
        ("chatgpt", "https://chat.openai.com"),
    ]

    inserted = 0
    skipped = 0
    for name, url in sites:
        if insert_if_missing(cursor, "web_command", name, "url", url):
            inserted += 1
        else:
            skipped += 1
    return inserted, skipped


def main() -> None:
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # Ensure tables exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sys_command(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            path VARCHAR(1000)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS web_command(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            url VARCHAR(1000)
        )
    """)

    sys_ins, sys_skip = seed_sys_commands(cur)
    web_ins, web_skip = seed_web_commands(cur)

    con.commit()
    con.close()

    print(f"sys_command: inserted={sys_ins}, skipped={sys_skip}")
    print(f"web_command: inserted={web_ins}, skipped={web_skip}")
    print("Done.")


if __name__ == "__main__":
    main()
