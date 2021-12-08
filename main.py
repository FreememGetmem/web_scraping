import mod_headers
import pandas as pd

from mod_classe import Trade
from mod_fonctions import scrapAllUrl, getDataFrame, getUrlsToScrap, menu, clear
from mod_db import insertDataFrameToDB, afficheDataFromMongoDb


def main():
    path = "bloomberg"
    urls = getUrlsToScrap(path)

    # ['bloomberg/1/American-Stocks.html', 'bloomberg/2/American-Stocks.html', 'bloomberg/3/American-Stocks.html',
    #  'bloomberg/4/American-Stocks.html', 'bloomberg/5/American-Stocks.html', 'bloomberg/6/American-Stocks.html',
    #  'bloomberg/1/EMEA-Stocks.html', 'bloomberg/2/EMEA-Stocks.html', 'bloomberg/3/EMEA-Stocks.html',
    #  'bloomberg/4/EMEA-Stocks.html', 'bloomberg/5/EMEA-Stocks.html', 'bloomberg/6/EMEA-Stocks.html',
    #  'bloomberg/1/APAC-Stocks.html', 'bloomberg/2/APAC-Stocks.html', 'bloomberg/3/APAC-Stocks.html',
    #  'bloomberg/4/APAC-Stocks.html', 'bloomberg/5/APAC-Stocks.html', 'bloomberg/6/APAC-Stocks.html']

    headers = mod_headers.headers
    list_zone = []
    list_pays = []
    list_trade = []
    list_value = []
    list_net_change = []
    list_change = []
    list_month = []
    list_year = []
    list_edt = []
    list_date = []

    stock = Trade(list_zone, list_pays, list_trade, list_value, list_net_change, list_change, list_month, list_year,
                  list_edt, list_date)

    def userMenu():
        menu()
        reply = True
        while reply:
            local = int(input("Lisez le menu et exécuter le programme: "))
            if local == 1:
                scrapAllUrl(urls, stock)
                print("Programme de scraping exécuté avec succès sur le site de Bloomberg!")
            elif local == 2:
                clear()
                df = getDataFrame(stock)
                pd.set_option('display.max_columns', 10)
                print(df)
                menu()
            elif local == 3:
                insertDataFrameToDB(df.to_dict("records"))
                print("Les données scrapées ont été insérés avec succès sur la base MongoDB !")
            elif local == 4:
                clear()
                criteria = ''
                champs = ['Zone', 'Pays', 'NomStocks', 'Value', 'NetChange', 'NetChange', 'PercenterChange', '1Month',
                          '1Year', 'timeEDT', 'DateScraping']
                result = afficheDataFromMongoDb(criteria, champs)
                print(result)
                menu()
            elif local == 5:
                clear()
                criteria = {"Zone": ' Americas '}
                champs = ['Zone', 'Pays', 'NomStocks', 'Value', 'NetChange', 'NetChange', 'PercenterChange', '1Month',
                          '1Year', 'timeEDT', 'DateScraping']
                result = afficheDataFromMongoDb(criteria, champs)
                print(result)
                menu()
            elif local == 6:
                clear()
                criteria = {"Zone": ' EMEA '}
                champs = ['Zone', 'Pays', 'NomStocks', 'Value', 'NetChange', 'NetChange', 'PercenterChange', '1Month',
                          '1Year', 'timeEDT', 'DateScraping']
                result = afficheDataFromMongoDb(criteria, champs)
                print(result)
                menu()
            elif local == 7:
                clear()
                criteria = {"Zone": ' APAC '}
                champs = ['Zone', 'Pays', 'NomStocks', 'Value', 'NetChange', 'NetChange', 'PercenterChange', '1Month',
                          '1Year', 'timeEDT', 'DateScraping']
                result = afficheDataFromMongoDb(criteria, champs)
                print(result)
                menu()
            elif local == 8:
                clear()
                criteria = {"NomStocks": 'BBREIT:IND   BBG US REITS'}
                champs = ['Zone', 'Pays', 'NomStocks', 'Value', 'NetChange', 'NetChange', 'PercenterChange', '1Month',
                          '1Year', 'timeEDT', 'DateScraping']
                result = afficheDataFromMongoDb(criteria, champs)
                print(result)
                menu()
            else:
                print("Fin de l'exécution du programme.....")
                reply = False



    userMenu()







    # Cruseur pour la reqête
    # criteria = {"Pays": 'United States'}


main()