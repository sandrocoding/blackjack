'''
Gioco del Blackjack
Versione 1.0

-- Versione preliminare

'''

import random

# --------------------
# Funzioni di supporto
# --------------------

def crea_mazzo():

    # Crea un mazzo di 52 carte con gli Array
    # CUORI = ALT + 3
    # PICCHE = ALT + 6
    # FIORI = ALT + 4
    # QUADRI = ALT + 5

    semi = ["♥", "♠", "♦", "♣"]
    valori = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    mazzo = []

    for seme in semi:
        for valore in valori:
            mazzo.append((valore, seme))
    random.shuffle(mazzo)
    
    return mazzo

def pesca_carta(mazzo):
    ''' Pesca una carta dal mazzo (toglie l'ultima) '''
    return mazzo.pop()

def valore_mano(mano):
    '''
        Calcola il valore di una mano
        A (Asso) Vale 11 ma se il valore delle carte va oltre il 21
        allora il valore dell'asso scande a 1
    '''

    valore = 0
    assi = 0

    for carta in mano:
        numero = carta[0]
        if numero in ["J", "Q", "K"]:
            valore += 10
        elif numero in ["A"]:
            valore += 11
            assi += 1
        else:
            valore += int(numero)
    
    # Se sballiamo oltre il 21 e abbiamo degli Assi, 
    # questi vengono trasformati da 11 a 1

    while valore > 21 and assi > 0:
        valore -= 10
        assi -= 1

    return valore    

def mostra_mano(giocatore, mano):
    '''
        Mostra la mano in maniera leggibile
    '''
    
    carte_str = " ".join([f"{val}{seme}" for val, seme in mano])
    print(f"{giocatore}: {carte_str} (valore: {valore_mano(mano)})")

def mostra_mano_dealer_nascosta(mano):
    '''
        Mostra la mano del banco (dealer) con una carta nascosta
    '''
    prima_carta = mano[0]
    print(f"Banco: {prima_carta[0]}{prima_carta[1]} [carta coperta]")


# -----------------
# Logica del gioco
# -----------------

def turno_giocatore(mazzo,mano_giocatore,mano_dealer):
    '''
        Gestisce il turno del giocatore 
        HIT (Carta) -- STAND (Stai così)
    '''

    while True:
        print("\n--------------------------")
        mostra_mano_dealer_nascosta(mano_dealer)
        mostra_mano("Tu:", mano_giocatore)

        if valore_mano(mano_giocatore) > 21:
            print("Hai perso!")
            return False
        
        scelta = input("Vuoi un'altra carta? (h = pesca(hit) / s = rimani(stand)): ").strip().lower()

        if scelta == "h":
            mano_giocatore.append(pesca_carta(mazzo))
        elif scelta == "s":
            return True
        else:
            print("Scelta non valida, inserisci 'h' o 's'")

def turno_dealer(mazzo, mano_dealer):
    '''
        Il banco pesca finchè ha meno di 17
    '''
    print("\nTurno del banco...")
    mostra_mano("Banco", mano_dealer)

    while valore_mano(mano_dealer) < 17:
        input("Premi il tasto INVIO per far pescare il banco...")
        mano_dealer.append(pesca_carta(mazzo))
        mostra_mano("Banco", mano_dealer)
    
    if valore_mano(mano_dealer) > 21:
        print("Il banco perde!!")
        return False
    return True

def determina_vincitore(mano_giocatore, mano_dealer):
    '''
    Confronta i punteggi e stampa il risultato
    '''
    valore_g = valore_mano(mano_giocatore)
    valore_d = valore_mano(mano_dealer)

    print("\n=== RISULTATO FINALE ===")
    mostra_mano("Tu", mano_giocatore)
    mostra_mano("Banco", mano_dealer)

    if valore_g > 21:
        print("Hai sballato!! Vince il banco")
    elif valore_d > 21:
        print("HAI VINTO!! Il banco ha sballato")
    elif valore_g > valore_d:
        print("HAI VINTO!!")
    elif valore_g < valore_d:
        print("Mi spiace vince il banco!!")
    else:
        print("Pareggio!")

def gioca_blackjack():
    '''
    Gioco del BlackJack
    Funzione principale
    '''

    print("=== BENVENUTO AL GIOCO DEL BLACKJACK ===")

    while True:
        mazzo = crea_mazzo()
        mano_giocatore = [pesca_carta(mazzo), pesca_carta(mazzo)]
        mano_dealer = [pesca_carta(mazzo), pesca_carta(mazzo)]

        # Turno Giocatore
        continua = turno_giocatore(mazzo, mano_giocatore, mano_dealer)
        
        if not continua:
            # Giocatore ha sballato, fine mano
            determina_vincitore(mano_giocatore, mano_dealer)
        else:
            # Turno banco
            dealer_sta = turno_dealer(mazzo, mano_dealer)
            determina_vincitore(mano_giocatore, mano_dealer)

    # Chiedi se rigiocare
    risposta = input("\nVuoi giocare un'altra mano? [s/n] ").strip(),lower()
    if risposta != "s":
        print("Grazie per aver giocato!")
        return False
    

# Avvio del Gioco

if __name__ == "__main__":
    gioca_blackjack()




