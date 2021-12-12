import os
import zipfile

def backuptoZip(folder):
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    #xeramos  un arquivo .zip co nome obtido e verificado no paso anterior
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    #Imkos recorrer a árbore de directorio e arquivos para facer a copia
    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Fin del proceso')
