from fastapi import APIRouter, Depends


route=APIRouter()

@route.get("/get_user")
def greet():
    return ("welcome")
