# 导入 fastapi
from fastapi import FastAPI

# 创建一个 fastapi 实例
app = FastAPI()

"""
常用的 HTTP 方法

POST 创建数据
GET 读取数据
PUT 更新数据
DELETE 删除数据
"""

# 创建一个路径
"""
@app.get("/") 告诉 FastAPI 在它下方的函数负责处理如下访问请求：

    请求路径为 /
    使用 get 操作
"""
@app.get("/")
async def root():
    return {"message": "Hello World"}

