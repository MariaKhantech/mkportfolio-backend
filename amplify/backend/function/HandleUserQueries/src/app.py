# from litestar import Litestar, get


# @get("/")
# async def index() -> str:
#     return "Hello, world!"


# @get("/books/{book_id:int}")
# async def get_book(book_id: int) -> dict[str, int]:
#     return {"book_id": book_id}


# app = Litestar([index, get_book])

# app.py
from litestar import Litestar, get
from mangum import Mangum

@get("/")
async def index() -> str:
    return "Hello, world!"

@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}

app = Litestar([index, get_book])

# Wrap the LiteStar application with Mangum for AWS Lambda compatibility
handler = Mangum(app)
