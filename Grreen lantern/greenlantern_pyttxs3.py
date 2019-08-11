import pyttsx3;
#engine = pyttsx3.init();
#engine.say("I will speak this text");
#engine.runAndWait() ;

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#for voice in voices:
#   engine.setProperty('voice', voice.id)
#   engine.say('The quick brown fox jumped over the ')
#   print(voice)
#   engine.runAndWait()


engine = pyttsx3.init();
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', rate-70)
engine.setProperty('volume', volume-0.50)
engine.say("In the brightest day")
engine.setProperty('volume', volume-0.50)
engine.say("and the darkest night")

engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', volume+0.50)

engine.say(" No evil")
engine.setProperty('volume', volume-0.50)
engine.say(" shall escape my sight")
engine.setProperty('voice', voices[0].id)
engine.say("To all those who worships evil's might") 
engine.setProperty('voice', voices[1].id)
engine.say(" Beware my power ")
engine.setProperty('volume', volume+5)
engine.say(" Green Lantern's light");
engine.runAndWait() ;

