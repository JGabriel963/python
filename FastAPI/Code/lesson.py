from fastapi import FastAPI, HTTPException

app = FastAPI()

cursos = {
    1: {
        "nome": "Dominando o Python",
        "nivel": "básico",
        "formacao": "PythonFundamentos"
    },
    2: {
        "nome": "Automação de Tarefas",
        "nivel": "intermediário",
        "formacao": "Automação"
    },
    3: {
        "nome": "Automação com Selenium",
        "nivel": "intermediário",
        "formacao": "Automação"
    }
}
# Path Parameter
@app.get("/cursos/{formacao}")
async def get_cursos_automacao(formacao:str):
    cursos_automacao = [
        curso for curso in cursos.values() if curso["formacao"] == formacao
        ]
    return cursos_automacao

# Query Parameter
@app.get("/cursos/")
async def get_cursos_por_formacao(formacao: str):
    cursos_por_formacao = [
        curso for curso in cursos.values() if curso["formacao"].lower() == formacao.lower()
    ]
    if not cursos_por_formacao:
        raise HTTPException(status_code=404, detail="Formação não encontrada")
    return cursos_por_formacao