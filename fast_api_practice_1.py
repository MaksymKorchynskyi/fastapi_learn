import time 
from fastapi.responses import StreamingResponse, FileResponse
from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, Response, BackgroundTasks, File, UploadFile
import uvicorn
from sqlalchemy import select
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from authx import AuthX, AuthXConfig
import asyncio

app = FastAPI()

@app.get(path= "/users", tags= ["Users"], summary="Claim users")
async def get_users():
    return [{"id":1, "name": "Artem"}]

if __name__ == "__main__":
    uvicorn.run("fast_api_practice_1:app", host="0.0.0.0", port=8000)


# books = [
#     {"id": 1,
#     "title" : "Assync in Python",
#     "author": "Metty",
#     },
#     {
#     "id": 2,
#     "title": "Backend develop in Python",
#     "author": "Artem", 
#     }]

# class BookSchema(BaseModel):
#     title: str 
#     author: str

# @app.get(path= "/books", 
#         tags=["Books"],
#         summary="Receive list books",
#         description="<h1> Get list all books<h1>",)
# def get_books():
#     return books

# @app.post(path= "/books", tags=["Books"])
# def add_book(book: BookSchema):
#     new_book_id = len(books) + 1
#     books.append({
#     "id": new_book_id,
#     "title": book.title,
#     "author": book.author
#     })
#     return {"success": True, "message": "Books Added"}


# @app.post("/files")
# async def upload_file(uploaded_file: UploadFile):
#     file = uploaded_file.file
#     filename = uploaded_file.filename
#     with open(filename, "wb") as f:
#         f.write(file.read())

# @app.post("/multiple_files")
# async def upload_files(uploaded_files: list[UploadFile]):
#     for uploaded_file in uploaded_files:
#         file = uploaded_file.file
#         filename = uploaded_file.filename
#     with open(filename, "wb") as f:
#         f.write(file.read())

# @app.get("/files/{filename}")
# async def get_file(filename: str):
#     return FileResponse(filename)
    
# def iterfile(filename: str):
#     with open(filename,"rd") as file:
#         while chunk := file.read(1024 * 1024):
#             yield chunk

# @app.get("/files/streaming/{filename}")
# async def get_streaming_file(filename: str):
#     return StreamingResponse(iterfile(filename),media_type="video/mp4")

# def sync_task():
#     time.sleep(3)
#     print("Send email")

# async def async_task():
#     await asyncio.sleep(3)
#     print("Completed request in another API")


# @app.post(path="/")
# async def some_route(bg_tasks: BackgroundTasks):
#     ...
#     #asyncio.create_task(async_task())
#     bg_tasks.add_task(sync_task)
#     return {"ok": True}




# config = AuthXConfig()
# config.JWT_SECRET_KEY = "SECRET_KEY"
# config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
# config.JWT_TOKEN_LOCATION = ["cookies"]

# security= AuthX(config=config)

# class UserLoginSchema(BaseModel):
#     username: str
#     password: str 
    

# @app.post("/login")
# def login(creds: UserLoginSchema, response: Response):
#     if creds.username == "test" and creds.password =="test":
#         token = security.create_access_token(uid="12345")
#         response.set_cookie(config.JWT_ACCESS_COOKIE_NAME,token)
#         return {"access_token": token}
#     raise HTTPException(status_code= 401, detail="Incorrect username or password")


# @app.get("/protected", dependencies=[Depends(security.access_token_required)])
# def protected():
#     return{"data":"TOP SECRET"}



# engine = create_async_engine('sqlite+aiosqlite:///books.db')

# new_session = async_sessionmaker(engine, expire_on_commit=False)

# async def get_session():
#     async with new_session() as session:
#         yield session

# SessionDep = Annotated[AsyncSession, Depends(get_session)]

# class Base(DeclarativeBase):
#     pass

# class BookModel(Base):
#     __tablename__ = "books"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     author: Mapped[str]

# @app.post("/setup_database")
# async def setup_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     return {"ok": True}

# class BookAddSchema(BaseModel):
#     title: str
#     author: str

# class BookSchema(BookAddSchema):
#     id: int 


# @app.post("/books")
# async def add_book(data: BookAddSchema, session: SessionDep):
#     new_book = BookModel(
#         title = data.title,
#         author = data.author,
#     )
#     session.add(new_book)
#     await session.commit()
#     return {"ok": True}

# @app.get("/books")
# async def get_books(session: SessionDep):
#     query = select(BookModel)
#     result = await session.execute(query)
#     return result.scalars().all()

# books = [{   
#     "id" : 1,
#     "title" : "Assinhronic in Python",
#     "author" : "Ronald"},
# {
#     "id" : 2,
#     "title" : "Backend in Python",
#     "author" : "Tom",
# }]

# @app.get("/books", tags= ["Books"], summary="Receive all books")
# def read_books():
#     return books;

# @app.get("/books/{book_id}", tags= ["Books"], summary= "Receive some books")
# def get_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             return book;
#     raise HTTPException(status_code=404, detail= "Books not found")

# class NewBook(BaseModel):
#     title: str
#     author: str

# @app.post("/books")
# def create_books(new_book: NewBook):
#     books.append({
#         "id": len(books) + 1,
#         "title": new_book.title,
#         "author": new_book.author,
#     })
#     return {"success": True, "message": "Books succesfully apporove"}

# if __name__ == "__main__":
#     uvicorn.run(app="fast_api_practice_1:app", reload= True)

