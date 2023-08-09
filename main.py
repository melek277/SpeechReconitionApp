import streamlit as st
import speech_recognition as sr
import tempfile
import os

def main():
    st.title("Speech Recognition and Audio Recording")

    recognizer = sr.Recognizer()

    recording = st.button("Start Recording")

    if recording:
        st.write("Recording... Please speak into your microphone.")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        st.write("Recording finished!")

        # Save the recorded audio to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
            temp_audio.write(audio.get_wav_data())
            temp_audio_path = temp_audio.name

        # Display the recorded audio using st.audio
        st.audio(temp_audio_path, format="audio/wav")

        try:
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
        except sr.UnknownValueError:
            st.warning("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Error with the request; {e}")

        # Remove the temporary audio file
        os.remove(temp_audio_path)

if __name__ == "__main__":
    main()
