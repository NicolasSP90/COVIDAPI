from MainSearchSettings import SearchSettings
import time

# Introdução
print("Desafio Owntec - v1.0"
      "\nInformações atualizadas sobre COVID!")

# Início com o menu de opções
startmenu = True
while startmenu:
    print("\nDefina o critério inicial da pesquisa:",
          "\n1- Pesquisa por paises listados na API.",
          "\n2- Pesquisar dados atuais sobre COVID.",
          "\n3- Pesquisar dados sobre COVID em data específica."
          "\n4- Sair.")
    menuoption = int(input())
    while not int(1) <= int(menuoption) <= int(4):
        print("Opçãp não identificada. Informe novamente."
              "\nDefina o critério inicial da pesquisa selecionando o número de um dos menus abaixo:",
              "\n1- Pesquisa por paises listados na API.",
              "\n2- Pesquisar dados atuais sobre COVID.",
              "\n3- Pesquisar dados sobre COVID em data específica."
              "\n4- Sair.")

    # Opção de encerrar o programa
    if menuoption == 4:
        print("Obrigado por utilizar o programa. Encerrando a aplicação.")
        time.sleep(2)
        exit()

    # Definição das configurações de pesquisa
    else:
        SearchSettings.menunumber(menuoption)
