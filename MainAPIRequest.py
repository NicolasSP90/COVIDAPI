import MainInformationAPI as Miapi
import json
import requests

class APIRequest:
    @staticmethod
    def requesturl(link, info):

        # Cabeçalho da requisição
        headers = {
            "X-RapidAPI-Host": str(Miapi.xRapidAPIHost),
            "X-RapidAPI-Key": str(Miapi.xRapidAPIKey)
        }

        # Tipo de requisição
        if info is None:
            request = requests.request("GET", link, headers=headers)
            resp = json.loads(request.text)
        else:
            request = requests.request("GET", link, headers=headers, params=info)
            resp = json.loads(request.text)

        # Resposta da requisição
        return resp