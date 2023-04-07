import speech_recognition as sr
import json
import pyaudio
from google.oauth2.service_account import Credentials

# set up the recognizer and microphone
r = sr.Recognizer()
mic = sr.Microphone()

# set up the Google Cloud Speech-to-Text API credentials
# replace the placeholder values with the path to your JSON file containing the credentials
credentials_json_path = "credentials.json"
with open(credentials_json_path, "r") as f:
    credentials_json = json.load(f)

# create a credentials object from the JSON key file
credentials = Credentials.from_service_account_file(credentials_json_path)

# create a recognizer instance with the Google Cloud Speech-to-Text API credentials
google_recognizer = sr.Recognizer()
google_recognizer.credentials = credentials

# set up the PyAudio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

print("Say something...")

# listen for audio input from the user
with mic as source:
    audio_data = r.record(source, duration=120)
text=None
# transcribe the audio to text using the Google Cloud Speech-to-Text API
try:
    text = google_recognizer.recognize_google(audio_data)
    print(f"Transcription: {text}")
except sr.UnknownValueError:
    print("Google Cloud Speech-to-Text API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Cloud Speech-to-Text API: {e}")
except Exception as e:
    print(e)
# save the transcription to a text file
with open("transcription.txt", "w") as file:
    file.write(text)


