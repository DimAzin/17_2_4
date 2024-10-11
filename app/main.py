from fastapi import FastAPI
from user import router as user_router

app = FastAPI()

# Подключаем маршруты пользователя
app.include_router(user_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
