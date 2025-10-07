sport_uitslagen = {
    "Emma": [2, 3, 1, 4, 2],
    "Liam": [1, 2, 1, 3, 0],
    "Noah": [0, 1, 2, 1, 3],
    "Sarah": [3, 3, 4, 2, 1],
    "Kiana": [1, 0, 2, 1 , 2],
    "Lucas": [2, 1, 3, 1, 0]
}
maximaal_punt = 0
minimaal_punt = 100
naam_opslag_max = ""
naam_opslag_min = ""
for mensen in sport_uitslagen:
    Punten_som = 0
    for punten in sport_uitslagen[mensen]:
        Punten_som += punten 
    Punten_som = Punten_som/5
    if Punten_som > maximaal_punt:
        maximaal_punt = Punten_som
        naam_opslag_max = mensen
    elif Punten_som < minimaal_punt:
        minimaal_punt = Punten_som
        naam_opslag_min = mensen

print (f"{minimaal_punt} gemiddeld van {naam_opslag_min}")
print (f"{maximaal_punt} gemiddeld van {naam_opslag_max}")