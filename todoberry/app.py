from fastapi import FastAPI
from todoberry.api import items_router, lists_router


app = FastAPI()

app.include_router(
    items_router,
    prefix="/lists/{list_id}/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    lists_router,
    prefix="/lists",
    tags=["lists"],
    responses={404: {"description": "Not found"}},
)
