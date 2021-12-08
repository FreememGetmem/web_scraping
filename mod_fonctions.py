import datetime
import pandas as pd
from bs4 import BeautifulSoup
import os
from mod_db import trade_db


def getUrlsToScrap(path):
    htmlfiles = [os.path.join(root, name)
                 for root, dirs, files in os.walk(path)
                 for name in files
                 if name.endswith(("Stocks.html"))]
    return htmlfiles


def scrapByUrl(tag1, tag2, trade):
    """
    il reçoit deux tags (structure html dont zone et table) ou sont stockés les données du fichier html
    ceci lui permet alors d'initialiser l'objet Trade() avec ses différents propriétés.
    :param tag1: pays_table
    :param tag2: zone
    :param trade: objet de l'étude
    :return: none
    """
    zone = tag2.select("a.hover-link.link.tab__link.selected")[0].text
    for val in tag1:
        for nation in val:
            if nation.text.strip() != '':
                data = nation.text.strip().split('      ')
                pays_row = data[0]
                pays = pays_row.split('     ')[0]
                infos = data[1:len(data)]
                for info in infos:
                    data_infos = info.strip().split('    ')
                    stock = data_infos[0]
                    if len(data_infos) == 1:
                        listAppendEmpty(trade)
                    else:
                        valeur = data_infos[1].split()
                        listAppendNotEmpty(trade, valeur)

                    trade.zone.append(zone)
                    trade.pays.append(pays)
                    trade.stock.append(stock)
                    trade.date.append(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))


def listAppendNotEmpty(trade, valeur):
    """
    Cette méthode met à jour la liste de Trade avec des valeurs correspondants
    :param trade:
    :param valeur:
    :return: none
    """
    trade.value.append(valeur[0])
    trade.netchange.append(valeur[1])
    trade.perchange.append(valeur[2])
    trade.month.append(valeur[3])
    trade.year.append(valeur[4])
    trade.edt.append(valeur[5])


def listAppendEmpty(trade):
    """
    Cette méthodee met à jour la liste de Trade avec des valeurs vides
    :param trade:
    :return: none
    """
    trade.value.append('--')
    trade.netchange.append('--')
    trade.perchange.append('--')
    trade.month.append('--')
    trade.year.append('--')
    trade.edt.append('--')


def getContent(url):
    """
    Apartir de l'url (repertoire en dure) reçu il lit le contenu html et retourne un fichier
    :param url: url
    :return: content
    """
    with open(url, 'r', encoding="ISO-8859-1") as file:
        content = file.read()
    return content


def scrapAllUrl(urls, trade):
    """
    Il parcours la liste d'url reçu et fait appel à la méthode scrapByUrl()
    pour chaque fichier
    :param urls:
    :return: none
    """
    for url in urls:
        soup = BeautifulSoup(getContent(url), 'lxml')
        pays_tables = soup.find_all('div', class_="data-tables")
        zone = soup.find('div', class_="section-tabs")
        scrapByUrl(pays_tables, zone, trade)


def getDataFrame(trade):
    """
    Cette méthode reçoit en argument un objet Trade pour créer un DataFrame en
    l'initialisant avec ce même objet
    :param trade:
    :return: un DataFrame
    """
    df = pd.DataFrame({
        "Zone": trade.zone,
        "Pays": trade.pays,
        "NomStocks": trade.stock,
        "Value": trade.value,
        "NetChange": trade.netchange,
        "PercenterChange": trade.perchange,
        "1Month": trade.month,
        "1Year": trade.year,
        "timeEDT": trade.edt,
        "DateScraping": trade.date
    })

    return df


def menu():
    print('''
                ************ MENU D'EXECUTION *************
            1 - Pour lancer le programme de web scraping
            2 - Pour afficher les données obtenues après le scraping via un DataFrame
            3 - pour insérer les données dans la bd MongoDB: BD (db) et TABLE(stock) 
            4 - Pour afficher les données depuis la BD MongoDB
            5 - Pour afficher les informations de la zone Americas
            6 - Pour afficher les informations de la zone EMEA
            7 - Pour afficher les informations de la zone APAC
            8 - Pour afficher les informations pour le stock BBG US REITS
            9 - Pour quitter le programme
            ''')

def clear():
    clearConsole = lambda: print('\n' * 150)
    clearConsole()
