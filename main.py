inventario = {
    0: {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
    1: {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
    2: {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}

def aggiungi_prodotto():
    nome = input("Inserisci il nome del prodotto: ")
    while True:
        try:
            quantita = int(input("Inserisci la quantità: "))
            prezzo = float(input("Inserisci il prezzo: "))
            break
        except ValueError:
            print("Errore: inserisci un numero valido per quantità e prezzo.")
    
    nuovo_id = max(inventario.keys()) + 1
    inventario[nuovo_id] = {"nome": nome, "quantità": quantita, "prezzo": prezzo}
    print(f"Prodotto aggiunto con ID {nuovo_id}.")

def modifica_quantita():
    try:
        id_prodotto = int(input("Inserisci l'ID del prodotto da modificare: "))
        if id_prodotto in inventario:
            nuova_quantita = int(input("Inserisci la nuova quantità: "))
            inventario[id_prodotto]["quantità"] = nuova_quantita
            print("Quantità aggiornata con successo.")
        else:
            print("Errore: ID prodotto non trovato.")
    except ValueError:
        print("Errore: inserisci un numero valido.")

def modifica_prezzo():
    try:
        id_prodotto = int(input("Inserisci l'ID del prodotto da modificare: "))
        if id_prodotto in inventario:
            nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))
            inventario[id_prodotto]["prezzo"] = nuovo_prezzo
            print("Prezzo aggiornato con successo.")
        else:
            print("Errore: ID prodotto non trovato.")
    except ValueError:
        print("Errore: inserisci un numero valido.")

while True:
    print("\nMenu:")
    print("1. Aggiungere un prodotto")
    print("2. Modificare la quantità di un prodotto")
    print("3. Modificare il prezzo di un prodotto")
    print("6. Esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        aggiungi_prodotto()
    elif scelta == "2":
        modifica_quantita()
    elif scelta == "3":
        modifica_prezzo()
    elif scelta == "6":
        print("Uscita dal programma.")
        break
    else:
        print("Opzione non valida. Riprova.")
