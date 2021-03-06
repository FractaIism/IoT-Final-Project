#This 檔案 uses UTF-8  Filename: w80.py  # 只是為了方便記得這檔案是否用 port 80
#  coding=utf-8   #這是第二列; 注意 coding 句子只在前兩列才有效 !
myPort = 8080
## 請在這檔案的目錄建立兩個子目錄: static 和 templates   (注意最後有 s)
from flask import Flask, request
from flask import render_template, redirect, send_file

app = Flask(__name__)
from flask_cors import CORS, cross_origin   #其實這些跨域支援的部分都可以不要
CORS(app, resources=r"/*")
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/")
@cross_origin("*")
def webRoot( ):
   return '<font color=Red size=7>Hello World!  &nbsp; &nbsp; 這是網站喔 !</font>'
   '''try:
      return render_template('index.html') 
   except:
      try:
         return app.send_static_file('index.html')  # this file is /static/index.html
      except:
         return "<h1 style='color:red;'>No index.html in templates and static</h1>", 404 '''

@app.route('/abc/')
@app.route('/abc')     # 這列可不寫, 但寫了可以避免最後沒打 "/" 會多轉址一次 
def justAuniqueFunction():
  try:
    return render_template('haha.html')   # 記得要放 templates 子目錄內 (注意最後有 s)!!!
  except: return "<h1 style='color:Red' >找不到 haha<font color=black>haha.html</font> 喔!</h1>",404


import os
from flask import send_from_directory
@app.route("/favicon.ico")
def helloGiveIC( ):  # FAVorite ICON 是微軟發明的 ; 建議 32x32 .jpg or .png 
   # return send_file('static/myicon.png')     # 注意是 static, 不是 /static  (沒有 / )
   try:    # 先試 /static/myicon.png 看看有沒有?
       return send_from_directory(os.path.join(app.root_path, 'static'),
             'myicon.png', mimetype='image/vnd.microsoft.icon')
   except:  # 試 web 根目錄的 myic.png  (故意用不同檔案名稱)
       return send_from_directory(app.root_path,
             'myic.png', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":    # 注意瀏覽器的網址列要用 127.0.0.1:port 不是 0.0.0.0
   app.run( '0.0.0.0' , port=myPort, threaded=True, debug=True)    # 如 port 是 80 則可不用打 :80; debug 使其自動重跑