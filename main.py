import streamlit as st
import speech_recognition as sr

def transcribe_speech(r, source, language):
    st.write("Listening...")
    audio = r.listen(source)

    try:
        st.write("Processing...")
        text = r.recognize_google(audio, language=language)
        st.write("Transcription:", text)
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        st.error("Error during transcription. Please try again later.")
        st.error(f"Details: {e}")
    return None

def main():
    st.title("Speech Recognition App")

    r = sr.Recognizer()

    # Language selection
    supported_languages = ["en-US", "es-ES", "fr-FR"]
    language_selection = st.selectbox("Select the language you're speaking in:", supported_languages)

    st.markdown(
        """
        <style>
        .stButton > button {
            width: 100%;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Click the 'Start Recording' button and speak something:")
    recording = False
    text = ""

    if st.button("Start Recording"):
        recording = True

    if recording:
        with sr.Microphone() as source:
            text = transcribe_speech(r, source, language_selection)

    # Pause and resume functionality
    if recording:
        if st.button("Pause Recording"):
            recording = False

    if not recording and text:
        if st.button("Resume Recording"):
            recording = True

    # Save transcription to file
    if text and st.button("Save Transcription"):
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(text)
        st.write("Transcription saved to 'transcription.txt'.")
if __name__ == "__main__":
    main()
