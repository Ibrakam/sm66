from fastapi import FastAPI, Request
from api.user_api.main import user_router
from api.post_api.main import post_router
from database import Base, engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.userservice import get_all_or_exact_user_db

app = FastAPI(docs_url="/docs")
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)
app.include_router(user_router)
app.include_router(post_router)


@app.get("/profile/{uid}", response_class=HTMLResponse)
async def main(request: Request, uid: int):
    exact_user = get_all_or_exact_user_db(uid=uid)
    return templates.TemplateResponse(request, name="index.html",
                                      context={"user": exact_user})
