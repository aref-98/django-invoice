import requests
import random

BASE_URL = "http://localhost:8000/api"

persons = [
    {"name": "ITnetwork s.r.o.", "identificationNumber": "05861381", "taxNumber": "CZ05861381", "accountNumber": "123456789", "bankCode": "5500", "iban": "CZ000123456789", "telephone": "+420 123 123 123", "mail": "redakce@itnetwork.cz", "street": "Karlovo náměstí 290/16", "zip": "120 00", "city": "Praha", "country": "CZECHIA", "note": "Největší IT akademie v Česku."},
    {"name": "Jan Novák", "identificationNumber": "12345678", "taxNumber": "CZ12345678", "accountNumber": "987654321", "bankCode": "0300", "iban": "CZ001987654321", "telephone": "+420 777 111 222", "mail": "jan.novak@gmail.com", "street": "Hlavní 1", "zip": "110 00", "city": "Praha", "country": "CZECHIA", "note": ""},
    {"name": "Eva Svobodová", "identificationNumber": "87654321", "taxNumber": "CZ87654321", "accountNumber": "111222333", "bankCode": "0100", "iban": "CZ002111222333", "telephone": "+420 606 222 333", "mail": "eva.svobodova@seznam.cz", "street": "Nová 5", "zip": "602 00", "city": "Brno", "country": "CZECHIA", "note": ""},
    {"name": "Petr Černý s.r.o.", "identificationNumber": "11223344", "taxNumber": "CZ11223344", "accountNumber": "444555666", "bankCode": "2010", "iban": "CZ003444555666", "telephone": "+420 733 444 555", "mail": "info@cerny.cz", "street": "Průmyslová 10", "zip": "301 00", "city": "Plzeň", "country": "CZECHIA", "note": "Stavební firma"},
    {"name": "Marie Horáková", "identificationNumber": "22334455", "taxNumber": "CZ22334455", "accountNumber": "777888999", "bankCode": "0600", "iban": "CZ004777888999", "telephone": "+420 605 333 444", "mail": "marie.horakova@email.cz", "street": "Lipová 3", "zip": "400 01", "city": "Ústí nad Labem", "country": "CZECHIA", "note": "Účetní služby"},
    {"name": "Tomáš Dvořák", "identificationNumber": "33445566", "taxNumber": "CZ33445566", "accountNumber": "123987456", "bankCode": "0800", "iban": "CZ005123987456", "telephone": "+420 724 555 666", "mail": "tomas.dvorak@dvorak.cz", "street": "Horní 7", "zip": "500 02", "city": "Hradec Králové", "country": "CZECHIA", "note": "IT konzultant"},
    {"name": "Lucie Marková s.r.o.", "identificationNumber": "44556677", "taxNumber": "CZ44556677", "accountNumber": "321654987", "bankCode": "5500", "iban": "CZ006321654987", "telephone": "+420 731 666 777", "mail": "info@markova.cz", "street": "Střední 15", "zip": "370 01", "city": "České Budějovice", "country": "CZECHIA", "note": "Marketing"},
    {"name": "Pavel Krejčí", "identificationNumber": "55667788", "taxNumber": "CZ55667788", "accountNumber": "456123789", "bankCode": "0300", "iban": "CZ007456123789", "telephone": "+420 608 777 888", "mail": "pavel.krejci@krejci.cz", "street": "Dolní 22", "zip": "460 01", "city": "Liberec", "country": "CZECHIA", "note": "Grafický designer"},
    {"name": "Jana Procházková", "identificationNumber": "66778899", "taxNumber": "CZ66778899", "accountNumber": "789456123", "bankCode": "0100", "iban": "CZ008789456123", "telephone": "+420 776 888 999", "mail": "jana.prochazkova@gmail.com", "street": "Zahradní 8", "zip": "586 01", "city": "Jihlava", "country": "CZECHIA", "note": ""},
    {"name": "Martin Blaha s.r.o.", "identificationNumber": "77889900", "taxNumber": "CZ77889900", "accountNumber": "654789321", "bankCode": "2010", "iban": "CZ009654789321", "telephone": "+420 602 999 001", "mail": "info@blaha.cz", "street": "Nádražní 33", "zip": "771 00", "city": "Olomouc", "country": "CZECHIA", "note": "Dopravní firma"},
    {"name": "Kateřina Nováková", "identificationNumber": "88990011", "taxNumber": "CZ88990011", "accountNumber": "321789654", "bankCode": "0800", "iban": "CZ010321789654", "telephone": "+420 737 001 002", "mail": "katerina.novakova@seznam.cz", "street": "Polní 44", "zip": "746 01", "city": "Opava", "country": "CZECHIA", "note": "Překladatelka"},
    {"name": "Jiří Pospíšil", "identificationNumber": "99001122", "taxNumber": "CZ99001122", "accountNumber": "987321654", "bankCode": "0600", "iban": "CZ011987321654", "telephone": "+420 603 002 003", "mail": "jiri.pospisil@pospisil.cz", "street": "Lesní 2", "zip": "360 01", "city": "Karlovy Vary", "country": "CZECHIA", "note": "Fotograf"},
    {"name": "Alena Kratochvílová", "identificationNumber": "10112233", "taxNumber": "CZ10112233", "accountNumber": "147258369", "bankCode": "5500", "iban": "CZ012147258369", "telephone": "+420 721 003 004", "mail": "alena.kratochvilova@email.cz", "street": "Slunečná 11", "zip": "530 02", "city": "Pardubice", "country": "CZECHIA", "note": ""},
    {"name": "Ondřej Šimánek s.r.o.", "identificationNumber": "20223344", "taxNumber": "CZ20223344", "accountNumber": "369258147", "bankCode": "0300", "iban": "CZ013369258147", "telephone": "+420 775 004 005", "mail": "info@simanek.cz", "street": "Komenského 9", "zip": "669 02", "city": "Znojmo", "country": "CZECHIA", "note": "Advokátní kancelář"},
    {"name": "Veronika Horáčková", "identificationNumber": "30334455", "taxNumber": "CZ30334455", "accountNumber": "258147369", "bankCode": "0100", "iban": "CZ014258147369", "telephone": "+420 604 005 006", "mail": "veronika.horackova@gmail.com", "street": "Mánesova 6", "zip": "700 30", "city": "Ostrava", "country": "CZECHIA", "note": "Copywriter"},
]

# Vytvoření osob
person_ids = []
for person in persons:
    r = requests.post(f"{BASE_URL}/persons", json=person)
    person_ids.append(r.json()["_id"])
    print(f"Vytvořena osoba: {person['name']} (ID: {r.json()['_id']})")

# Vytvoření 30 faktur
products = ["Článek", "Webová stránka", "Konzultace", "Vývoj aplikace", "Grafika", "SEO optimalizace", "Účetnictví", "Překlad", "Fotografie", "Právní poradenství"]
for i in range(1, 31):
    invoice = {
        "invoiceNumber": 2024000 + i,
        "issued": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "dueDate": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "product": random.choice(products),
        "price": random.randint(100, 50000),
        "vat": 21,
        "note": f"Testovací faktura č. {i}",
        "buyerId": random.choice(person_ids),
        "sellerId": random.choice(person_ids),
    }
    r = requests.post(f"{BASE_URL}/invoices", json=invoice)
    print(f"Vytvořena faktura č. {i} (ID: {r.json()['id']})")

print("Hotovo!")