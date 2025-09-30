# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
while True:

    Input_vraag = input("Welke stad")
    Temperatuur = steden_temp.get(Input_vraag, "??")
    print(Temperatuur)
