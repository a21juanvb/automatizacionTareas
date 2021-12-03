import requests

import backup
#from backup import backuptoZip



#función para leer el archivo flow.txt
def procesar_data(d):
    resultado = None
    if d is not None:
        datos = d.split('|')
        operador = datos[0]
        comando1 = datos[1]
        comando2 = datos[2]

        resultado = operador, comando1, comando2
    return resultado

#Recuperamos los datos
if __name__ == '__main__':
    #tomamos el archivo de un repositorio
    res = requests.get('https://gitlab.iessanclemente.net/abautis/seminarioautomatizacion/-/raw/main/flow.txt?inline=false')
    #llamamos a la funcion que lee el archivo y lo devolvemos en datos
    datos = procesar_data(res.text)
    #rompemos otra vez para ver si ejecutamos ono
    isBackup = datos[1].split(':')[1]
    isSent = datos[2].split(':')[1]
    #imprimimos las acciones detectadas
    print("backup: ", isBackup)
    print("sent: ", isSent)

    if int(isBackup) == 1:
        backup.backuptoZip('data')
    else:
        print('El proceso de copia de seguridad esta deshabilitado')




