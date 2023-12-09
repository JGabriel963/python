from fastapi import FastAPI

app = FastAPI()

# Dicionário de Jogadores
players = [
    {
        "id": 1,
        "name": "Dudu",
        "age": 30,
        "time": "Palmeiras"
    },
    {
        "id": 2,
        "name": "Vinícius JR",
        "age": 28,
        "time": "Real Madrid"
    },
    {
        "id": 3,
        "name": "Raphael Veiga",
        "age": 29,
        "time": "Flamengo"
    }
]


@app.get("/")
def index():
    return {"Mensagem": "Olá mundo!"}

@app.get('/players')
def list_players():
    return players

# Path Parameter
@app.get("/players/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player
        else:
            return {"Messagem": "Player not found"}
    
# Query Parameter
@app.get("/players_by_name")
def get_by_name(name: str):
    for player in players:
        if player['name'] == name:
            return player
        else:
            return {"Messagem": "Player not found"}