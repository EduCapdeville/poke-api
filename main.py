from enum import Enum
from fastapi import FastAPI

dados = [
    {"name": "bulbasaur", "element": "grass", "attack": "scratch"},
    {"name": "charmander", "element": "fire", "attack": "ember"},
    {"name": "squirtle", "element": "water", "attack": "bubble"},
    {"name": "charizard", "element": "fire", "attack": "ember"},
    {"name": "blastoise", "element": "water", "attack": "bubble"},
    {"name": "pidgey", "element": "flying", "attack": "scratch"},
    {"name": "venusaur", "element": "grass", "attack": "scratch"},
    
]

class PokemonName(str, Enum):
    bulbasaur = "bulbasaur"
    charmander = "charmander"
    squirtle = "squirtle"
    pidgey = "pidgey"
    
app = FastAPI()

@app.get("/pokemons/{pokemon_name}")
async def get_pokemon(pokemon_name: PokemonName):
    for pokemon in dados:
        if pokemon["name"] == pokemon_name.value:
            return {
                "name": pokemon["name"],
                "element": pokemon["element"],
                "attack": pokemon["attack"]
            }

    return {"chosen_pokemon": pokemon_name, "message": "Pokémon not found"}

@app.get("/pokemons/")
async def get_pokemon_attack(attack_name: str):    
    #criar um container
    #pegar um item e verificar se ele satisfaz uma condição
    #se for positivo guarda no container criado
    #se for negativo ignora
    #repete para todos os itens
    pokemons = list()
    for pokemon in dados:
        if pokemon["attack"] == attack_name:
            pokemons.append(pokemon)
    return pokemons
            
        
    
    