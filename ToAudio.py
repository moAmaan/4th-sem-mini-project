def Confirm():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say("Mail has been sent Successfully")
    engine.runAndWait()


def ToAudio(mail_from, mail_subject, mail_content):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(f"Mail from {mail_from}         Subject {mail_subject}        {mail_content}")
    engine.runAndWait()

def Menu():
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say("Welcome to voiced mail System for visually impaired people")
    engine.say("System features are:")
    engine.say("Say Send : to  Send an email")
    engine.say("Say recieve: to Check inbox And read email")
    engine.say("Say exit: to Exit the System")
    engine.say("Give your choice please")
    engine.runAndWait()
