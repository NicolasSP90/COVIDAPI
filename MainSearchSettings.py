from MainAPIRequest import APIRequest
from MainSpreadsheet import XLSX

class SearchSettings:
    @staticmethod
    def menunumber(number):

        # Limpa a variável.
        query = None

        # Pesquisa por país ou termo
        if number == int(1):

            # Configurações de pesquisa
            querycountry = input("\nInsira o país ou termo para pesquisa e pressione ENTER;"
                          "\nPara listar todos os paises deixe o campo em branco e pressione ENTER;\n")
            query = {"search": querycountry}
            url = "https://covid-193.p.rapidapi.com/countries"

            # Ajuste de parâmetros, se necessário
            if len(query["search"]) == 0:
                query = None

            # Requisição
            req = APIRequest.requesturl(url, query)

            # Pesquisa sem erros
            if req["errors"] == []:
                print("\nForam encontrados ", req["results"], " paises.")
                count = 1
                for countrylisted in req["response"]:
                    print(count, "- ", countrylisted)
                    count += 1

                # Exportar resultados
                XLSX.createspreadsheet(number, req)

            # Pesquisa com erros
            else:
                print("Problemas encontrados nos parâmetros."
                      "\nVerifique a ortografia(paises em inglês) e se o problema persistir informe o suporte técnico\n")
                exit()

        # Pesquisa por dados atuais
        elif number == int(2):

            # Configurações de pesquisa
            querycountry = input(
                "\nInsira o país para pesquisa ou pressione ENTER para listar os dados de todos os paises registrados."
                "\nEm caso de dúvidas verifique os paises listados na API no menu principal: ")
            query = {"country": str(querycountry)}
            url = "https://covid-193.p.rapidapi.com/statistics"

            # Ajuste de parâmetros, se necessário
            if len(query["country"]) == 0:
                query = None

            # Requisição
            req = APIRequest.requesturl(url, query)

            # Pesquisa com erros nos parâmetros inseridos
            if not len(req["errors"]) == 0:
                for errors in req["errors"]:
                    print(req["errors"][errors])
                print("\nRevise os parâmetros e tente novamente.")

            # Pesquisa sem erros
            else:

                # Nenhum país encontrado
                if req["results"] == 0:
                    print("Nenhum país encontrado."
                          "\nVerifique a ortografia inserida ou confirme o nome na lista de paises registrados.\n")

                # Dados dos países encontrados
                else:
                    results = 0
                    while results < int(req["results"]):
                        print("País: " + str(req["response"][results]["country"]))
                        print("Casos confirmados: " + str(req["response"][results]["cases"]["total"]))
                        print("Casos ativos: " + str(req["response"][results]["cases"]["active"]))
                        print("Casos críticos: " + str(req["response"][results]["cases"]["critical"]))
                        print("Casos recuperados: " + str(req["response"][results]["cases"]["recovered"]))
                        print("Casos novos: " + str(req["response"][results]["cases"]["new"]))
                        print("Casos por milhão: " + str(req["response"][results]["cases"]["1M_pop"]))
                        print("Total de Mortos: " + str(req["response"][results]["deaths"]["total"]))
                        print("Novas mortes: " + str(req["response"][results]["deaths"]["new"]))
                        print("Mortes por milhão: " + str(req["response"][results]["deaths"]["1M_pop"]))
                        print("Testes realizados: " + str(req["response"][results]["tests"]["total"]))
                        print("Testes por milhão: " + str(req["response"][results]["tests"]["1M_pop"]) + "\n")
                        results += 1

                    # Exportar resultados
                    XLSX.createspreadsheet(number, req)

        # Pesquisa por dados no histórico
        else:

            # Configurações de pesquisa
            querycountry = input("\nInsira o país para pesquisa. Para dados GLOBAIS digite All."
                                 "\nEm caso de dúvidas verifique os paises listados na API no menu principal: ")
            querydate = input("\nInsida a data e pressione ENTER. "
                              "\nDeixe o campo em branco para todos os resultados registrados."
                              "\nData (AAAAMMDD): ")
            while len(querydate) > 0 and len(querydate) != 8:
                querydate = input("\nProblemas ao verificar a data. Insida a data e pressione ENTER. "
                                  "\nDeixe o campo em branco para todos os resultados registrados."
                                  "\nData (AAAAMMDD): ")
            querydate = querydate[:4] + "-" + querydate[4:6] + "-" + querydate[6:]
            query = {"country": str(querycountry), "day": str(querydate)}

            # Ajuste de parâmetros, se necessário
            if len(query["day"]) == 2:
                del query["day"]
            url = "https://covid-193.p.rapidapi.com/history"

            # Requisição
            req = APIRequest.requesturl(url, query)

            # Pesquisa com erros nos parâmetros inseridos
            if not len(req["errors"]) == 0:
                for errors in req["errors"]:
                    print(req["errors"][errors])

            # Pesquisa sem erros.
            else:
                print("\nForam encontradas " + str(req["results"]) + " referências para " + str(req["parameters"]["country"]))
                results = 0
                while results < int(req["results"]):
                    print("\nReferência (YYYY-MM-DD): " + str(req["response"][results]["day"]))
                    correctedour = str(req["response"][results]["time"])[11:16]
                    print("Horário de referência: " + correctedour)
                    print("Casos confirmados: " + str(req["response"][results]["cases"]["total"]))
                    print("Casos ativos: " + str(req["response"][results]["cases"]["active"]))
                    print("Casos críticos: " + str(req["response"][results]["cases"]["critical"]))
                    print("Casos recuperados: " + str(req["response"][results]["cases"]["recovered"]))
                    print("Casos novos: " + str(req["response"][results]["cases"]["new"]))
                    print("Casos por milhão: " + str(req["response"][results]["cases"]["1M_pop"]))
                    print("Total de Mortos: " + str(req["response"][results]["deaths"]["total"]))
                    print("Novas mortes: " + str(req["response"][results]["deaths"]["new"]))
                    print("Mortes por milhão: " + str(req["response"][results]["deaths"]["1M_pop"]))
                    print("Testes realizados: " + str(req["response"][results]["tests"]["total"]))
                    print("Testes por milhão: " + str(req["response"][results]["tests"]["1M_pop"]) + "\n")
                    results += 1

                # Exportar resultados
                XLSX.createspreadsheet(number, req)
