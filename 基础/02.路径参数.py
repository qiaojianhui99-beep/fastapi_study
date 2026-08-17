from fastapi import FastAPI
import uvicorn

app = FastAPI()

"""
1. 路径参数
    访问地址 http://127.0.0.1:8000/items/123
    会得到下面的内容

{
    "item_id": "123"
}
"""
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


"""
2. 路径参数定义类型
    访问地址 http://127.0.0.1:8000/items1/123
    会得到下面的内容
    
    {
        "item_id": 123
    }
    
    因为这里配置了参数 item_id 的类型是 int，数字类型，接收的时候会自动转换成 数字类型的
    
    如果说这个时候你传递了一个字符串或者浮点类型的数据，就会出现转换错误的提示
    
    当访问 http://127.0.0.1:8000/items1/asd 这个地址的时候：
    {
        "detail": [
            {
                "type": "int_parsing",
                "loc": [
                    "path",
                    "item_id"
                ],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "input": "asd"
            }
        ]
    }
"""
@app.get("/items1/{item_id}")
async def read_item1(item_id: int):
    return {"item_id": item_id}


"""
3. 书写接口的顺序
    代码执行是从上到下依次执行的，如果找到相符的路径，就不会往下找了
    下面的代码就是，永远都是执行第一个函数，不会执行第二个
"""

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
"""
    有的时候，路径和动态参数可能是混写的，入下方的代码
    如果访问 /users/me ，就会执行对应的函数
    如果 /users/ 后面的参数不是 me ，他就会走后面的路径代码
    但是这两个代码的位置不能互换，因为如果互换了，永远都走不到 /users/me 这个路径代码里面了，
    me 会被当做参数，传入到  /users/{user_id} 这个路径里面
"""

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}





# 如果当前文件是 main.py 文件，就不需要写下面的代码
# 直接运行 fastapi dev 就可以运行
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)