lang= raw_input("Choose your language: es, en, fr")
def greet(lang):
    if lang== "es":
        return "Hola"
    elif lang== "en":
        return "Hello"
    else:
        return "Bonjour"
        
if lang=="es":
    name=raw_input("Su nombre:")
elif lang=="en":
    name=raw_input("State your name:")
else:
    name=raw_input("votre nom")

print greet(lang), name
