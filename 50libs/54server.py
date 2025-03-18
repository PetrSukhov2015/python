from fastapi import FastAPI
import uvicorn

# Создание приложения FastAPI
app = FastAPI()

# Первый GET-запрос
@app.get("/api/v1/hello")
def hello():
    return {"message": "fuck, World!"}

# Второй GET-запрос
@app.get("/api/v1/data")
def get_data():
    return {"data": [1, 2, 3, 4, 5]}

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)