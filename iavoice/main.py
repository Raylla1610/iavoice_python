import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice, voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    r = sr.Recognizer()
    with sr.Micriphone() as source:
        print("Ouvindo...")
        r.pause_threshol = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-br')
        print(f"usuário disso: {query}\n")

    except Exception as e:
        print("Poderia dizer novamente...")
        return "None"

    return query  

def create_todo_list():
    speak("o qye você quer adicionar a sua lista de tarefas?")
    task = recognize_speech()
    with open('todo.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {task}\n")
    speak("tarefa adicionada")


def search_web():
    speak("o que você gostaria de procurar?")
    query = recognize_speech()
    url = f"https://WWW.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Aqui está os resultadores para {query}.")

def set_reminder():
    speak("O que eu devo lembrá-lo?")
    task = recognize_speech()
    speak("Em quantos minutos?")
    mins = recognize_speech()
    mins = int(mins)
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutos=mins)
    with open('reminders.txt','a') as f:
        f.write(f"{reminder_time} - {task}\n")
    speak(f"Lembrete definido para{mins} minitos a patir de agora.")

def main():
    speak("Olá!, Eu sou seu assistente pessoal Jarvis. Em que posso ajudar?")
    while True:
        query = recognize_speech().lower()

        if 'criar um lista de tarefas' in query: 
            create_todo_list()

        elif 'procure na web' in query:
            search_web()

        elif'criar um lembrete' in query:
            set_reminder()

        elif "pare" in query or "sair" in query:
            speak("Até logo!")
            break

        else:
            speak("Desculpe, Não entendi. Poderia repetir?")

main()
                          
              


