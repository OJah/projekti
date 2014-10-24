class hlo:
    etunimi = ""
    sukunimi = ""
    puhelin = 0
    
 
def tulostaluettelo(lista):
    henkilo = hlo()
    for i in range(len(lista)):
        henkilo = lista[i]
        print(henkilo.etunimi, henkilo.sukunimi, henkilo.puhelin)
    print()

#Tässä kohtaa näyttäisi olevan jokin virhe!?!?!    
def lisaahlo(lista):
    henkilo.etunimi = input("Anna lisättävä etunimi: ")
    henkilo.sukunimi = input("Anna lisättävä sukunimi: ")
    henkilo.puhelin = input("Anna lisättävä puhelinnumero: ")
    lista.append(henkilo)
    print()
    return lista

#Tähän funktioon voisi lisätä viestin käyttäjälle, jos poistettavaa henkilöä ei löydy 
def poistahlo(lista):
    henkilo = hlo()
    etunimi = input("Anna poistettavan etunimi: ")
    sukunimi = input("Anna poistettavan sukunimi: ")
    for i in range(len(lista)):
        henkilo = lista[i]
        if (henkilo.etunimi == etunimi) and (henkilo.sukunimi == sukunimi):
            print(henkilo.etunimi, henkilo.sukunimi, henkilo.puhelin, "tuhotaan.")
            del lista[i]
            break
    print()
    return lista
 
def tiedostostaluku(lista):
    henkilo = hlo()
    try:
        tiedosto = open("luettelo.txt", "r")
    except IOError:
        print("Virhe")
    while True:
        rivi = tiedosto.readline()
        rivi = rivi[:-1]
        if len(rivi) == 0:
            break
        alkiot = rivi.split(" ")
        henkilo = hlo()
        henkilo.etunimi = alkiot[0]
        henkilo.sukunimi = alkiot[1]
        henkilo.puhelin = alkiot[2]
        lista.append(henkilo)
    tiedosto.close()
    return lista
 
def tiedostoonkirjoitus(lista):
    
    try:
        tiedosto = open("luettelo.txt", "w")
    except IOError:
        print("Virhe")
    for i in range(len(lista)):
        henkilo = hlo()
        henkilo = lista[i]
        tiedosto.write(str(henkilo.etunimi) +" " + str(henkilo.sukunimi) +" " + str(henkilo.puhelin) + "\n")
    tiedosto.close()
    
def paavalikko():
    lista = []
    lista = tiedostostaluku(lista)
    while True:
        print("Puhelinluettelo:")
        print("1) Selaa luetteloa")
        print("2) Lisää henkilö")
        print("3) Poista henkilö")
        print("0) Lopeta")
        valinta = int(input("Mitä haluat tehdä?: "))
        if valinta == 1:
            tulostaluettelo(lista)
        elif valinta == 2:
            lista = lisaahlo(lista)
        elif valinta == 3:
            lista = poistahlo(lista)
        elif valinta == 0:
            tiedostoonkirjoitus(lista)
            break
        else:
            print("Syöte ei kelpaa.")
paavalikko()
