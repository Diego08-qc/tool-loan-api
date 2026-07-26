from fastapi import FastAPI

from app.routers.tool import router as tool_router

from app.routers.borrower import router as borrower_router

from app.routers.loan import router as loan_router

app = FastAPI(
    title="Tool Loan API",
    version="1.0.0",
    description="API para la gestión de préstamos de herramientas."
)

app.include_router(tool_router)
app.include_router(borrower_router)
app.include_router(loan_router)


@app.get("/")
def root():
    return {
        "message": "Tool Loan API funcionando correctamente"
    }