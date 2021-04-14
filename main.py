import email as Email
import csv
#Programa principal
if __name__ == '__main__':
    cont = [0]
    archivo = open('Emails.csv')
    reader = csv.reader(archivo, delimiter=';')
    email = Email.Email()   #se crea un objeto de la clase Email
    nombre = input('Nombre: ')  #nombre del usuario
    correo = input('Correo: ')  #correo del usuario
    password = input('Contraseña: ')    #contraseña del correo
    email.crearCuenta(correo, password) #se crea la cuenta
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, email.retornaEmail()))
    #cambio de contraseña
    print('CAMBIO DE CONTRASEÑA'); print('¿Desea cambiar la contraseña?')
    if(input('si o no: ') == 'si'):
        if(input('Ingrese la contraseña anterior: ') == email.getPassword()):
            password = input('Contraseña nueva: ')
            email.newPassword(password)  # se cambia la contraseña
            print('DATO: se cambió con éxito la contraseña')
        else:
            print('ERROR: la contraseña ingresada es incorrecta')
    #crear otro objeto de la clase Email
    print('CREAR OBJETO DE LA CLASE EMAIL')
    correo = input('Correo: ')
    password = input('Contraseña: ')
    email.crearCuenta(correo, password)
    #leer lista
    print('LISTA DE DOMINIOS DE CORREOS')
    dominio = input('Ingrese dominio a buscar: ')
    for fila in reader:
        for columna in range(len(fila)):
            correo = fila[columna]
            if(email.getDominio(correo) == dominio):
                cont[0]+=1
    print('Correos con el dominio "{}": {}'.format(dominio, cont[0]))
    archivo.close()
