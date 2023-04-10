import requests
from pprint import pprint




"""
Instruções para TODOS os exercícios/funções abaixo:
1. Veja as instruções de como instalar o treinador e os testes no documento entregue junto com este arquivo.
2. Se um determinado parâmetro de uma função deve ser inteiro, então esta função deve rejeitar valores não-numéricos ou numerais não-inteiros nesse parâmetro.
3. Da mesma forma, se um parâmetro de uma função deve ser uma string, então esta função deve rejeitar valores que não sejam do tipo string nesse parâmetro.
4. Strings em branco são sempre consideradas inválidas.
5. Todos os nomes de pokémons que aparecerem como parâmetros devem ser aceitos em minúsculas, MAIÚSCULAS ou até mesmo MiStUrAdO. Lembre-se dos métodos lower() e upper() da classe string.
6. Todos os nomes de pokémons, cores, jogos, movimentos, etc. recebidos e devolvidos pela PokeAPI estão em letras minúsculas e assim devem ser mantidas.

Alguns exemplos de URLs que podem servir de inspiração:
http://pokeapi.co/api/v2/

http://pokeapi.co/api/v2/pokemon/39/
http://pokeapi.co/api/v2/pokemon/jigglypuff/

http://pokeapi.co/api/v2/pokemon-species/39/
http://pokeapi.co/api/v2/pokemon-species/jigglypuff/

http://pokeapi.co/api/v2/evolution-chain/11/
http://pokeapi.co/api/v2/growth-rate/1/
http://pokeapi.co/api/v2/pokemon-color/2/
"""

"""
Não altere esta URL. Ela é utilizada para conectar no PokeAPI.
"""
site_pokeapi = "https://pokeapi.co"

"""
Vamos precisar destas quatro exceções personalizadas.
Abaixo, criamos excessões com nomes personalizados.
"""

class PokemonNaoExisteException(Exception):
    pass #nao faça nada aqui nem nas Exceptions seguintes
         # ela já está pronta, só é um "nome" novo

class PokemonNaoCadastradoException(Exception):
    pass

class TreinadorNaoCadastradoException(Exception):
    pass

class PokemonJaCadastradoException(Exception):
    pass

"""
Esta função certifica-se de que seu parâmetro é um número inteiro e lança uma ValueError se não for.
"""
def check_int(a):
    if type(a) is not int:
        raise ValueError()

"""
Esta função certifica-se de que seu parâmetro é uma string e que não está vazia e lança uma ValueError se não for.
"""
def check_str(a):
    if type(a) is not str or a == "":
        raise ValueError()



dic_cores = {
    "brown": "marrom",
    "yellow": "amarelo",
    "blue": "azul",
    "pink": "rosa",
    "gray": "cinza",
    "purple": "roxo",
    "red": "vermelho",
    "white": "branco",
    "green": "verde",
    "black": "preto"
}

dic_tipos = {
    "normal": "normal",
    "fighting": "lutador",
    "flying": "voador",
    "poison": "veneno",
    "ground": "terra",
    "rock": "pedra",
    "bug": "inseto",
    "ghost": "fantasma",
    "steel": "aço",
    "fire": "fogo",
    "water": "água",
    "grass": "grama",
    "electric": "elétrico",
    "psychic": "psíquico",
    "ice": "gelo",
    "dragon": "dragão",
    "dark": "noturno",
    "fairy": "fada"
}

"""
1. Dado o número de um pokémon, qual é o nome dele?
"""
def nome_do_pokemon(numero):    
    check_int(numero)
    if numero < 1 or numero > 807: 
        raise PokemonNaoExisteException()
    url = f'http://pokeapi.co/api/v2/pokemon/{numero}/'
    response = requests.get(url)
    status_code = response.status_code   
    if response.status_code == 404:
        raise PokemonNaoExisteException()
    elif response.status_code == 200:    
        data = response.json()
        name = data['name']
        return name
    

"""
2. Dado o nome de um pokémon, qual é o número dele?
"""
def numero_do_pokemon(nome):
    check_str(nome)
    url = f'http://pokeapi.co/api/v2/pokemon/{nome.lower()}/'

    response = requests.get(url)
    status_code = response.status_code
    if response.status_code == 404:
        raise PokemonNaoExisteException()
    elif response.status_code == 200:
        data = response.json()
        numero = data['id']
        return numero
    
"""
3. Dado o nome ou número de um pokémon, qual é o nome da cor (em inglês) predominante dele?
"""
def color_of_pokemon(nome):
    check_str(nome)
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
    response = requests.get(url)
    status_code = response.status_code
    if response.status_code == 404:
        raise PokemonNaoExisteException()
    elif response.status_code == 200:
        data = response.json()
        return data['color']['name']
   

"""
4. Dado o nome de um pokémon, qual é o nome da cor (em português) predominante dele?
Os nomes de cores possíveis em português são "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?
"""
def cor_do_pokemon(nome):    
    check_str(nome)
    return dic_cores[color_of_pokemon(nome)]
    #  url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
    #  response = requests.get(url)
    #  status_code = response.status_code
    #  if response.status_code == 404:
    #     raise PokemonNaoExisteException()
    #  elif response.status_code == 200:
    #     data = response.json()
    #     color =  data['color']['name']   
    #     if color in dic_cores.keys():
    #         return dic_cores[color]

     
"""
5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista contendo os tipos, mesmo que haja somente um.
Se houver dois tipos, a ordem não é importante.
"""
def tipos_do_pokemon(nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome.lower()}/'
    response = requests.get(url)
    status_code = response.status_code
    if response.status_code == 404:
        raise PokemonNaoExisteException()
    elif response.status_code == 200:
        list_types = []
        list_types_portugues = []
        data = response.json()
        types = data['types']

        for item in types:
            name = item['type']['name']
            list_types.append(name)
        for i in list_types:
            if i in dic_tipos.keys():
                list_types_portugues.append(dic_tipos[i])
        return list_types_portugues     

"""
6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None
"""
def evolucao_anterior(nome):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
    response = requests.get(url)
    status_code = response.status_code
    if response.status_code == 404:
        raise PokemonNaoExisteException()
    elif response.status_code == 200:
        data = response.json()
        if data['evolves_from_species'] == None:
            return None
        return data['evolves_from_species']['name']
    else:
        return status_code
    
"""
7. A medida que ganham pontos de experiência, os pokémons sobem de nível.
É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
Valores negativos de experiência devem ser considerados inválidos.
dica: na URL pokemon-species, procure growth rate
"""
def nivel_do_pokemon(nome, experiencia):# experiencia

    if experiencia < 0: 
        raise ValueError()
    url = f'https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}/'
    response = requests.get(url)
    status_code = response.status_code
    if status_code == 404:
        raise PokemonNaoExisteException()
    elif status_code == 200:
        data = response.json()
        nivel = data['growth_rate']['url']
        response2 = requests.get(nivel)
        status_code2 = response.status_code
        if status_code2 == 404:
            raise PokemonNaoExisteException()
        elif status_code2 == 200:
            lista_nivel = response2.json()['levels']
            level = 0  
            for xpLevel in lista_nivel: 
                if experiencia < xpLevel['experience']:
                    return level
                level = xpLevel['level']

            return level
        else:
            return status_code
                

