# -*- coding: utf-8 -*-

from typing import Union

import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def predict(
        text: str = Body(..., description="待预测文本text"),
        k: int = Body(1, description="TopK的值", examples=[3, 5])
):
    print("调用predict方法......")
    # TODO: 调用模型预测推理逻辑得到结果，结果类似假定为字典
    pred_result = {}

    # 拼接返回最终值
    return {'code': 0, 'msg': '成功', 'data': pred_result, 'text': text, 'k': k}


app.post("/predict", summary="Predict预测接口")(predict)

if __name__ == '__main__':
    # http://127.0.0.1:9001/docs
    uvicorn.run(app, host="0.0.0.0", port=9001, log_level="info")
