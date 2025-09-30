# Start de oefen mee met onderstaande dictionary.
som = 0
planner = {
    "Slaap": 6,
    "Werk":  8,
    "Ontspanning": 4
}
print(list(planner.values()))

print("Planning")
for sleutel,waarde in planner.items():
    print(sleutel,waarde)
    som += -waarde
    tijd_over =   som + 24

print (tijd_over)
    