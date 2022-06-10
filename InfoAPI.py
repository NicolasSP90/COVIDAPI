import requests
import json
import MainInformationAPI as Miapi

# lista paises
urlcountries = "https://covid-193.p.rapidapi.com/countries"

# estatísticas de um pais
urlstatistics = "https://covid-193.p.rapidapi.com/statistics"
urlhistory = "https://covid-193.p.rapidapi.com/history"
country = "usa"

# pesquisa se pais existe
querycountry = {"search": str(country)}

# estatística de um pais no dia
querystatistics = {"country": str(country)}
day = "02"
month = "06"
year = "2020"
queryhistory = {"country": str(country), "day": str(year) + "-" + str(month) + "-" + str(day)}

# info API
headers = {
	"X-RapidAPI-Host": str(Miapi.xRapidAPIHost),
	"X-RapidAPI-Key": str(Miapi.xRapidAPIKey)
}

# info requests
url = str(urlcountries)
query = None
response = requests.request("GET", str(url), headers=headers, params=query)

print(response.text)
resultado = json.loads(response.text)
