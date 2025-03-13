            #Exo2:
import random

class Personne:
    def __init__(self, nom, sante="saine", proba_infection=0.3):
        self.nom = nom
        self.sante = sante
        self.proba_infection = proba_infection

    def contact(self, autre_personne):
        """
        Simule un contact avec une autre personne.
        Si l'autre est infectée, possibilité de transmission.
        """
        if autre_personne.sante == "infectee" and self.sante == "saine":
            if random.random() < self.proba_infection:
                self.sante = "infectee"

class Population:
    def __init__(self, personnes):
        self.personnes = personnes

    def simuler_jour(self):
        """
        Simule une journée de contacts aléatoires.
        """
        # Sélection aléatoire de paires de personnes
        for personne in self.personnes:
            if personne.sante == "infectee":
                # Choisir une personne aléatoire à infecter
                autre = random.choice(self.personnes)
                autre.contact(personne)
    
    def statut_epidemie(self):
        """
        Retourne le nombre de personnes dans chaque état.
        """
        stats = {"saine": 0, "infectee": 0, "immunisée": 0}
        for p in self.personnes:
            stats[p.sante] += 1
        return stats

# Exemple d'utilisation
if __name__ == "__main__":
    # Créer une population de 10 personnes
    personnes = [Personne(f"Personne_{i}") for i in range(10)]
    # Infecter une personne au hasard
    personnes[0].sante = "infectee"
    population = Population(personnes)

    # Simulation sur 5 jours
    for jour in range(5):
        population.simuler_jour()
        print(f"Jour {jour + 1}: {population.statut_epidemie()}")
# %%
