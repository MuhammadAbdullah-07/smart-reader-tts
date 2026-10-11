 # Smart Reader (Text-to-Speech App)

A web app that converts text into natural-sounding speech in Urdu, English and Arabic.

**Live demo:** https://YOUR-APP-LINK.streamlit.app

## Features
- Multiple languages and voices (male and female)
- Adjustable speech speed
- Audio player and MP3 download
- Input validation and error handling

## Tech Stack
- Python
- Streamlit (UI)
- edge-tts (neural text-to-speech)
- asyncio (async audio generation)

## Project Structure
- `app.py`: Streamlit user interface
- `tts_engine.py`: text-to-speech logic and voice list
- `requirements.txt`: dependencies

## Run Locally
    pip install -r requirements.txt
    streamlit run app.py