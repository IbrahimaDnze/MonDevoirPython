        #Exo1:
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def lecture_fichier(monfichier):

  #lecture du fichier CSV et retourne une liste de dictionnaires
    liste_donne = []
    with open(monfichier, 'r', encoding='utf-8') as file:
        lecture = csv.DictReader(file)
        for ligne in lecture:
            liste_donne.append({
                'prefecture': ligne['prefecture'],
                'date': ligne['date'],
                'cas': int(ligne['cas']),
                'deces': int(ligne['Décès'])
            })
    return liste_donne

def calcul_statistique(donnee):

    #Calcule les statistiques par préfecture

    statistique = defaultdict(lambda: {'total_cas': 0, 'total_deces': 0})

    for ligne in donnee:
        prefecture = ligne['prefecture']
        statistique[prefecture]['total_cas'] += ligne['cas']
        statistique[prefecture]['total_deces'] += ligne['deces']

    # Calcul du taux de mortalité
    for prefecture in statistique:
        statistique[prefecture]['taux_mortalite'] = (
            statistique[prefecture]['total_deces'] / statistique[prefecture]['total_cas']
            if statistique[prefecture]['total_cas'] > 0 else 0
        )

    return dict(statistique)

def nb_total_cas_par_prefecture(stastistic):

    #Crée un diagramme à barres des cas par préfecture

    prefectures = list(stastistic.keys())
    cas = [stastistic[k]['total_cas'] for k in prefectures]

    plt.figure(figsize=(13, 7))
    plt.bar(prefectures, cas)
    plt.title('TOTAL DE CAS PAR PREFECTURE')
    plt.xlabel('Préfecture')
    plt.ylabel('Nombre de cas')
    plt.xticks(rotation=47)
    plt.tight_layout()
    plt.savefig('cas_par_prefecture.png')
    plt.close()

def taux_mortalite_par_prefecture(statistic):

    #Crée un diagramme à barres des taux de mortalité par préfecture

    prefectures = list(statistic.keys())
    taux = [statistic[p]['taux_mortalite'] * 100 for p in prefectures]

    plt.figure(figsize=(13, 7))
    plt.bar(prefectures, taux)
    plt.title('TAUX DE MORTALITE PAR PREFECTURE')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux de mortalité (%)')
    plt.xticks(rotation=47)
    plt.tight_layout()
    plt.savefig('taux_mortalite.png')
    plt.close()

def main():
    # Lecture des données
    donnee = lecture_fichier('ebola_guinea.csv')

    # Calcul des statistiques
    statistique = calcul_statistique(donnee)

    # Affichage des résultats
    for prefecture, statistic in statistique.items():
        print("\nPréfecture: {}".format(prefecture ))
        print("Nombre Total des cas: {}".format(statistic['total_cas']))
        print("Nombre Total des décès: {}".format(statistic['total_deces']))
        print(f"Taux de mortalité: {statistic['taux_mortalite']*100:.1f}%")

    # Création des visualisations
    nb_total_cas_par_prefecture(statistique)
    taux_mortalite_par_prefecture(statistique)

if __name__ == "__main__":
    main()