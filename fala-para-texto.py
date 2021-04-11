# -*- coding: utf-8 -*-

import speech_recognition as sr

def falaParaTexto(texto = "", max_contador = 5):    
    contador = 0
    print("Microfones:", sr.Microphone.list_microphone_names())
    microfone = sr.Recognizer()
    with sr.Microphone() as canal:
        microfone.adjust_for_ambient_noise(canal)
        while contador < max_contador:
            try:
                contador += 1
                audio = microfone.listen(canal)
                texto = microfone.recognize_google(audio, language = "pt-BR")
                texto = texto.encode("utf8")
                break
            except Exception as e:
                print("error:", e)
    return texto

# print("Entendi: " + falaParaTexto().decode("utf8"))
