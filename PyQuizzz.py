try:
    temps = "logistique"
    import logistique
    temps = "datetime"
    from datetime import datetime
    temps = "os"
    import os
    temps = "urllib"
    import urllib.request as dl
    from urllib import request
    temps = 'json'
    import json
    excepted = True
except ModuleNotFoundError:
    print("Une erreur d'importation est survenue avec le module : '" + temps + "'. Merci de contacter un administrateur PyQuizzz")
    excepted = False
    

"""              
    Thanks to using PyQuizzz
    Made by TheAngelLCF (https://github.com/TheAngelLCF/)
    Logiciel gratuit propriétaire
"""

def game():
    
    dico_csv = logistique.import_csv()
    
    game_dico = logistique.randomise_dico(dico_csv)
    
    compteur_win = 0
    compteur_lost = 0
    compteur_question = 1
    pseudo = input("Votre nom d'utilisateur: ")
    
    tours_max = 0
    
    while tours_max <= 0 or tours_max > len(game_dico):
        try:
            tours_max = input("Combien de tours maximun voulez-vous (entre 1 et " + str(len(game_dico)) + ") ? : ")
            tours_max = int(tours_max)
        except ValueError:
            tours_max = 0
        except TypeError:
            tours_max = 0
    
    time = datetime.now()
    started_at = (time.minute, time.second)
    
    for dico in game_dico:
        if(compteur_question > tours_max):
            break
        dico_rep = {1: dico["rep1"], 2: dico["rep2"], 3: dico["rep3"], 4: dico["rep4"]}
        print("Question n°" + str(compteur_question))
        
        compteur_question += 1
        
        print("\n" + dico["question"] + "\n")
        
        compteur_temps = 1
            
        for _,k in dico_rep.items():
            if(k == " "):
                break
            print("Réponse " + str(compteur_temps) + ": " + k)
            compteur_temps += 1
        
        print("skip pour passer cette question")
        
        rep_joueur = 0
        
        while rep_joueur not in [1,2,3,4, "skip"]:
            rep_joueur = input("\nQuelle est votre réponse: ")
            try:
                rep_joueur = int(rep_joueur)
                if(rep_joueur < 1 or rep_joueur > 4):
                    print("Merci de bien mettre un numéro disponible")
                    rep_joueur = 0
                    continue
                elif(dico_rep[rep_joueur] == " "):
                    print("Ce choix n'est pas possible")
                    rep_joueur = 0
            except ValueError:
                continue
            except TypeError:
                continue
        
        if(rep_joueur == int(dico["bonne_reponse"])):
            compteur_win += 1
            print("Bravo, vous avez trouvé la bonne réponse\n\n")
        elif(rep_joueur == "skip"):
            compteur_lost += 1
            print("Vous venez de passer la question, la réponse était " + dico_rep[int(dico['bonne_reponse'])] + "\n\n" )
        else:
            compteur_lost += 1
            print("Faux, la réponse était " + dico_rep[int(dico['bonne_reponse'])] + "\n\n" )
    
    time = datetime.now()
    end_at = (time.minute, time.second)
    
    time_all = logistique.temp_pris(started_at, end_at)
    
    print("Vous vennez de finir le jeu, votre score est de " + str(compteur_win) + "manche(s) gagné(s) contre " + str(compteur_lost) + "manche(s) perdu(s)")
    print("Vous avez prit " + time_all)
    print("Merci d'avoir jouez à PyQuizzz !")
    
    with open('resultat.txt', 'a', encoding='utf-8') as file:
        file.write("<" + "=" * 20 + ">\n")
        file.write("Nom d'utilisateur: " + pseudo + "\n")
        file.write("Bonne réponse(s):" + str(compteur_win) + "/" + str(tours_max) + "        (moyenne : " + str(int(100 * compteur_win / tours_max))  + "%)")
        file.write("\nTemps pris: " + time_all + "\n")
       
    input("")
    
    start()
    
    return None
          

def modif():
    print("Vous venez de rentrer dans la fonction de mise à jour du fichier csv, en cas problème, merci de contacter un administrateur PyQuizzz")
    
    question = input("Quelle est la question ? : ")
    
    rep_max = 0
    while not(rep_max >= 2 and rep_max <= 4):
        try:
            rep_max = int(input("Combien de réponse voulez-vous mettre (min 2 |max 4): "))
        except TypeError:
            continue
        except ValueError:
            continue
    
    reps = []
    for k in range(1, rep_max + 1):
        reps.append(input("Réponse numéro " + str(k) + " : "))
    for _ in range(4 - rep_max):
        reps.append(" ")
    
    temps_compteur = 0
    
    for reponse in reps:
        if(reponse == " "):
            break
        temps_compteur += 1
        oui_non = ""
        while oui_non.lower() not in ["oui", "non"]:
            oui_non = input("Est-ce que la réponse \"" + str(reponse) + "\" est la bonne réponse ? (oui | non) : ")
        if(oui_non == "oui"):
            break
    
    WEBHOOK_URL = 'https://discord.com/api/webhooks/883054140899590145/97iNGJZiVKm0Qxup6ChfLLKG0e0L_CVIsuqwSk2kh1nQNKqmrcdpdrL4L-TUH-UOifWz'
    
    temps = '|'
        
    for string in reps:
        if(reps == ' '):
            break
        temps += str(string) + '|'
        
    payload  = {
        'content' : "> Une nouvelle personne à ajouter un quizzz",
        'embeds' : [
            {
                'description': 'Question: ' + question + '\nRéponses: ' + temps + '\nBonne réponse: ' + str(temps_compteur),
            }
            ]
        }
        
    headers = {
        'Content-Type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }
        
        
    try:
        req = request.Request(url=WEBHOOK_URL, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
        request.urlopen(req)
    except:
        print('Erreur, merci de contacter un administrateur PyQuizzz !')
        input('Impossible d\'envoyer la question dans le serveur, veuillez cliquez sur \'entrée\' pour continuer')
    
    
    logistique.edit_file(len(logistique.import_csv()), question, reps, temps_compteur)
    
    start()
    
    return None

def start():    
    liste_files = os.listdir()
    if("quizzz.csv" not in liste_files):
        print("La base de donnée n'est pas présente, téléchargement automatique en cours ...")
        try:
            dl.urlretrieve("https://pastebin.com/raw/BaRdqZ66", "quizzz.csv")
            print("Le fichier 'quizzz.csv' a été télécharger avec succés")
        except:
            print("Le fichier 'quizzz.csv' n'a pas pu être télécharger. Merci de vérifier votre connexion internet !")
    choix = ""
    while choix not in ["jouer", "ajouter", "stop"]:
        choix = input("Que veux-tu faire (choix possible: jouer | ajouter | stop ): ")
                
    if(choix == "jouer"):
        game()
    elif(choix == "stop"):
        return None
    else:
        modif()

if __name__ == "__main__" and excepted:
    start()
