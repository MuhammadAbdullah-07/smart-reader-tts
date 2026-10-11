import os
import asyncio
import edge_tts

VOICES={
    "English":{
        "Aria (female)":"en-US-AriaNeural",
        "Guy (Male)":"en-US-GuyNeural"
    },
    "Urdu":{
        "Uzma  (female)":"ur-PK-UzmaNeural",
        "Asad (Male)":"ur-PK-AsadNeural"
    },
    "Arabic":{
        "Zariyah  (female)":"ar-SA-ZariyahNeural",
        "Hamed  (Male)":"ar-SA-Hamed Neural"
    },        
}

async def _generate(text,voice,rate,output_path):
    communicate=edge_tts.Communicate(text,voice,rate=rate)
    await communicate.save(output_path)

def text_to_speech(text, voice, speed=0, output_path="outputs/audio.mp3"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rate = f"{int(speed):+d}%"
    asyncio.run(_generate(text,voice,rate,output_path))
    return output_path

if __name__ == "__main__":
    path = text_to_speech("السلام علیکم! یہ میرا پہلا پروجیکٹ ہے۔",
                          voice="ur-PK-UzmaNeural")
    print("Audio created:", path)    