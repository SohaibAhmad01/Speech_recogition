from gtts import gTTS
import os
import playsound

text = "Suresh Aaj ham log physics ke chapter number 2 kinematics ke bare mein baat karenge Jo physics ki Kaisi branch hai jismein Ham Kisi bhi object ki motion ko study karte hain lekin use motion ki cause ko study nahi kiya Jata ab ismein rest and motion do aur chijen अलग-अलग a Jaati Hain rest Ki Baat karen to Kisi bhi body rest Mein Kab Hogi Jab vah apni position Apne object ke apne ticket ke liha se change Nahin Karegi Agar motion Ki Baat Karen To Aisa object Jo apni position change kar raha hai apne ticket ki Had Se surrounding ke liha se to vah motion Mein hoga to motion ki types Agar a Jaati Hain jismein translater emotion Hai linear motion Hai rotatory motion Hai vibratory motion hai agar aap vibratory motion ke bare mein baat karen to vibratory motion Aisi motion ko kaha jata hai jismein koi bhi object apni min position ke aage aur Piche move karta hai to uski motion ko Ham vibratory motion Kahate Hain yah min position jo hai uski vah position Hoti Hai Jahan per vah object rest Mein Hota Hai Jis Tarah Ek baccha jo hai vah Jhule Mein Jhula jhul raha hai uski motion vibrate Rahi Hogi vibratory motion ke bad Ham baat karenge rotatory motion rotatory motion Aisi hoti hai jo Kisi bhi object Apne access per Gir ghumta Hai uski use motion ko Ham rotatory motion Kahate Hain Jis Tarah Hamari Arth jo hai vah apne Axis per rotate kar rahi hai vah Din Aur Raat Ka jo badalna hai vah Arth ki rotatory motion ki vajah se hota hai to Arth ki motion rotatory motion Hogi wheel jo hai vah bhi rotatory motion ki example Mein a jata hai agar aap linear motion Ki Baat karen to linear motion ko Ham linear motion Kahenge ISI Tarah Agar Baat Karen Ham dusri chijon ke bare mein a Jaate Hain scalar quantity Aisi quantity ko Kahate Hain jismein object"
language = 'ur'
filename = 'output.mp3'

# Create a TTS object with the translated text and save it to an MP3 file
tts = gTTS(text=text, lang=language)
tts.save(filename)

# Play the audio file using the playsound library
playsound.playsound(filename)