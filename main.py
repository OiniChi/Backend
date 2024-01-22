from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
async def print_func() -> str:
    return "Лысенко Андрей Максимович"

@app.get('/users')
async def print_func() -> str:
    return "Номер тел. : +79234671287"

@app.get('/tools')
async def print_func() -> str:
    return f"Навыки: Владения ООП, базовое владение реляционными базами данных SQL/PostgreSQL, знания языков: С/C++/C#, Python, знания фреймворков .Net Framework, FastAPI, Docker..."

suka
