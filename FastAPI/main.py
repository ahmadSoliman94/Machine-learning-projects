# import fastapi
from fastapi import FastAPI

# create a FastAPi instance
app = FastAPI()


# Define a path operation decorator
# @app.get('/') # (/): is the path

# # create path operation function
# def index():
#     # we can use dictionary as a value 
#     return {'data': {'name':'Ahmad'}}

# # to have a route exmpale: localhost:8000/about
# @app.get('/about')
# def about():
#     return {'data': {'about page'}}

''' 1. Path Parameters:'''

# @app.get('/')
# def index():
#     return {'data': 'blog list'}

# # to fetch single blog like '/blog/id'
# @app.get('/blog/{id}')

# def show(id):

#     # fetch blog with id = id
#     return {'data':id}

# # another example
# @app.get('/blog/{id}/comments')

# def comments(id):

#     # fetch comments of blog with id = id
#     return {'data': {'Hello', 'World'}}

# 1.1. Path parameters with types

# @app.get('/')
# def index():
#     return {'data': 'blog list'}

# # to fetch single blog like '/blog/id'
# @app.get('/blog/{id}')

# def show(id:int):

#     # fetch blog with id = id
#     return {'data':id}

# # another example
# @app.get('/blog/{id}/comments')
# def comments(id):

#     # fetch comments of blog with id = id
#     return {'data': {'Hello', 'World'}}


''' 2. API Docs - Swagger '''

# to check valid vsalues. 
# to check Response headers: content-length and type, Date, Server-type

''' 3. Query Parameters '''

# if we need to get for example only 10 published blog
# @app.get('/blog')
# def index(limit, published):

#     # only get 10 published blogs
#     if published:
#         return {'data': f'{limit} published blogs from the db'}
#     else:
#         return {'data': f'{limit}  blogs from the db'}

# # with default values: 
# from typing import Union

# @app.get('/blog')
# def index(limit=10, sort: Union[str, None] = None, published:bool = True):

#     # only get 10 published blogs
#     if published:
#         return {'data': f'{limit} published blogs from the db'}
#     else:
#         return {'data': f'{limit}  blogs from the db'}

''' 4. Request Body '''

# Import Pydantic's BaseModel
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# Create data model, that inherits from BaseModel.
# class Item(BaseModel): 
#     name: str
#     description: Union[str, None] = None # optional default patametrs
#     price: float
#     tax: Union[float, None] = None

# # Declare it as a parameter
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# note: useing Automatic docs to create items and see the results

# Use the model: 
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax # we can access all the attributes of the model object directly
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# Request body + path + query parameters

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# app = FastAPI()


# @app.put("/items/{item_id}") # put: to update the data
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

''' Query Parameters and String Validations '''

#example: to enforce that 1 is optional and its length not more 20 characters

# from typing import Union

# # import Query
# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")

# # Use Query as the default value
# async def read_items(

#     # if i remove Union[....] and just write q: str = ... then it will be requierd
#     q: Union[str, None] = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$") # add more validation: min_length, regex
#     ):

    
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

''' Path parameters and Numeric Validations'''

from typing import Union

# Import Path
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    # declare a title metadata value for the path parameter item_id
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results