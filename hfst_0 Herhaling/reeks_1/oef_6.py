def mag_stemmen(leeftijd, inwoner):
    if leeftijd >= 18 and inwoner == True:
        Stemrecht = "Mag"
        return Stemrecht
    else:
        Stemrecht = "Mag niet"
        return Stemrecht



print( mag_stemmen(17, False) ) # mag niet stemmen
print( mag_stemmen(29, False) ) # mag niet stemmen
print( mag_stemmen(8,  True)  ) # mag niet stemmen
print( mag_stemmen(65, True)  ) # mag stemmen