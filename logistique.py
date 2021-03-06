import csv
from random import randint

def rich_presence():
    """
    Initilazes the connection on this programme and Discord
    
    return type: None
    """
    try:
        from pypresence import Presence
        
        rpc = Presence("883449660801450015")
        rpc.connect()
        rpc.update(state="github.com/TheAngelLCF/PyQuizzz",
                   details="En cours de développement",
                   large_image="python",
                   large_text="Made by Python",
                   buttons=[{"label": "Github (offline)", "url": "https://github.com/TheAngelLCF/PyQuizzz"}])
        return None
    except:
        print("Le module 'PyPresence' n'est pas présent, skip fait sur cette importation")
        return None

def temp_pris(start, end):
    """
    Permet de calculer le temps que l'utilisateur à pris
    
    param :
    start / end : tuple int (minutes, secondes)
    
    return type: str
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
    """
    Retourne l'écart entre deux chiffres dans une horlogue
    
    param:
    first / second : int
    
    return type Int
    """
    ecart_int = 0
    while first != second:
        if(first == 60):
            first = 1
            ecart_int += 1
        else:
            ecart_int += 1
            first += 1
    return ecart_int

def import_csv(csv123):
    """
    Charge la base de donnée csv compris dans la racine du programme de nom de la valeur de 'csv'
    
    param:
    csv: str
    
    return type Liste de Dictionnaires
    """
    with open(csv123, "r", encoding='utf-8') as csv_file:
        it_dictreader = csv.DictReader(csv_file, delimiter='|')    
        table = [dict(enregistrement) for enregistrement in it_dictreader]
    return table

def edit_quizzz(idd, question, reps, bonne_reponse):
    """
    Permet d'ajouter dans la base de données csv compris dans la racine du programme de nom 'pyquizzz.csv' des données
    
    param:
    idd: int
    question: str
    reps: list
    bonne_reponse: int
    
    return type None
    """
    with open('quizzz.csv', 'a', encoding='utf-8') as csv_file:
        rep1,rep2,rep3,rep4 = reps
        csv_file.write(str(idd) + "|" + str(question) + "|" + str(rep1) + "|" + str(rep2) + "|"  + str(rep3) + "|"  + str(rep4) + "|" + str(bonne_reponse) + "\n")
        print("Logs: Ajout effectué dans la base de donnée")
    return None

def create_config(webhook_yn, webhook_url):
    with open('config.csv', 'w', encoding='utf-8') as config_file:
        config_file.write('webhook_yn|webhook\n' + webhook_yn + '|' + webhook_url)
        
def random_int_on_dic(dico):
    """
    Créer une liste avec des nombreux aléatoire uniques
    
    param:
    dico: Dictionnaire
    
    return type List
    """
    taille_dico = len(dico)
    deja_pris = []
    while len(deja_pris) != taille_dico:
        temp = randint(0, taille_dico - 1)
        if(temp not in deja_pris):
            deja_pris.append(temp)
    return deja_pris

def randomise_dico(dico):
    """
    Génére une liste de dictionnaire mélangé aléatoirement
    
    param:
    dico: Dictionnaire
    
    return type List
    """
    random_int = random_int_on_dic(dico)
    new_dico = []
    for number in random_int:
        new_dico.append(dico[number])
    return new_dico

def webhook_sender(webhook_url, payload):
    try:
        from urllib import request
        import json
    except:
        return None
    
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }
        
    try:
        req = request.Request(url=webhook_url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
        request.urlopen(req)
    except:
        print('Erreur durant l\'envoye au webhook \'' + webhook_url + '\', merci de contacter un administrateur PyQuizzz !')

def hastebin_make(payload):
    try:
        import requests
    except:
        return None
    
    post = requests.post('http://hastebin.com/documents', data=payload)
    if(post.status_code == 200):
        return post.json()['key']
    return None