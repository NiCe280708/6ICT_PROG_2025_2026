def vergelijker(x,y):
    if x > y:
        Grootte = "Groter"
    elif x == y:
        Grootte = "Even"
    else:
        Grootte = "Kleiner"
    print(Grootte)


vergelijker(4,3) # 4 is groter dan 3
vergelijker(2,9) # 2 is kleiner dan 9
vergelijker(6,6) # 6 is gelijk aan 6