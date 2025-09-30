# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}

aantal = int(input("Voor hoeveel mensen"))


print("Recept voor blablabla")
for sleutel, waarde in recept.items():
    waarde_aangepast = (waarde / 4) * aantal
    print(sleutel, waarde_aangepast)