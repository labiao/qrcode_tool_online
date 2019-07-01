import flask
import qrcode
import time
app = flask.Flask(__name__)

@app.route('/')
def home():
#     # 第一步：获取要生成二维码的数据
#     data = flask.request.args.get("data")
#     # 第二部：生成二维码图像
#     img = qrcode.make(data)
#     img.save(r"F:\武汉纺织大学Python实训\day6\代码\qrcode_tool_online\static\qr.png")

#     # 第三步：在页面上显示二维码图片
#     f = open("index.html", "r", encoding="utf-8")
#     data = f.read()
#     f.close()
#     return data
    # return '<img src="/static/qr.png" />' 

    return flask.render_template('qr_tool.html')


@app.route('/qr', methods=["POST"])
def qr():
    # 第一步：获取要生成二维码的数据
    data = flask.request.form.get("data")
    # 第二部：生成二维码图像
    img = qrcode.make(data)
    img.save(r"F:\武汉纺织大学Python实训\day6\代码\qrcode_tool_online\static\qr.png")
    # 第三步：在页面上显示二维码图片
    # f = open("index.html", "r", encoding="utf-8")
    # data = f.read()
    # f.close()
    return '<img src="/static/qr.png" />' 
    

if __name__ == '__main__':
    app.run(debug=True)