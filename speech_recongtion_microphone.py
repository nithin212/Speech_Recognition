import speech_recognition as sr
r=sr.Recognizer()

with sr.Microphone() as source:   #we have to ue with the files which are unmanaged.
  audio=r.listen(source)
try:
  print("System predicts:",+r.recognize_google()audio) #using google's api for speech recognition
except Exception:
  print("Some Techncial Glitches")
