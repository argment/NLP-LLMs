# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    最终对外提供一个模型预测方法，
    该预测方法需要实现的内容就是：
        1. 接受调用方传递过来的请求参数；
        2. 在该方法内部对数据进行处理、调用模型；
        3. 最后返回结果
    :return:
    """
    try:
        text = None
        if request.method == 'GET':
            print("当前接口调用方式为GET")
            # 当请求方式为GET的时候，参数直接从request.args(args是一个字典)中按照参数名称直接获取即可
            text = request.args.get('text')
        elif request.method == 'POST':
            print("当前接口调用方式为POST")
            # 当请求方式为POST的时候，一般的参数直接从request.form(form是一个字典)中按照参数名称直接获取即可
            # 当请求方式为POST的时候，如果传递的数据为文件的话，需要从request.files中获取
            text = request.form.get('text')
            print(request.form)
            print(request.files)
        else:
            print("当前请求方式是不支持的.")

        if text is None:
            # 结果返回的时候，一般返回一个json对象即可
            return jsonify({'code': 1, 'msg': '请以get或者post的请求方式给定参数text.'})

        # TODO: 调用模型预测推理逻辑得到结果，结果类似假定为字典
        pred_result = {}

        # 拼接返回最终值
        return jsonify({'code': 0, 'msg': '成功', 'data': pred_result, 'text': text})
    except Exception as e:
        return jsonify({'code': 2, 'msg': f'服务器异常:{e}.'})


if __name__ == '__main__':
    #
    app.run(
        host="0.0.0.0",  # 给定当前启动的flask服务监听的IP地址是什么
        port=5000,  # 给定当前启动的服务监听哪个端口
        debug=False
    )
