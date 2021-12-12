import requests

import backup




#función de lectura do archivo de control de operacións (flow.txt)
def procesar_datos(flow):
    resultado = None
    if flow is not None:
        datos = flow.split('|')
        operador = datos[0]
        comando1 = datos[1]
        comando2 = datos[2]
        pin = datos[3]

        resultado = operador, comando1, comando2, pin
    return resultado

# Parte que procesa a recuperación dos datos
if __name__ == '__main__':
    #o arquivo de control está nun repositorio de github
    secuencia = requests.get('https://github.com/a21juanvb/automatizacionTareas/blob/master/flow.txt')
    datos = procesar_datos(secuencia.text)
    # recortamos os datos para obter as distintas cadeas de instrucións e clave
    clave = datos[3].split(':')[1]
    isBackup = datos[1].split(':')[1]

    if clave != '12345':
        print('Non se pode procesar a orde, dado que a clave non concorda coa anotación de control')
    else:
        print("backup: ", isBackup)
        if int(isBackup) == 1:
            backup.backuptoZip('data')
        else:
            print('Active o servizo de backup, neste momento está deshabilitado')