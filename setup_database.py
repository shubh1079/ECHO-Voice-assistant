import sqlite3
import os

def setup_database():
    """Setup the SQLite database with necessary tables and sample data"""
    
    # Create database connection
    con = sqlite3.connect("echo.db")
    cursor = con.cursor()
    
    # Create system commands table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sys_command(
            id INTEGER PRIMARY KEY, 
            name VARCHAR(100), 
            path VARCHAR(1000)
        )
    """)
    
    # Create web commands table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS web_command(
            id INTEGER PRIMARY KEY, 
            name VARCHAR(100), 
            url VARCHAR(1000)
        )
    """)
    
    # Create contacts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY, 
            name VARCHAR(200), 
            mobile_no VARCHAR(255), 
            email VARCHAR(255)
        )
    """)
    
    # Insert sample system commands
    sample_sys_commands = [
        ('notepad', 'notepad.exe'),
        ('calculator', 'calc.exe'),
        ('paint', 'mspaint.exe'),
        ('wordpad', 'wordpad.exe'),
        ('chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),
        ('firefox', 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'),
    ]
    
    for name, path in sample_sys_commands:
        cursor.execute("INSERT OR IGNORE INTO sys_command (name, path) VALUES (?, ?)", (name, path))
    
    # Insert sample web commands
    sample_web_commands = [
        ('google', 'https://www.google.com'),
        ('youtube', 'https://www.youtube.com'),
        ('facebook', 'https://www.facebook.com'),
        ('instagram', 'https://www.instagram.com'),
        ('twitter', 'https://twitter.com'),
        ('linkedin', 'https://www.linkedin.com'),
        ('github', 'https://github.com'),
        ('stackoverflow', 'https://stackoverflow.com'),
    ]
    
    for name, url in sample_web_commands:
        cursor.execute("INSERT OR IGNORE INTO web_command (name, url) VALUES (?, ?)", (name, url))
    
    # Insert sample contacts
    sample_contacts = [
        ('John Doe', '9876543210', 'john@example.com'),
        ('Jane Smith', '9876543211', 'jane@example.com'),
        ('Bob Johnson', '9876543212', 'bob@example.com'),
    ]
    
    for name, mobile, email in sample_contacts:
        cursor.execute("INSERT OR IGNORE INTO contacts (name, mobile_no, email) VALUES (?, ?, ?)", (name, mobile, email))
    
    # Commit changes and close connection
    con.commit()
    con.close()
    
    print("Database setup completed successfully!")
    print("Created tables: sys_command, web_command, contacts")
    print("Added sample data for testing")

if __name__ == "__main__":
    setup_database()
