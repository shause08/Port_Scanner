import requests
from bs4 import BeautifulSoup, Comment
import re

def recupere_donnees(url):
    # Envoie une requête HTTP pour récupérer le contenu de la page web
    response = requests.get(url)
    
    # Vérifie si la requête a réussi (statut 200)
    if response.status_code == 200:
        # Analyse le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trouve tous les commentaires dans le code source
        commentaires = soup.find_all(string=lambda text: isinstance(text, Comment))
        
        # Utilise une expression régulière pour extraire la première lettre ou le premier chiffre après les deux-points dans les commentaires
        pattern = r':[^\s]*[A-Za-z0-9]'
        
        # Concatène les premières lettres ou chiffres trouvés dans les commentaires
        valeurs_concatenees = ""
        for commentaire in commentaires:
            resultats = re.findall(pattern, commentaire)
            for resultat in resultats:
                # Supprime le caractère ':' du début de chaque résultat
                valeur = resultat[1:]
                valeurs_concatenees += valeur
                
        print(valeurs_concatenees)
    else:
        print(f"Échec de la requête. Statut de la requête : {response.status_code}")

# Remplacez l'URL par celle de la page que vous souhaitez analyser
url_a_analyser = 'http://92.205.177.169:83'
recupere_donnees(url_a_analyser)
