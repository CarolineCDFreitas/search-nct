# exercício de busca com lista, loops e condicionais. Agora dicionários

from enum import Enum


class OPCOES(Enum):
    ANO_DE_DEBUT = 1
    UNIT = 2
    NOME = 3
    IDADE = 4

#membros
johnny = {
    "id": 1,
    "nome_artistico": "Johnny",
    "nome": "John Jun Suh",
    "ano_de_nascimento": "1995",
    "nacionalidade": "estadunidense",
    "debut_info": [
        {"ano": 2017, "unit": "127", "debut_song": "Limitless"},
    ],
}

taeyong = {
    "id": 2,
    "nome_artistico": "Taeyong",
    "nome": "Lee Taeyong",
    "ano_de_nascimento": "1995",
    "nacionalidade": "sul-coreano",
    "debut_info": [
        {"ano": 2016, "unit": "u", "debut_song": "The 7th Sense"},
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2023, "unit": "solo", "debut_song": "Shalala"},
    ],
}

yuta = {
    "id": 3,
    "nome_artistico": "Yuta",
    "nome": "Nakamoto Yuta",
    "ano_de_nascimento": "1995",
    "nacionalidade": "japonês",
    "debut_info": [
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2024, "unit": "solo", "debut_song": "Off the Mask"},
    ],
}

doyoung = {
    "id": 4,
    "nome_artistico": "Doyoung",
    "nome": "Kim Dongyoung",
    "ano_de_nascimento": "1996",
    "nacionalidade": "sul-coreano",
    "debut_info": [
        {"ano": 2016, "unit": "u", "debut_song": "The 7th Sense"},
        {"ano": 2017, "unit": "127", "debut_song": "Limitless"},
        {"ano": 2023, "unit": "dojaejung", "debut_song": "Perfume"},
        {"ano": 2024, "unit": "solo", "debut_song": "Little Light"},
    ],
}

kun = {
    "id": 5,
    "nome_artistico": "Kun",
    "nome": "Qian Kun",
    "ano_de_nascimento": "1996",
    "nacionalidade": "chinês",
    "debut_info": [
        {"ano": 2018, "unit": "u", "debut_song": None},
        {"ano": 2019, "unit": "wayv", "debut_song": "Regular"},
    ],
}

ten = {
    "id": 6,
    "nome_artistico": "Ten",
    "nome": "Chittaphon Leechaiyapornkul",
    "ano_de_nascimento": "1996",
    "nacionalidade": "tailândes",
    "debut_info": [
        {"ano": 2016, "unit": "u", "debut_song": "The 7th Sense"},
        {"ano": 2019, "unit": "wayv", "debut_song": "Regular"},
        {"ano": 2024, "unit": "solo", "debut_song": "Nightwalker"},
    ],
}

jaehyun = {
    "id": 7,
    "nome_artistico": "Jaehyun",
    "nome": "Jeong Yuno",
    "ano_de_nascimento": "1997",
    "nacionalidade": "sul-coreano",
    "debut_info": [
        {"ano": 2016, "unit": "u", "debut_song": "The 7th Sense"},
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2023, "unit": "dojaejung", "debut_song": "Perfume"},
        {"ano": 2024, "unit": "solo", "debut_song": "Smoke"},
    ],
}

winwin = {
    "id": 8,
    "nome_artistico": "Winwin",
    "nome": "Dong Sicheng",
    "ano_de_nascimento": "1997",
    "nacionalidade": "chinês",
    "debut_info": [
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2019, "unit": "wayv", "debut_song": "Regular"},
    ],
}

jungwoo = {
    "id": 9,
    "nome_artistico": "Jungwoo",
    "nome": "Kim Jungwoo",
    "ano_de_nascimento": "1998",
    "nacionalidade": "sul-coreano",
    "debut_info": [
        {"ano": 2018, "unit": "u", "debut_song": "Boss"},
        {"ano": 2018, "unit": "127", "debut_song": "Regular"},
        {"ano": 2023, "unit": "dojaejung", "debut_song": "Perfume"},
        {"ano": None, "unit": None, "debut_song": None},
    ],
}

