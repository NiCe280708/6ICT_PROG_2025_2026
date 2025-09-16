# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
welk_fruit = input("Welk fruit zoek je")
if welk_fruit in fruitmand:
    print(f"{fruitmand[welk_fruit]} {welk_fruit}")
else:
    print("kon niet vinden")