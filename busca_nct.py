# exercício de busca com lista, loops e condicionais

from enum import Enum


class OPCOES(Enum):
    ANO_DE_DEBUT = 1
    UNIT = 2
    NOME = 3
    AGE = 4


# membros
johnny = ["Johnny", "1995", "2017"]
taeyong = ["Taeyong", "1995", "2016"]
yuta = ["Yuta", "1995", "2016"]
doyoung = ["Doyoung", "1996", "2016"]
kun = ["Kun", "1996", "2018"]
ten = ["Ten", "1996", "2016"]
jaehyun = ["Jaehyun", "1997", "2016"]
winwin = ["Winwin", "1997", "2016"]
jungwoo = ["Jungwoo", "1998", "2018"]
mark = ["Mark", "1999", "2016"]
hendery = ["Hendery", "1999", "2019"]
xiaojun = ["Xiaojun", "1999", "2019"]
haechan = ["Haechan", "2000", "2016"]
renjun = ["Renjun", "2000", "2016"]
jeno = ["Jeno", "2000", "2016"]
jaemin = ["Jaemin", "2000", "2016"]
yangyang = ["YangYang", "2000", "2019"]
chenle = ["Chenle", "2001", "2016"]
jisung = ["Jisung", "2002", "2016"]
sion = ["Sion", "2002", "2024"]
riku = ["Riku", "2003", "2024"]
yushi = ["Yushi", "2005", "2024"]
jaehee = ["Jaehee", "2005", "2024"]
ryo = ["Ryo", "2007", "2024"]
sakuya = ["Sakuya", "2007", "2024"]


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

    members = []
    if opcao == OPCOES.ANO_DE_DEBUT.value:
        resposta = int(input("Digite o ano: "))
        if resposta:
            for unit in nct:
                for member in unit:
                    if isinstance(member, list):
                        if resposta == int(member[2]):
                            members.append(member[0])

    if len(members) >= 2:
        members.insert(-1, "e")
        list = ", ".join(members).replace(", e,", " e")
        
    

    if (len(members)) == 1:
        print(f"O membro do NCT que debutou no ano {str(resposta)} foi {members[0]}.")
    elif (len(members)) > 1:
        print(f"Os membros do NCT que debutaram no ano {str(resposta)} foram {list}.")
    elif resposta < 2016:
        print(
            "O NCT debutou, pela primeira vez, em 2016. Pesquise por anos posteriores a esse."
        )
    else:
        print("Nenhum membro debutou nesse ano.")
    break


# for unit in nct:
#     for member in unit:
#         if isinstance(member, list):
#             if int(member[1]) > 2000:
#                 print(f"{member[0]}, nascido em {member[1]} do {unit[0]}")
