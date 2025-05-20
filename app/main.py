import sys

from fastapi import FastAPI


app = FastAPI(
    title="Bookstore REST Api",
    description=description,
    summary="CRUD of authors and books",
    version="1.0.0",
    terms_of_service="",
    license_info="",
)
