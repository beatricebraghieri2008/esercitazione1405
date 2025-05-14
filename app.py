import random

def main():
    clients = []

    # Inserimento dati clienti
    while True:
        try:
            code = int(input('Inserisci codice cliente (999999 per terminare): '))
            if code == 999999:
                break
            kg = float(input('Inserisci kg lavati: '))
            euro = float(input('Inserisci euro pagati: '))
            clients.append([code, kg, euro])
        except ValueError:
            print("Input non valido. Riprova.")

    # Riepilogo giornata
    tot_kg = sum(c[1] for c in clients)
    tot_euro = sum(c[2] for c in clients)
    max_pagamento = max((c[2] for c in clients), default=0)
    clients_max_pagamento = [c[0] for c in clients if c[2] == max_pagamento]

    print("\n--- Riepilogo Giornata ---")
    print(f"Totale kg lavati: {tot_kg:.2f}")
    print(f"Media kg lavati per cliente: {tot_kg / len(clients) if clients else 0:.2f}")
    print(f"Totale pagato dai clienti: {tot_euro:.2f}")
    print(f"Cliente(i) che ha(hanno) pagato di più: {', '.join(map(str, clients_max_pagamento))}")
    print("Clienti che hanno lavato più di 5 kg:", [c[0] for c in clients if c[1] > 5])
    print("Clienti con pagamenti in dollari:")
    for c in clients:
        print(f"Cliente {c[0]} - {c[1]} kg - {c[2] / 0.89:.2f} USD")

    # Funzione per modificare dati cliente
    def modifica_client(code, nuovi_kg, nuovi_euro):
        for c in clients:
            if c[0] == code:
                c[1], c[2] = nuovi_kg, nuovi_euro
                print(f"Dati del cliente {code} aggiornati.")
                return
        print(f"Cliente con codice {code} non trovato.")

    # Richiesta modifica
    scelta = input("\nVuoi modificare i dati di un cliente? (s/n): ").lower()
    if scelta == 's':
        try:
            code = int(input("Inserisci codice cliente da modificare: "))
            nuovi_kg = float(input("Inserisci nuovi kg: "))
            nuovi_euro = float(input("Inserisci nuovi euro: "))
            modifica_client(code, nuovi_kg, nuovi_euro)
        except ValueError:
            print("Input non valido per la modifica.")

    # Promozione clienti
    codes_premiati = {random.randint(100000, 999999) for _ in range(100)}
    try:
        code_utente = int(input('\nInserisci il tuo codice cliente per verificare la promozione: '))
        print("Hai vinto!" if code_utente in codes_premiati else "Non hai vinto!")
    except ValueError:
        print("Codice non valido.")

if __name__ == '__main__':
    main()


