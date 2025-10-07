smiley = [
    [0, 1, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [3, 0, 0, 0, 3],
    [0, 3, 3, 3, 0]
]
woord_som = ""
teller = 0
for index, lijsten in enumerate(smiley):
    woord_som = ""
    for nummers in smiley[index]:
        if nummers == 0:
            woord_som += " "
        elif nummers == 1:
            woord_som += "#"
        elif nummers == 2:
            woord_som += "."
        elif nummers == 3:
            woord_som += "-"
    print (woord_som)