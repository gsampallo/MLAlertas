import requests
import re
from bs4 import BeautifulSoup
import io
import json
import os
from pushbullet import Pushbullet

class MLAlertas:

    def __init__(self):
        
        self.loadParameters()
        print(self.__parameters["URL"])
        self.queryCount()

        if(self.__nuevaCantidad > self.__cantidad):
            print("Uno mas")
            self.sendAlert()           
        
        self.saveParameters()


    def loadParameters(self):
        __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.filename = __location__+'/config.json'
        
        if(os.path.exists(self.filename)):
            with open(self.filename) as f:
                self.__parameters = json.load(f)
                self.__cantidad = int(self.__parameters["cantidad"]);
            f.close()
        else:
            print("No existe el archivo de parametros")
            print("Cree el archivo config.json")
            exit()

    @property
    def cantidad(self):
        return self.__cantidad;

    def queryCount(self):
        page = requests.get(self.__parameters["URL"])
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('div', class_='item-conditions')
        rs = re.findall("[0-9]*", str(results))
        while '' in rs:
            rs.remove('')
        print(rs[0])
        self.__nuevaCantidad = int(rs[0])

    def saveParameters(self):
        self.__parameters["cantidad"] = self.__nuevaCantidad
        with open(self.filename, "w") as jsonFile:
            json.dump(self.__parameters, jsonFile)
        jsonFile.close()

    def sendAlert(self):
        pb = Pushbullet(self.__parameters["APIKEY"])

        valor = self.__nuevaCantidad - self.__cantidad

        push = pb.push_note('+'+str(valor)+' - Se vendieron en total '+str(self.__nuevaCantidad)+' de libros', "Aviso de Productos")

if __name__ == "__main__":

    alertas = MLAlertas()

