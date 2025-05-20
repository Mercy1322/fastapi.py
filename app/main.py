import sys

from fastapi import FastAPI


app = FastAPI(
    title="Bookstore REST Api",
    description=description,
    summary="CRUD of authors and books",
    version="1.0.0",
    terms_of_service="",
    contact={
        "name": "Angela Checa",
        "url": "https://github.com/Trjegul84",
        "email": "angela@gmail.com",
    },
    license_info="",
)
