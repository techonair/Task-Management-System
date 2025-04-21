from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app import routes, health
from app.models import Base
from app.database import engine
from fastapi.exceptions import RequestValidationError

app = FastAPI(title="Task Management System")

Base.metadata.create_all(bind=engine)

@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    custom_errors = []

    for err in errors:
        if "enum" in str(err.get("msg", "")):
            custom_errors.append({
                "field": err.get("loc")[-1],
                "message": "Invalid status. Allowed values: 'pending', 'in-progress', 'completed'."
            })
        else:
            custom_errors.append({
                "field": err.get("loc")[-1],
                "message": err.get("msg")
            })

    return JSONResponse(
        status_code=422,
        content={"errors": custom_errors}
    )

app.include_router(routes.router)
app.include_router(health.router)