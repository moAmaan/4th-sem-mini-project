def GetAudio():
    import numpy as np
    import sounddevice as sd
    from scipy.io.wavfile import write

    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    write('./Files/output.wav', fs, myrecording)  # Save as WAV file 


    
    
   
   

