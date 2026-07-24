from fastapi import FastAPI

app = FastAPI(
    title="Tool Loan API",
    version="1.0.0",
    description="API para la gestión de préstamos de herramientas."
)


@app.get("/")
def root():
    return {
        "message": "Tool Loan API funcionando correctamente"
    }