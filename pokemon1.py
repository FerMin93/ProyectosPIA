import requests

#America Fernanda Martinez Barron
#1901395

if __name__ == '__main_':
	url = 'https://pokeapi.co/api/v2/pokemon-form/'
	
	response = requests.get(url)
	if response.status_code == 200:
		payload = response.json()
		results = payload.get('results',[])
		
		if results:
			for pokemon in results:
				name = pokemon['name']
				print(name)