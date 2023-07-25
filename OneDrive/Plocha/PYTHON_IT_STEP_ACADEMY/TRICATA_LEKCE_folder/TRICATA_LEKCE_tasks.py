'''
DJANGO a FLASK - Úvod, ARCHITEKTRUA WEBOVÝCH APLIKACÍ

pip list == po zadání v CDM mi vyjede, vše co mám nainstalováno v daném projektu jako python, flask apod.

ARCHITEKTURA
- frontend, backend
FRONTEND
- jak to vypadá

BACKEND
- práce s procesy
- databáze

- komunikují mezi sebou metodami GET a POST - ty jsou nejpoužívanějsí
- je jich ale 11
- nejčastější je ale GET a POST
- GET je od serveru pro uživatele, uživatel cche něco získat
- POST uživatel něco posílá, např. odesílá heslo
- pak je ještě třeba PUT a DELETE ale ty nejsou tak důležité?



FLASK
- na začátku dáme "from flask import Flask"
-  spouštím v CMD'flask run' 
- POZOR! nesouvisí přímo s FLASKEM, ale if __name__ == "__main__" --> pokud se spouští soubor name a zavolá se vše, co je v daném IFU
- pokud vytvoříme FLASKOVOU aplikaci, tak musíme dát na začátek jménoapp = Flask()
- zjistit více o "app.run(debug=True)" ??
- přes decorátor @názevaplikace.route("/") --> spojuje to route a funkcionalitu
    - lomítko je signál pro přidání funkcionality
    - za lomítkem pak musí být název, kde se stránka/aplikace spustí
    - můžeme tam dávat ale i funkce kdy do ('/user/<username>') přidávám např. jméno
        - username pak přidám níže do aplikace
    -route zpracovává requesty GET by default
    - pokud chceme řešit POST tak jde přes POSTMANA
    -  

PORT
- local host - je to IP našeho počítače, 127.00.01 apod. je to když jsme třeba spiuštěli html weby apod.
- na konci čísla je port, můžu změnit v kodu

JINJA2
- template do Flasku na HTML
'''
