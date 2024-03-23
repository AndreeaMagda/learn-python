'''
Creati un joc Rock-Paper-Scissors pentru doi jucatori. (Hint: Solicitati selectia
jucatorilor (folosind input), comparati alegerile lor, afisati un mesaj de felicitari
pentru castigator si intreabati daca jucatorii doresc sa inceapa un nou joc).
Tine minte regulile:
● Piatra bate foarfeca
● Foarfeca taie hartia
● Hartia bate piatra
'''

def rock_paper_scrissors():
    player1=input(" Player a1lege: piatra, hartie sau foarfeca: ")
    player2 = input("Player 2 alege: foarfeca, hartie sau foarfeca: ")

    if player1 == player2:
        print("Wow. Este remiza!!")
    elif (player1 == "piatra" and player2 == "foarfeca") or \
            (player1 == 'foarfeca' and player2 == 'hartie') or \
            (player1 == 'hartie' and player2 == 'piatra'):
        print("Felicitari! Jucatorul 1 a castigat cu ", player1)
    else:
        print("Felicitari Jucatorul 2 a castigat cu", player2)

    play_again = input("Doriti sa jucati din nou? (da/nu): ").lower()
    if play_again != 'da':
        print("Multumim pentru joc!")
        return


rock_paper_scrissors()
