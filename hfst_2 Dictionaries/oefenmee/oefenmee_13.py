# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit, waarde in fruitmand.items():
    vraag = int(input(f"Hoeveel {fruit} will je kopen"))
    fruitmand[fruit] = waarde + vraag

print(fruitmand)

for fruit, waarde in fruitmand.items():
    print(f"Er zijn nu {waarde} {fruit}")