mark = {
    "id": 10,
    "nome_aristitico": "Mark",
    "nome": "Mark Lee",
    "ano_de_nascimento": "1999",
    "nacionalidade": "canadense",
    "debut_info": [
        {"ano": 2016, "unit": "u", "debut_song": "The 7th Sense"},
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"},
        {"ano": 2025, "unit": "solo", "debut_song": None},
    ],
}

hendery = {
    "id": 11,
    "nome_artistico": "Hendery",
    "nome": "Wong Kung Hang",
    "ano_de_nascimento": "1999",
    "nacionalidade": "macaense",
    "debut_info": [
        {"ano": 2019, "unit": "wayv", "debut_song": "Regular"},
    ],
}

xiaojun = {
    "id": 12,
    "nome_artistico": "Xioajun",
    "nome": "Xiao Dejun",
    "ano_de_nascimento": "1999",
    "nacionalidade": "chinês",
    "debut_info": [
        {"ano": 2019, "unit": "wayv", "debut_song": "Regular"},
        {"ano": 2020, "unit": "u", "debut_song": "Make a Wish"},
    ],
}

haechan = {
    "id": 13,
    "nome_artistico": "Haechan",
    "nome": "Lee Donghyuck",
    "ano_de_nascimento": "2000",
    "nacionalidade": "sul-coreano",
    "debut_info": [
        {"ano": 2016, "unit": "127", "debut_song": "Fire Truck"},
        {"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"},
        {"ano": None, "unit": "solo", "debut_song": None},
    ],
}

renjun = {
    "id": 14,
    "nome_artistico": "Renjun",
    "nome": "Huang Renjun",
    "ano_de_nascimento": "2000",
    "nacionalidade": "chinês",
    "debut_info": [{"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"}],
}

jeno = {
    "id": 15,
    "nome_artistico": "Jeno",
    "nome": "Lee Jeno",
    "ano_de_nascimento": "2000",
    "nacionalidade": "sul-coreano",
    "debut_info": [{"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"}],
}

jaemin = {
    "id": 16,
    "nome_artistico": "Jaemin",
    "nome": "Na Jaemin",
    "ano_de_nascimento": "2000",
    "nacionalidade": "sul-coreano",
    "debut_info": [{"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"}],
}

yangyang = {
    "id": 17,
    "nome_artistico": "Yangyang",
    "nome": "Liu Yangyang",
    "ano_de_nascimento": "2000",
    "nacionalidade": "taiwanês",
    "debut_info": [{"ano": 2019, "unit": "wayv", "debut_song": "Regular"}],
}

chenle = {
    "id": 18,
    "nome_artistico": "Chenle",
    "nome": "Zhong Chenle",
    "ano_de_nascimento": "2001",
    "nacionalidade": "chinês",
    "debut_info": [{"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"}],
}

jisung = {
    "id": 19,
    "nome_artistico": "Jisung",
    "nome": "Park Jisung",
    "ano_de_nascimento": "2002",
    "nacionalidade": "sul-coreano",
    "debut_info": [{"ano": 2016, "unit": "dream", "debut_song": "Chewing Gum"}],
}

