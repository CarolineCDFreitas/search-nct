# exercício de busca com lista, loops e condicionais

from enum import Enum


class OPCOES(Enum):
    ANO_DE_DEBUT = 1
    UNIT = 2
    NOME = 3
    AGE = 4


# membros
johnny = [1, "Johnny", "1995", "2017"]
taeyong = [2, "Taeyong", "1995", "2016"]
yuta = [3, "Yuta", "1995", "2016"]
doyoung = [4, "Doyoung", "1996", "2016"]
kun = [5, "Kun", "1996", "2018"]
ten = [6, "Ten", "1996", "2016"]
jaehyun = [7, "Jaehyun", "1997", "2016"]
winwin = [8, "Winwin", "1997", "2016"]
jungwoo = [9, "Jungwoo", "1998", "2018"]
mark = [10, "Mark", "1999", "2016"]
hendery = [11, "Hendery", "1999", "2019"]
xiaojun = [12, "Xiaojun", "1999", "2019"]
haechan = [13, "Haechan", "2000", "2016"]
renjun = [14, "Renjun", "2000", "2016"]
jeno = [15, "Jeno", "2000", "2016"]
jaemin = [16, "Jaemin", "2000", "2016"]
yangyang = [17, "YangYang", "2000", "2019"]
chenle = [18, "Chenle", "2001", "2016"]
jisung = [19, "Jisung", "2002", "2016"]
sion = [20, "Sion", "2002", "2024"]
riku = [21, "Riku", "2003", "2024"]
yushi = [22, "Yushi", "2005", "2024"]
jaehee = [23, "Jaehee", "2005", "2024"]
ryo = [24, "Ryo", "2007", "2024"]
sakuya = [25, "Sakuya", "2007", "2024"]

debut_years = ["2016", "2017", "2018", "2019", "2024"]

# nct
dojaejung = ["DOJAEJUNG", doyoung, jaehyun, jungwoo, "nct", "2023"]
ilichil = [
    "127",
    johnny,
    taeyong,
    yuta,
    doyoung,
    jaehyun,
    jungwoo,
    mark,
    haechan,
    "nct",
    "2016",
]
dream = ["dream", mark, haechan, renjun, jeno, jaemin, chenle, jisung, "nct", "2016"]
wayv = ["wayv", kun, ten, winwin, hendery, xiaojun, yangyang, "nct", "2019"]
wish = ["wish", sion, riku, yushi, jaehee, ryo, sakuya, "nct", "2024"]
nct = [dojaejung, ilichil, dream, wayv, wish]


while True:

    print("Opções \n1 - Ano de debut \n2 - Unit \n3 - Nome \n4 - Idade \n")
    opcao = int(input("Insira a opção que deseje pesquisar: "))

    resposta = str()

    id_membro = []
    membros_encontrados = []

    if opcao == OPCOES.ANO_DE_DEBUT.value:
        resposta = int(input("Digite o ano: "))
        if resposta not in [int(ano) for ano in debut_years]:
            if resposta < 2016:
                print(
                    "O NCT debutou, pela primeira vez, em 2016. Pesquise por anos posteriores a esse."
                )
            else:
                print("Nenhum membro debutou nesse ano.")
        elif resposta:
            for unit in nct:
                for membro in unit:
                    if isinstance(membro, list):
                        if resposta == int(membro[3]):
                            id_membro.append(membro[0])
                            membros_encontrados.append(membro[1])

        membros_id = list(set(id_membro))
        membros = list(set(membros_encontrados))

        if len(membros) >= 2:
            membros.insert(-1, "e")
            lista_de_membros = ", ".join(membros).replace(", e,", " e")

        if (len(membros)) == 1:
            print(
                f"O membro do NCT que debutou no ano {str(resposta)} foi {membros[0]}."
            )
        elif (len(membros)) > 1:
            print(
                f"Os membros do NCT que debutaram no ano {str(resposta)} foram {lista_de_membros}."
            )

    elif opcao == OPCOES.UNIT.value:
        resposta = input("Digite a unit: ")
        if resposta.lower() not in [unit[0].lower() for unit in nct]:
            print("Digite um nome válido")
        elif resposta:
            for unit in nct:
                if resposta.lower() == unit[0].lower():
                    if isinstance(unit, list):
                        for membro in unit:
                            if isinstance(membro, list):
                                membros_encontrados.append(membro[1])

        membros = list(set(membros_encontrados))

        if len(membros):
            membros.insert(-1, "e")
            lista_de_membros = ", ".join(membros).replace(", e,", " e")
            
            if resposta.lower() == wayv[0]:
                print(f"Os membros do WayV são {lista_de_membros}.")
            else:
                print(f"Os membros do NCT {resposta.upper()} são {lista_de_membros}.")

    elif opcao == OPCOES.NOME.value:
        resposta = input("Digite o nome: ")
        if resposta:
            for unit in nct:
                for membro in unit:
                    if isinstance(membro, list):
                        if resposta.lower() == membro[1].lower():
                            membros_encontrados.append(membro)
                            id_membro.append(membro[0])
        units_encontradas = set()

        for membro in membros_encontrados:
            for unit in nct:
                for membro_especifico in unit:
                    if (
                        isinstance(membro_especifico, list)
                        and membro_especifico[0] == membro[0]
                    ):
                        units_encontradas.add(unit[0])
        units = list(units_encontradas)

        #### ============= to do ========= ####
        # lista_de_units para ajustar o dream e sua formatação tirando o replace
        if len(units) > 1:
            units.insert(-1, "e")
            lista_de_units = ", ".join(units).replace(", e,", " e NCT")

        if (len(units)) == 1 and "wayv" in units_encontradas:
            print(f"{resposta.capitalize()} está no WayV.")
        elif (len(units)) == 1 and "wayv" not in units_encontradas:
            print(f"{resposta.capitalize()} está no NCT {(units[0])}.")
        elif (len(units)) >= 2:
            print(f"{resposta.capitalize()} está no NCT {lista_de_units}.")

    break
