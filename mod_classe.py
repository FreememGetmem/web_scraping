
class Trade:
    '''
    Classe Trade qui va instancier l'objet stock avec les propriétés suivantes:
    zone: Amérique ou EMEA(Europe Africa Midle East) ou APAC (Asia Pacifique)
    pays: les pays représentés
    stock: nom des stock étudiés
    value: valeur du change
    Net Change:
    Percenter Change:
    1 Month:
    1 Year:
    EDT Time: l'heure d'évaluation des valeurs des stock
    '''
    def __init__(self, zone, pays, stock,value, netchange, perchange, month, year,edt, date ):
        self.zone = zone
        self.pays = pays
        self.stock = stock
        self.value = value
        self.netchange = netchange
        self.perchange = perchange
        self.month = month
        self.year = year
        self.edt = edt
        self.date = date

    def __str__(self):
        return "{} {} {} {} {} {} {} {} ".format(self.zone, self.pays, self.stock,self.value, self.netchange, self.perchange, self.month, self.year,self.edt, self.date)



