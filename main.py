from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
async def print_func1() -> str:
    return "Лысенко Андрей Максимович"

@app.get('/users')
async def print_func2() -> str:
    return "Номер тел. : +79234671287"

@app.get('/tools')
async def print_func3() -> str:
    return f"Навыки: Владения ООП, базовое владение реляционными базами данных SQL/PostgreSQL, знания языков: С/C++/C#, Python, знания фреймворков .Net Framework, FastAPI, Docker..."

@app.get('/users')
async def print_func4() -> str:
    return "Номер тел. : +79234671287"
