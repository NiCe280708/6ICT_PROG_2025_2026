# Start de opdracht met onderstaande code.
deelnemers = ["Lucas", "Emma", "Jan", "Piet", "Maud"]

deelnemers_talen = {    
    "Lucas": "python",    
    "Piet": "assembly",    
    "Maud": "ruby"
}

for index, mensen in enumerate(deelnemers):
    taal_check = deelnemers_talen.get(mensen, "nee")
    if taal_check == "nee":
        print("Vul het in")
        extra = input("Wat is je taal")
        if extra == "":
            continue
        else:
            deelnemers_talen[mensen] = extra
    else:
        print("Dan niet")

print (deelnemers_talen)