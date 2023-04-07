#mp3 flac wav

import wave
# audio signal parameters
# -number of channels
# - sample width
# -framerate/sample rate
# -number of frames
# -values of frame

obj=wave.open('file_example_WAV_1MG.wav', 'rb')

print('sample width', obj.getsampwidth())
print('frames rate', obj.getframerate())
print("Number of channels", obj.getnchannels())
print('Number of frames', obj.getnframes())
print('parameters', obj.getparams())

# check the time of audio file
time_audio=obj.getnframes()/ obj.getframerate()
print("time of audio is ", time_audio)

frames=obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))
# print(frames)
print(len(frames)/4)


#above statement didn't give expected answer


obj_new=wave.open('file_example.wav', 'wb')

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()