"""
This is the main file, which will be used for running the application.
"""
from fastapi import FastAPI
import routes.authentication
import routes.do_select

fast = FastAPI()  # instance for FastAPI


fast.include_router(routes.do_select.router)
fast.include_router(routes.authentication.route)
