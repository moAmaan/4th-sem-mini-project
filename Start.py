#import files
import pyttsx3
import GetAudio
import ToAudio
import AudioToText


engine = pyttsx3.init()
engine.setProperty('rate', 125)

while True:

   ToAudio.Menu()


   GetAudio.GetAudio()


   choice=AudioToText.AudioToText()


   if choice=='Send' or choice=='send' :
         engine.say("Select a contact and say your message") 
         engine.runAndWait()
         import SendMail
  
   elif choice=='Recieve' or choice=='recieve' :
         import RecieveMail
   

   elif choice=='Exit' or choice=='exit' :
         engine.say("Exiting the system")
         engine.runAndWait()
         break

   else:
         engine.say("wrong choice is given , please provide valid choice")
         engine.runAndWait()