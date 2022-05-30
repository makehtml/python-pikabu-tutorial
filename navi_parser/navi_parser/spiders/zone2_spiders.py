import requests


url = 'https://gan.shom.fr/navarea/NavareaIIenVigueur.txt'
params = {'title': 'navarea', 'id'= 'id', 'date': 'date', 'area':'area', 'description': 'description'}
response = requests.get(url,params = params)
response.json