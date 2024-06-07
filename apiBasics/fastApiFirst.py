from enum import Enum
#adds further support for enums


from fastapi import FastAPI, HTTPException
#it is the api 

from pydantic import BaseModel
#data validation tool 
# Fast api relies on pydantic 


app = FastAPI()

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category



 ##it is a mock database in this example we can use sql instead of this 
items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}
# it is a dictonary but fast api changes it to a json when we want it 

# FastAPI handles JSON serialization and deserialization for us.
# We can simply use built-in python and Pydantic types, in this case dict[int, Item].


 ##end pointler bunlar 
## şimdi buraya yapılan request bize itemleri returnledi 
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int  ) -> Item:
    if item_id not in items : #mevcut olmayan bir numara istendiyse
        # html hasta sayfası fast api içinden gelir 
        raise HTTPException(
            status_code=  9182, detail=f'item with {item_id=} does not exist'
        )
    return items[item_id]
#in defination (item_id : int ) defines that input must be and integer
#and the -> item means return type will be an item object in docs but it doesnt enforce it 

# isme bağlı search için

Selection = dict[str,str|int|float|Category|None] #possible arguments for filtering search
#optional parameters for search filters 



#gets items?name= type search 
@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    """ gets parameters optionally either give name or none  """
    def check_item(item: Item):
        """helper gunction to Check if the item matches the query arguments from the outer scope. 
        if you look for ?safetouse=true it will stop since there are no such value """
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
    #list comprehension to filter out requested search results
    selection = [item for item in items.values() if check_item(item)]
    #retuns values 
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }

@app.get("/hackername")
def index():
    return {"swiper no hacking"}



#### https://www.youtube.com/watch?v=SORiTsvnU28&t=483s&ab_channel=ArjanCodes