from fastapi import FastAPI, Body

app = FastAPI()


BOOKS = [
    {"title": "Title One", "author": "Author2", "category": "math"},
    {"title": "Title One", "author": "Author1", "category": "science"},
    {"title": "Title One", "author": "Author1", "category": "science"},
    {"title": "Title One", "author": "Author1", "category": "science"},
    {"title": "Title One", "author": "Author1", "category": "science"},
    {"title": "Title tow", "author": "Author2", "category": "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}/")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return "not found"


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{author_name}")
async def read_category_by_query(author_name: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == author_name.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {"dynamic_param": dynamic_param}
