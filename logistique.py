import csv
from random import randint

def temp_pris(start, end):
    """Permet de calculer le temps que l'utilisateur à pris
    param : start / end : tuple (minutes, secondes)
    param : minutes / secondes : int
    """
    retour = ''
    start_m, start_s = start 
    end_m, end_s = end
    temps = (ecart(start_m, end_m), ecart(start_s, end_s))
    if(temps[0] == 0):
        retour += ''
    else:
        if(temps[0] == 1):
            retour += str(temps[0]) + ' minute '
        else:
            retour += str(temps[0]) + ' minutes '
    if(temps[1] == 0):
        retour += ''
    else:
        if(temps[1] == 1):
            retour += str(temps[1]) + ' seconde'
        else:
            retour += str(temps[1]) + ' secondes'
    return retour

def ecart(first, second):
    ecart_int = 0
    while first != second:
        if(first == 60):
            first = 1
            ecart_int += 1
        else:
            ecart_int += 1
            first += 1
    return ecart_int

def create_file(): # id/question/reps(liste)/bonne reponse
    with open('quizzz.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write("id,question,reps,bonne_reponse\n")

def import_csv():
    with open('quizzz.csv', "r", encoding='utf-8') as csv_file:
        it_dictreader = csv.DictReader(csv_file, delimiter='|')    
        table = [dict(enregistrement) for enregistrement in it_dictreader]
    return table

def edit_file(idd, question, reps, bonne_reponse):
    with open('quizzz.csv', 'a', encoding='utf-8') as csv_file:
        rep1,rep2,rep3,rep4 = reps
        csv_file.write(str(idd) + "|" + str(question) + "|" + str(rep1) + "|" + str(rep2) + "|"  + str(rep3) + "|"  + str(rep4) + "|" + str(bonne_reponse) + "\n")
        print("Logs: Ajout effectué dans la base de donnée")
        
def random_int_on_dic(dico):
    taille_dico = len(dico)
    deja_pris = []
    while len(deja_pris) != taille_dico:
        temp = randint(0, taille_dico - 1)
        if(temp not in deja_pris):
            deja_pris.append(temp)
    return deja_pris

def randomise_dico(dico):
    random_int = random_int_on_dic(dico)
    new_dico = []
    for number in random_int:
        new_dico.append(dico[number])
    return new_dico


        
