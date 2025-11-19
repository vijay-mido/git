from fastapi import APIRouter, Depends


route=APIRouter()

@route.get("/get_user")
def greet():
    return ("welcome")

@route.get("/user")
def wel():
    return ("heee")