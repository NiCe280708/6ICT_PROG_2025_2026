# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgi?': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}
for landen in grootste_steden:
    print(f"Grootste steden in {landen} zijn")
    for hoofdsteden in grootste_steden[landen]:
        print(f"{hoofdsteden} met {grootste_steden[landen][hoofdsteden]}")
