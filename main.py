import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech Recognition App")

    r = sr.Recognizer()

    # Wrap the app content in a container
    with st.beta_container():
        st.write("Click the 'Start Recording' button and speak something:")
        if st.button("Start Recording"):
            with sr.Microphone() as source:
                st.write("Listening...")
                audio = r.listen(source)

                try:
                    st.write("Processing...")
                    text = r.recognize_google(audio)
                    st.write("Transcription:", text)
                except sr.UnknownValueError:
                    st.write("Sorry, I could not understand audio.")
                except sr.RequestError as e:
                    st.write("Error:", e)

if __name__ == "__main__":
    main()
