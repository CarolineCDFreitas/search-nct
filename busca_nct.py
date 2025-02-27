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


# nct
dojaejung = ["dojaejung", doyoung, jaehyun, jungwoo, "nct", "2023"]
ilichil = [
    "Ilichil",
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
dream = ["Dream", mark, haechan, renjun, jeno, jaemin, chenle, jisung, "nct", "2016"]
wayv = ["WayV", kun, ten, winwin, hendery, xiaojun, yangyang, "nct", "2019"]
wish = ["Wish", sion, riku, yushi, jaehee, ryo, sakuya, "nct", "2024"]
nct = [dojaejung, ilichil, dream, wayv, wish]


while True:

    print("Opções \n1 - Ano de debut \n2 - Unit \n3 - Nome \n4 - Idade \n")
    opcao = int(input("Insira a opção que deseje pesquisar: "))

    id_membro = []
    membros_encontrados = []
    if opcao == OPCOES.ANO_DE_DEBUT.value:
        resposta = int(input("Digite o ano: "))
        if resposta:
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
        list = ", ".join(membros).replace(", e,", " e")

    if (len(membros)) == 1:
        print(f"O membro do NCT que debutou no ano {str(resposta)} foi {membros[0]}.")
    elif (len(membros)) > 1:
        print(f"Os membros do NCT que debutaram no ano {str(resposta)} foram {list}.")
    elif resposta < 2016:
        print(
            "O NCT debutou, pela primeira vez, em 2016. Pesquise por anos posteriores a esse."
        )
    else:
        print("Nenhum membro debutou nesse ano.")
    break
