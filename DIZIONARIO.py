meme = {
        "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
        "LOL": "Una risposta comune a qualcosa di divertente",
        "SHEESH": "Leggera disapprovazione",
        "CREEPY": "Spaventoso, inquietante",
        "PARA": "preoccuparsi per qualcosa, paranoiarsi"
        }
domanda = input("che parola non sai? (scrivi in MAIUSCOLO)")

# la parte di cui non so niente if? random? NON LO SO!!!!
while True:
    if domanda in meme.keys():
        print(meme[domanda])
    
    else:
        print("Mi dispiace, ma non so il significato")
