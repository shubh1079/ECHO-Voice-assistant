# ECHO Voice-Controlled Personal Assistant

A powerful voice-controlled personal assistant built with Python, featuring speech recognition, text-to-speech, and a modern web interface.

## Features

- 🎤 **Voice Recognition**: Listen and respond to voice commands
- 🔊 **Text-to-Speech**: Natural voice responses
- 🔥 **Hotword Detection**: Activate with "Jarvis", "Alexa", or "Echo"
- 🌐 **Web Interface**: Modern UI built with HTML/CSS/JavaScript
- 📱 **WhatsApp Integration**: Send messages, make calls via WhatsApp
- 🎵 **YouTube Search**: Search and play YouTube videos
- 🤖 **AI Chatbot**: Powered by HugChat for intelligent conversations
- 🖥️ **Application Control**: Open applications and websites
- 📞 **Contact Management**: Store and manage contacts

## Screenshots

![Screenshot 2024-04-22 222911](https://github.com/dakshvarshneyy/ECHO-Voice-Controlled-Personal-Assistant/assets/107689714/5a08fd59-b439-4224-bbe4-dcfed249f458)
![Screenshot 2024-04-22 223313](https://github.com/dakshvarshneyy/ECHO-Voice-Controlled-Personal-Assistant/assets/107689714/46e3ae38-d71f-4160-a93d-ea2494e8fd8f)
![Screenshot 2024-04-22 223242](https://github.com/dakshvarshneyy/ECHO-Voice-Controlled-Personal-Assistant/assets/107689714/2ddabd50-5d90-4dcc-8579-771926878b13)

## System Requirements

- **OS**: Windows 10/11 (recommended)
- **Python**: 3.7 or higher
- **Microphone**: Required for voice input
- **Speakers**: Required for voice output
- **Internet**: Required for speech recognition and AI features

## Quick Setup

### Option 1: Automatic Setup (Recommended)

1. **Clone or download** this repository
2. **Navigate** to the project directory:
   ```bash
   cd ECHO-Voice-Controlled-Personal-Assistant
   ```
3. **Run the setup script**:
   ```bash
   python setup_and_run.py
   ```
4. **Follow the prompts** to install dependencies and setup the database
5. **Start ECHO** when prompted

### Option 2: Manual Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup the database**:
   ```bash
   python setup_database.py
   ```

3. **Configure HugChat** (optional):
   - Get a Hugging Face token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Update `engine/cookies.json` with your token

4. **Run the application**:
   ```bash
   python run.py
   ```

## Usage

### Voice Commands

Once ECHO is running, you can use these voice commands:

#### Basic Commands
- **"Open [application]"** - Opens applications (e.g., "Open notepad")
- **"Open [website]"** - Opens websites (e.g., "Open google")
- **"Play [video] on YouTube"** - Searches and plays YouTube videos

#### WhatsApp Commands
- **"Send message to [contact]"** - Sends WhatsApp message
- **"Call [contact]"** - Makes WhatsApp call
- **"Video call [contact]"** - Starts WhatsApp video call

#### AI Chat
- **Ask any question** - ECHO will respond using AI

### Activation

ECHO listens for these wake words:
- "Jarvis"
- "Alexa" 
- "Echo"

### Keyboard Shortcut

You can also press **Win + J** to activate ECHO manually.

## Project Structure

```
ECHO-Voice-Controlled-Personal-Assistant/
├── engine/                 # Core functionality
│   ├── command.py         # Voice commands and speech
│   ├── features.py        # Main features (WhatsApp, YouTube, etc.)
│   ├── db.py             # Database operations
│   ├── config.py         # Configuration
│   ├── helper.py         # Helper functions
│   └── cookies.json      # HugChat authentication
├── www/                   # Web interface
│   ├── index.html        # Main interface
│   ├── style.css         # Styling
│   ├── script.js         # JavaScript functionality
│   └── assets/           # Images, audio, etc.
├── main.py               # Main application entry
├── run.py                # Multi-process runner
├── setup_database.py     # Database initialization
├── setup_and_run.py      # Complete setup script
├── requirements.txt      # Python dependencies
└── echo.db              # SQLite database (created automatically)
```

## Troubleshooting

### Common Issues

1. **"No module named 'pyaudio'"**
   - Install Visual C++ Build Tools
   - Or use: `pip install pipwin && pipwin install pyaudio`

2. **Microphone not working**
   - Check microphone permissions in Windows settings
   - Ensure microphone is set as default input device

3. **Speech recognition errors**
   - Check internet connection
   - Ensure microphone is working properly

4. **HugChat not working**
   - Verify your Hugging Face token in `engine/cookies.json`
   - Check if the token has proper permissions

### Audio Issues

- **No sound output**: Check speaker settings and volume
- **Poor voice recognition**: Use a good quality microphone in a quiet environment
- **Echo feedback**: Use headphones to prevent feedback loops

## Customization

### Adding Applications

Edit the database to add more applications:
```sql
INSERT INTO sys_command (name, path) VALUES ('your_app', 'path_to_executable');
```

### Adding Websites

Add more websites:
```sql
INSERT INTO web_command (name, url) VALUES ('your_site', 'https://yoursite.com');
```

### Adding Contacts

Add contacts for WhatsApp integration:
```sql
INSERT INTO contacts (name, mobile_no, email) VALUES ('Name', 'phone_number', 'email');
```

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues, please:
1. Check the troubleshooting section
2. Ensure all dependencies are installed
3. Verify your system meets the requirements
4. Check the console output for error messages

---

**Enjoy using ECHO!** 🎉
