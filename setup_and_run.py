import os
import sys
import subprocess
import platform

def install_dependencies():
    """Install required Python packages"""
    print("Installing required dependencies...")
    
    # Check if pip is available
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("Error: pip is not available. Please install pip first.")
        return False
    
    # Install packages from requirements.txt
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def setup_database():
    """Setup the database"""
    print("Setting up database...")
    try:
        from setup_database import setup_database
        setup_database()
        return True
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False

def check_system_requirements():
    """Check if system meets requirements"""
    print("Checking system requirements...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required.")
        return False
    
    # Check if running on Windows
    if platform.system() != "Windows":
        print("Warning: This application is designed for Windows. Some features may not work on other platforms.")
    
    # Check for microphone
    try:
        import pyaudio
        p = pyaudio.PyAudio()
        device_count = p.get_device_count()
        p.terminate()
        if device_count == 0:
            print("Warning: No audio devices found. Voice features may not work.")
    except:
        print("Warning: Could not check audio devices.")
    
    return True

def run_application():
    """Run the ECHO voice assistant"""
    print("Starting ECHO Voice Assistant...")
    try:
        from run import startJarvis, listenHotword
        import multiprocessing
        
        # Start both processes
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        
        p1.start()
        p2.start()
        
        print("ECHO is now running!")
        print("Say 'Jarvis', 'Alexa', or 'Echo' to activate voice commands.")
        print("Press Ctrl+C to stop the application.")
        
        p1.join()
        
        if p2.is_alive():
            p2.terminate()
            p2.join()
            
        print("ECHO stopped.")
        
    except KeyboardInterrupt:
        print("\nStopping ECHO...")
    except Exception as e:
        print(f"Error running application: {e}")

def main():
    """Main setup and run function"""
    print("ECHO Voice-Controlled Personal Assistant Setup")
    print("=" * 50)
    
    # Check system requirements
    if not check_system_requirements():
        return
    
    # Install dependencies
    if not install_dependencies():
        print("Failed to install dependencies. Please check your internet connection and try again.")
        return
    
    # Setup database
    if not setup_database():
        print("Failed to setup database.")
        return
    
    print("\nSetup completed successfully!")
    print("\nNote: For HugChat functionality, you need to:")
    print("1. Get a Hugging Face token from https://huggingface.co/settings/tokens")
    print("2. Update the 'hf_token' value in engine/cookies.json")
    print("3. Restart the application")
    
    # Ask user if they want to run the application
    response = input("\nDo you want to run ECHO now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        run_application()
    else:
        print("You can run ECHO later by executing: python run.py")

if __name__ == "__main__":
    main()
