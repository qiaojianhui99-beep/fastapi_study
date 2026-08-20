from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
1. 通过 pydantic 声明请求体
"""


class Item(BaseModel):
    name: str
    # 可选参数
    description: str | None = None
    price: float
    # 可选参数
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


"""
2. 请求体 + 路径参数
    item_id 就是路径参数
    item 就是请求体中所需的参数
"""


class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item1):
    return {"item_id": item_id, **item.model_dump()}


"""
3. 请求体 + 路径 + 查询参数
    item_id 就是路径参数
    item 就是请求体中所需的参数
    q 就是查询参数
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result: dict[str, int | str | float | None] = {"item_id": item_id, **item.model_dump()}
    if q:
        result["q"] = q  # 直接赋值而不是使用 update
    return result