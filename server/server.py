from db_users_controller import DB_Users_Controller
from fastapi import *
from fastapi.responses import FileResponse
import uvicorn
from requests_models import *

print("Starting_server...")
db_users_controller = DB_Users_Controller()
app = FastAPI()

@app.get("/test")
async def test():
    print("TEST")
    return "Successfully connect to server!"

@app.get("/item")
async def get_item():
    # print("ANSWER")
    return FileResponse("tmp/database.db")

@app.post("/auth")
async def auth(auth_info: Auth_info):
    print(auth_info.name, auth_info.password)
    print("AUTH")
    return "Please, authorize!"


"""@app.middleware("http")
async def debug_request(request: Request, call_next):
    response = await call_next(request)
    print(Request.base_url)
    return response"""

uvicorn.run(app=app, host="localhost",port=9999)
