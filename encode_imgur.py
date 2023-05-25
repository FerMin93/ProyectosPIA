#America Fernanda Martinez Barron 
#1901395
import requests
import base64 
from requests import Response
#
## Para descargar la imagen del sitio
#
if __name__ == '__main__':
    url = 'https://i.imgur.com/uvFEcJN.jpeg'

    Response: Response = requests.get(url, stream=True)
    with open('uvFEcJN.jpeg','wb') as file_down:
        for chunk in Response.iter_content(): #Descargando contenido poco a poco 
            file_down.write(chunk)
        Response.close()
    #
    ## Para codificar la imagen
    #
    with open('uvFEcJN.jpeg','rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf8')

        print(base64_message)