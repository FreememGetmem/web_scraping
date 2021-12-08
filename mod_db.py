from pymongo import MongoClient
import pandas as pd

#Créer le client MongoDB
client = MongoClient('localhost', 27017)
#BD Mongo
trade_db= client.db.stock

#Inserer Donnee
def insertDataFrameToDB(dataframe):
    '''
    Insertion de la dataframe vers la base MongoDB
    :param dataframe:
    :return: none
    '''
    trade_db.insert_many(dataframe)


#Afficher Donnee
def afficheDataFromMongoDb(criteria, champs):
    '''
    Cruseur pour la reqête de selection
    :return: result
    '''
    if criteria == '':
        curseur = trade_db.find()
    else:
        curseur = trade_db.find(criteria)
    result = pd.DataFrame(list(curseur), columns=champs)

    return result

#Enlever Collection
def dropCollectionMongoDb():
    '''
      Drop collection for Test Purpose
    '''
    print(client.db.list_collection_names())  # Return a list of collections in 'testdb1'
    if "stock" in client.db.list_collection_names():
        collection = client.db["stock"]
        collection.drop()

dropCollectionMongoDb()