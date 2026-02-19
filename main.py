from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    message = "Привет, это строка из FastAPI!"
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"data": message}
    )

if __name__ == "__main__":
    import uvicorn
    file_name = os.path.basename(__file__)
    module_name = file_name[:-3]
    uvicorn.run(
        f"{module_name}:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True
    )