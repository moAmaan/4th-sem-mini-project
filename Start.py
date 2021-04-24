#import files
import pyttsx3
import GetAudio
import ToAudio
import AudioToText


engine = pyttsx3.init()
engine.setProperty('rate', 125)


ToAudio.Menu()


GetAudio.GetAudio()


choice=AudioToText.AudioToText()


if choice=='Send' or choice=='send' :
   engine.say("Please say your message") 
   engine.runAndWait()
   import SendMail
   exit()
    
if choice=='Recieve' or choice=='recieve' :
   import RecieveMail
   exit()

if choice=='Exit' or choice=='exit' :
   exit()

else:
    engine.say("wrong choice is given , please provide valid choice")
    engine.runAndWait()