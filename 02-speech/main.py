import sys
from api_communication import *
filename=filename = "kashifurdu.wav"

audio_url=upload(filename)
save_transcript(audio_url,filename)