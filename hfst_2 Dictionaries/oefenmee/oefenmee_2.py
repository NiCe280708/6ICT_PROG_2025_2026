# Start de oefen mee met onderstaande dictionary.
fruit = "appel"
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
nieuw_fruit = "mango"
nieuw_aantal = "67"

fruitmand[nieuw_fruit] = nieuw_aantal
print (fruitmand)

fruitmand[fruit] = nieuw_aantal

weg_fruit = "kers"
fruitmand.pop(weg_fruit)
print (fruitmand)