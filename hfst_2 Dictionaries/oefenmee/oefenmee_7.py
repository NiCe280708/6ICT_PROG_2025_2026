# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}

while True:
    input_vraag = input("Welke gast")
    if input_vraag in gasten:
        print(f"Welkom {input_vraag} de {gasten[input_vraag]}")
        gasten.pop(input_vraag)
    elif input_vraag == "STOP":
        break
    else:
        print("Niet in lijst")

