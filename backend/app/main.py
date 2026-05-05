# import FastAPI
from fastapi import FastAPI

# import your routes file
from app.routes import order_routes   # <-- add this

# create app
app = FastAPI()

# connect the router to the app
app.include_router(order_routes.router)   # <-- add this

# keep your root test route
@app.get("/")
def read_root():
    return {"message": "Hello Excalibur"}
