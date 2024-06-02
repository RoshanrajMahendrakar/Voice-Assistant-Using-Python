import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
def sptext():
	recognizer=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		recognizer.adjust_for_ambient_noise(source)
		audio=recognizer.listen(source)
		try:
			print("Recognizing...")
			data=recognizer.recognize_google(audio)
			return data
		except sr.UnknownValueError:
			print(" Not Understand ")
def speechtx(x):
	engine=pyttx3.init()
	voices=engine.getProperty('voices')
	engine.setProperty("voice"voices[1].id)
	rate=engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine(x)
	engine.runAndWait()
if __name__ == '__main__':
	if "hello john" in sptext().lower():
		while true:
			data1=sptext().lower()
			if "name" in data1:
				name="my name is john"
				speechtx(name)	
			elif "age" or "old" in data1:
				age="iam 1 year old"
				speechtx(age)
			elif "time" in data1:
				time=datetime.datetime.now().strftime("%I%M%p")
				speechtx(time)	
			elif 'youtube' in data1:
				webbrowser.open("https://www.youtube.com/")
			elif 'google' or 'web' in data1:
				webbrowser.open('https://www.google.com/')	
			elif 'joke' in data1:
				joke_1=pyjokes.get_joke(language="en",category="all")
				print(joke_1)
				speechtx(joke_1)
			elif "song"	in data1:
				address="D:\roshan\songs"
				list_song=os.listdir(address)
				print(list_song)
				os.startfile(os.path.join(address,list_song[0]))
			elif 'exit' in data1:
				speechtx("Thanks for using john")
				break
            time.sleep(5)



	else:
		print("thanks")	

				