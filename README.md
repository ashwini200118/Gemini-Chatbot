# Gemini Chatbot

A simple command-line chatbot powered by Google's Gemini AI.

## Prerequisites

- Python 3.7 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Gemini-Chatbot.git
   cd Gemini-Chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install google-generativeai python-dotenv
   ```

4. Create a `.env` file in the root directory and add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot:
```
python gemini_service.py
```

Type your messages and press Enter. Type 'exit' to quit.

## Features

- Interactive chat with Gemini AI
- Simple command-line interface
- Error handling for API issues

## License

This project is open source. Feel free to use and modify.