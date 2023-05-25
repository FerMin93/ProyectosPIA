#America Fernanda Martinez Barron 
#1901395
import base64
#
## Obtenemos un frase desde el input principal.
#
print ('Bienvenidos a codificadorBase64 en Python')
frase = input('Proporciona una frase para codificar: ')
#
## Obtenemos los bytes de la frase
#
frase_bytes = frase.encode('ascii')
#
## Se calculan los bytes en base64
#
base64_bytes = base64.b64encode(frase_bytes)
#
## Segenera mensaje en base64
#
base64_message = base64_bytes.decode('ascii')
print ('La frase codificada en Base 64 en :')
print(base64_message)