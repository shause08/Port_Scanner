import requests
from bs4 import BeautifulSoup, Comment
import re

def recupere_donnees(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        commentaires = soup.find_all(string=lambda text: isinstance(text, Comment))
        
        pattern = r':[^\s]*[A-Za-z0-9]'
        
        valeurs_concatenees = ""
        for commentaire in commentaires:
            resultats = re.findall(pattern, commentaire)
            for resultat in resultats:
                valeur = resultat[1:]
                valeurs_concatenees += valeur
                
        print(valeurs_concatenees)
    else:
        print(f"Échec de la requête. Statut de la requête : {response.status_code}")

url_a_analyser = 'http://92.205.177.169:83'
recupere_donnees(url_a_analyser)
