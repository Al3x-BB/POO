#Clase Email
import re
class Email:
    #atributos de la clase
    __idDominio = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''
    #operaciones de la clase
    def __init__(self, idDominio = '', dominio = '', tipoDominio = '', password = ''):
        self.__idDominio = idDominio
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__password = password
    def retornaEmail(self):
        if (self.__idDominio == '' or self.__dominio =='' or self.__tipoDominio == ''):
            correo = 'ERROR'
        else:
            correo = "%s@%s.%s"%(self.__idDominio, self.__dominio,self.__tipoDominio)
        return correo
    def getDominio(self, correo): #para el inciso 4
        l1 = correo.split('@', 1)   #divide el correo en dos (idDominio y (dominio con tipoDominio))
        l2 = l1[1].split('.', 1)    #divide el el sobrente y se obtiene el dominio y el tipoDominio
        return l2[0]    #devuelve el dominio del correo
    def crearCuenta(self, correo, password): #rehacer
        if(re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower())):
            print('DATO: correo ingresado es válido')
            l1 = correo.split('@',1)    #divide el correo en dos (idDominio y (dominio con tipoDominio))
            l2 = l1[1].split('.', 1)    #divide el el sobrente y se obtiene el dominio y el tipoDominio
            self.__idDominio = l1[0]
            self.__dominio = l2[0]
            self.__tipoDominio = l2[1]
            self.__password = password
        else:
            print('ERROR: correo ingresado es incorrecto')
    def getPassword(self): #devuelve la contraseña
        return self.__password
    def newPassword(self, password):  #permite cambiar la contraseña
        self.__password = password
