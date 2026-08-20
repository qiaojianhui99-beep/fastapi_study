from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
1. 默认值
    参数后面冒号跟类型，等号后面跟的是默认值

    访问地址: http://127.0.0.1:8000/items/

    对应参数的数据：skip=0, limit=10

    访问地址: http://127.0.0.1:8000/items/?skip=20

    对应参数的数据：skip=0, limit=20（使用地址中传递的参数）

"""


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


"""
2. 可选参数
    定义类型的时候，使用 | 分割，定义 None，即可声明可选参数
"""


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


"""
3. 查询参数类型转换
    可定义 bool 布尔类型的数据，

    short 传递下方的数据，会被转换成 True
    ?short=true
    ?short=1
    ?short=True
    ?short=on
    ?short=yes

    short 传递下方的数据，会被转换成 False
    ?short=false
    ?short=0
    ?short=False
    ?short=off
    ?short=no

    short 不传递的话，默认是 False
"""


@app.get("/items/type/{item_id}")
async def read_item_type(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


"""
4. 多个路径和查询参数
    FastAPI 可以识别同时声明的多个路径参数和查询参数。
    而且声明查询参数的顺序并不重要。
    FastAPI 通过参数名进行检测：
"""


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int,
        item_id: str,
        q: str | None = None,
        short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )


"""
5. 必填参数
    设置参数的时候，不设置默认参数，那么就是必填参数
    下面的代码中，如果访问地址  http://127.0.0.1:8000/items/foo-item
    并未传递 needy 会出现报错的问题，缺失参数

    如果访问地址 http://127.0.0.1:8000/items/foo-item?needy=sooooneedy 
    这个样子传递就是正常的访问了

    当然，必填参数和可选参数可以同时使用的！
"""


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item