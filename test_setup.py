import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import eel
        print("✓ Eel imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import eel: {e}")
        return False
    
    try:
        import pyttsx3
        print("✓ pyttsx3 imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pyttsx3: {e}")
        return False
    
    try:
        import speech_recognition as sr
        print("✓ SpeechRecognition imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import SpeechRecognition: {e}")
        return False
    
    try:
        import playsound
        print("✓ playsound imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import playsound: {e}")
        return False
    
    try:
        import pyautogui
        print("✓ pyautogui imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pyautogui: {e}")
        return False
    
    try:
        import pywhatkit
        print("✓ pywhatkit imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pywhatkit: {e}")
        return False
    
    try:
        import pvporcupine
        print("✓ pvporcupine imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pvporcupine: {e}")
        return False
    
    try:
        import pyaudio
        print("✓ pyaudio imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pyaudio: {e}")
        return False
    
    try:
        import hugchat
        print("✓ hugchat imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import hugchat: {e}")
        return False
    
    return True

def test_database():
    """Test database connection and tables"""
    print("\nTesting database...")
    
    try:
        import sqlite3
        con = sqlite3.connect("echo.db")
        cursor = con.cursor()
        
        # Test tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        required_tables = ['sys_command', 'web_command', 'contacts']
        for table in required_tables:
            if table in tables:
                print(f"✓ Table '{table}' exists")
            else:
                print(f"✗ Table '{table}' missing")
                return False
        
        # Test data exists
        cursor.execute("SELECT COUNT(*) FROM sys_command")
        sys_count = cursor.fetchone()[0]
        print(f"✓ sys_command has {sys_count} entries")
        
        cursor.execute("SELECT COUNT(*) FROM web_command")
        web_count = cursor.fetchone()[0]
        print(f"✓ web_command has {web_count} entries")
        
        cursor.execute("SELECT COUNT(*) FROM contacts")
        contact_count = cursor.fetchone()[0]
        print(f"✓ contacts has {contact_count} entries")
        
        con.close()
        return True
        
    except Exception as e:
        print(f"✗ Database test failed: {e}")
        return False

def test_audio():
    """Test audio functionality"""
    print("\nTesting audio...")
    
    try:
        import pyaudio
        p = pyaudio.PyAudio()
        device_count = p.get_device_count()
        p.terminate()
        
        if device_count > 0:
            print(f"✓ Found {device_count} audio devices")
            return True
        else:
            print("✗ No audio devices found")
            return False
            
    except Exception as e:
        print(f"✗ Audio test failed: {e}")
        return False

def test_files():
    """Test if required files exist"""
    print("\nTesting files...")
    
    required_files = [
        "www/index.html",
        "www/style.css", 
        "www/script.js",
        "www/assets/audio/start_sound.mp3",
        "engine/config.py",
        "engine/helper.py"
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("ECHO Voice Assistant - Setup Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_database,
        test_audio,
        test_files
    ]
    
    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! ECHO is ready to run.")
        print("\nTo start ECHO, run: python run.py")
    else:
        print("❌ Some tests failed. Please check the issues above.")
        print("\nYou may need to:")
        print("1. Install missing dependencies")
        print("2. Setup the database: python setup_database.py")
        print("3. Check audio device settings")
    
    return all_passed

if __name__ == "__main__":
    main()
