"""
我是通过 uv 管理虚拟环境的

1. 创建虚拟环境
    uv venv

2. 初始化项目
    uv init

3. 激活虚拟换将

    windows 电脑
    .venv/Scripts/activate

    mac 电脑
    source .venv/bin/activate

4. 安装依赖
    uv add "fastapi[standard]"

5.关闭虚拟环境
    deactivate
"""

# 运行第一个 fastapi 项目
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# 如果当前文件是 main.py 文件，就不需要写下面的代码
# 直接运行 fastapi dev 就可以运行
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


"""
访问地址 http://127.0.0.1:8000/

页面上会出现下面内容

{
    "Hello": "World"
}

访问地址 http://127.0.0.1:8000/docs

查看对应接口的文档地址
"""