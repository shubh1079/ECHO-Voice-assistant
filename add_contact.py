import os
import sqlite3
import argparse
from typing import Optional

DB_PATH = os.path.join(os.path.dirname(__file__), "echo.db")


def ensure_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name VARCHAR(200),
            mobile_no VARCHAR(255),
            email VARCHAR(255)
        )
        """
    )


def contact_exists(conn: sqlite3.Connection, name: str, mobile_no: str) -> bool:
    cur = conn.execute(
        "SELECT 1 FROM contacts WHERE LOWER(name)=LOWER(?) OR mobile_no=? LIMIT 1",
        (name.strip(), mobile_no.strip()),
    )
    return cur.fetchone() is not None


def add_contact(conn: sqlite3.Connection, name: str, mobile_no: str, email: Optional[str]) -> bool:
    name = name.strip()
    mobile_no = mobile_no.strip()
    email = (email or "").strip() or None

    if not name or not mobile_no:
        raise ValueError("Name and mobile number are required")

    if contact_exists(conn, name, mobile_no):
        print("Contact already exists (by name or number). Skipping.")
        return False

    conn.execute(
        "INSERT INTO contacts (name, mobile_no, email) VALUES (?, ?, ?)",
        (name, mobile_no, email),
    )
    conn.commit()
    print(f"Added contact: {name} ({mobile_no})" + (f" <{email}>" if email else ""))
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Add a contact to echo.db")
    parser.add_argument("--name", help="Contact name")
    parser.add_argument("--mobile", help="Mobile number (e.g., 9876543210)")
    parser.add_argument("--email", help="Email address", default=None)
    args = parser.parse_args()

    name = args.name
    mobile = args.mobile
    email = args.email

    # Interactive fallback
    if not name:
        name = input("Name: ").strip()
    if not mobile:
        mobile = input("Mobile (10-digit for India): ").strip()
    if email is None:
        email = input("Email (optional, leave blank): ").strip() or None

    with sqlite3.connect(DB_PATH) as conn:
        ensure_table(conn)
        add_contact(conn, name, mobile, email)


if __name__ == "__main__":
    main()
