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

        form_data = {'ctf':valeurs_concatenees}

        form = soup.find('form')
        if form:
            form_action = form.get('action', '')
            form_method = form.get('method', 'post')

            form_action_url = f"{url.rstrip('/')}/{form_action.lstrip('/')}"

            if form_method.lower() == 'post':
                post_response = requests.post(form_action_url, data=form_data)

                if post_response.status_code == 200:
                    print("Flag successfully posted for checking.")
                else:
                    print(f"Failed to post flag. Status code: {post_response.status_code}")
            else:
                print("Form method is not POST.")
            
            # Vérifie si la requête a réussi (statut 200)
        if post_response.status_code == 200:
            # Utilise une expression régulière pour extraire les lettres ou chiffres entre deux caractères "#"
            pattern = r'#([A-Za-z0-9]+)#'
            
            # Recherche toutes les occurrences dans le contenu de la page
            resultats = re.findall(pattern, post_response.text)
            
            # Affiche les résultats trouvés
            valeurs_concatenees_hash = ''.join(resultats)
            print(valeurs_concatenees_hash)
        else:
            print(f"Échec de la requête. Statut de la requête : {post_response.status_code}")
    else:
        print(f"Échec de la requête. Statut de la requête : {response.status_code}")

url_a_analyser = 'http://92.205.177.169:83' 
recupere_donnees(url_a_analyser)
