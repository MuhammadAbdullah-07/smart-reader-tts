import streamlit as st
from tts_engine import text_to_speech, VOICES   ## awaaz banane wala function aur voices ki dictionary.

st.set_page_config(page_title="Smart Reader",page_icon="🔊")
st.title("🔊 Smart Reader")
st.caption("Type or paste text and listen to it.")

## Side blocks
with st.sidebar:
    st.header("Settings")
    language=st.selectbox("Languages",list(VOICES.keys())) ## Shows list of languages
    voice_name=st.selectbox("Voice",list(VOICES[language].keys())) ## Shows selected language
    voice = VOICES[language][voice_name]
    speed=st.slider("Speed (%)",-50,50,0, step=10)

## Main Content
text=st.text_area("Text",height=250)  ## text box for user to give sentences

## Button

if st.button("Generate Speech",type="primary"):
    if not text.strip():  ## strip-- uses to removes extra spaces
        st.warning("Please enter some text first")
    else:
        with st.spinner("Generating Speech..."):  ## for user interaction
            try:
                path=text_to_speech(text,voice=voice,speed=speed)
                with open(path,"rb") as f:
                    st.session_state["audio"]=f.read()  ## reading the file
                st.success("Speech Generated !")  ## shows success msg
            except Exception as e:
                st.error(f"Something went wrong : {e}")  ## error handling

if "audio" in st.session_state:
    st.audio(st.session_state["audio"],format="audio/mp3") ## shows browser player
    st.download_button("Download MP3",st.session_state["audio"], ## button data , button data , filename and file format
                       file_name="audio.mp3",mime="audio/mpeg")

