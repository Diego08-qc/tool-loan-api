from fastapi import FastAPI

from app.routers.tool import router as tool_router

app = FastAPI(
    title="Tool Loan API",
    version="1.0.0",
    description="API para la gestión de préstamos de herramientas."
)

app.include_router(tool_router)


@app.get("/")
def root():
    return {
        "message": "Tool Loan API funcionando correctamente"
    }