import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import time

audio = sr.Recognizer()
maquina = pyttsx3.init()

def comandos():
    while True:
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language="pt-BR")
                comando = comando.lower()

                if "gabriele" in comando:
                    comando = comando.replace("gabriele","")
                    maquina.say(comando)
                    maquina.runAndWait()

                    if "oi" in comando:
                        maquina.say("Paulo")
                        maquina.say("Como posso ajudar")
                        maquina.runAndWait()

                    elif "horas" in comando:
                        hora = datetime.datetime.now().strftime("%H:%M")
                        maquina.say("Agora são " + hora)
                        maquina.runAndWait()

                    elif "toca" in comando:
                        musica = comando.replace("toca", "") 
                        resultado = pywhatkit.playonyt(musica)
                        maquina.say("Tocando Música")
                        maquina.runAndWait()

                    elif "procure" in comando:
                        procurar=comando.replace("procure","") 
                        wikipedia.set_lang("pt")
                        resultado=wikipedia.summary(procurar,2)
                        print(resultado)
                        maquina.say(resultado)
                        maquina.runAndWait()

                    elif "piada" in comando:
                        maquina.say("Qual é o cúmulo da paciência")
                        time.sleep(2.5)
                        maquina.say("Esperando a uva passar")
                        maquina.runAndWait()

        except:
            print("Microfone não está funcionando")

comandos()
