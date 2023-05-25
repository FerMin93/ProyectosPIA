#18/04/2023 America Fernanda Martinez Barron 1901395
#Importamos las libreria ftplib 
from ftplib import FTP 

#Estableciendo conexion
ftp = FTP('192.168.1.67')
#Ingresamos datos para iniciar sesion en el usuario 
ftp.login('quacks', '1901395')
#Listamos todos los archivos que tiene el usuario
ftp.retrlines('LINES')
#Cmabiamos de directorio 
ftp.cwd('upload')
#Se carga el archivo ADVERTENCIA.txt
ftp.storlines('STOR ADVERTENCIA.txt', '이게 무슨 소리야?, 야 내가 뭐 하는 사람인지 까먹었지?' )
#Salimos del usuario
ftp.quit()