sion = {
    "id": 20,
    "nome_artistico": "Sion",
    "nome": "Oh Sion",
    "ano_de_nascimento": "2002",
    "nacionalidade": "sul-coreano",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

riku = {
    "id": 21,
    "nome_artistico": "Riku",
    "nome": "Maeda Riku",
    "ano_de_nascimento": "2003",
    "nacionalidade": "japonês",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

yushi = {
    "id": 22,
    "nome_artistico": "Yushi",
    "nome": "Tokuno Yushi",
    "ano_de_nascimento": "2005",
    "nacionalidade": "japonês",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

jaehee = {
    "id": 23,
    "nome_artistico": "Jaehee",
    "nome": "Kim Daeyoung",
    "ano_de_nascimento": "2005",
    "nacionalidade": "sul-coreano",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

ryo = {
    "id": 24,
    "nome_artistico": "Ryo",
    "nome": "Hirose Ryo",
    "ano_de_nascimento": "2005",
    "nacionalidade": "japonês",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

sakuya = {
    "id": 25,
    "nome_artistico": "Sakuya",
    "nome": "Fujinaga Sakuya",
    "ano_de_nascimento": "2005",
    "nacionalidade": "japonês",
    "debut_info": [{"ano": 2024, "unit": "wish", "debut_song": "Wish"}],
}

#units
dojaejung = {
    "unit": "DOJAEJUNG",
    "membros": [
        doyoung, jaehyun, jungwoo
    ],
    "ano_de_debut": "2023",
    "debut_song": "Perfume"
},

ilichil = {
    "unit": "127",
    "membros": [
        johnny, taeyong, yuta, doyoung, jaehyun, jungwoo, mark, haechan
    ],
    "ano_de_debut": "2016",
    "debut_song": "Fire Truck"
}

dream = {
    "unit": "dream",
    "membros": [
        mark, haechan, renjun, jeno, jaemin, chenle, jisung
    ],
    "ano_de_debut": "2016",
    "debut_song": "Chewing Gum"
}

wayv = {
    "unit": "wayv",
    "membros": [
        kun, ten, winwin, hendery, xiaojun, yangyang
    ],
    "ano_de_debut": "2019",
    "debut_song": "Regular"
}

wish = {
    "unit": "wish",
    "membros": [
        sion, riku, yushi, jaehee, ryo, sakuya
    ],
    "ano_de_debut": "2024",
    "debut_song": "Wish"
}
#nct
nct = {
    "units": [
        dojaejung, ilichil, dream, wayv, wish
    ],
    "debut_years": ["2016", "2017", "2018", "2019", "2023", "2024"]
}

while True:

    print("Opções \n1 - Ano de debut \n2 - Unit \n3 - Nome \n4 - Idade \n")
    opcao = int(input("Insira a opção que deseje pesquisar: "))

    resposta = str()

    id_membro = []
    membros_encontrados = []
    units_encontradas = set()
    anos_encontrados = []

    if opcao == OPCOES.ANO_DE_DEBUT.value:
        resposta = int(input("Digite o ano: "))
        if resposta not in [int(ano) for ano in nct["debut_years"]]:
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
                            if (
                                membro[0] not in id_membro
                                and membro[1] not in membros_encontrados
                            ):
                                id_membro.append(membro[0])
                                membros_encontrados.append(membro[1])

        if len(membros_encontrados) >= 2:
            membros_encontrados.insert(-1, "e")
            lista_de_membros = ", ".join(membros_encontrados).replace(", e,", " e")

        if (len(membros_encontrados)) == 1:
            print(
                f"O membro do NCT que debutou no ano {str(resposta)} foi {membros_encontrados[0]}."
            )
        elif (len(membros_encontrados)) > 1:
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
                    anos_encontrados.append(unit[-1])
                    if isinstance(unit, list):
                        for membro in unit:
                            if isinstance(membro, list):
                                membros_encontrados.append(membro[1])

        if len(membros_encontrados):
            membros_encontrados.insert(-1, "e")
            lista_de_membros = ", ".join(membros_encontrados).replace(", e,", " e")

            if resposta.lower() == wayv[0]:
                print(
                    f"O WayV debutou em {wayv[-1]}. {lista_de_membros} são os membros do WayV."
                )
            else:
                print(
                    f"O NCT {resposta.upper()} debutou em {anos_encontrados[0]}. {lista_de_membros} são os membros do NCT {resposta.upper()}."
                )

    elif opcao == OPCOES.NOME.value:
        resposta = input("Digite o nome: ")
        if resposta:
            for unit in nct:
                for membro in unit:
                    if isinstance(membro, list):
                        if resposta.lower() == membro[1].lower():
                            membros_encontrados.append(membro)
                            id_membro.append(membro[0])

        for membro in membros_encontrados:
            for unit in nct:
                for membro_especifico in unit:
                    if (
                        isinstance(membro_especifico, list)
                        and membro_especifico[0] == membro[0]
                    ):
                        units_encontradas.add(unit[0])
        units = list(sorted(units_encontradas))

        if len(units) > 1:
            units.insert(-1, "e")
            lista_de_units = ", ".join(units).upper().replace(", E,", " e NCT")

        if (len(units)) == 1 and "wayv" in units_encontradas:
            print(f"{resposta.capitalize()} está no WayV.")
        elif (len(units)) == 1 and "wayv" not in units_encontradas:
            print(f"{resposta.capitalize()} está no NCT {(units[0].upper())}.")
        elif (len(units)) >= 2:
            print(f"{resposta.capitalize()} está no NCT {lista_de_units}.")

    break
