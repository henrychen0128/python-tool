from flask import Flask,request,jsonify
import time
import json
import hmac
import hashlib
import requests
import requests.packages.urllib3
from werkzeug.wrappers import Response
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)

@app.route('/test1', methods=['POST'])
def content_notebook1():
  while(1):
   print(1)
  return 'test1'

@app.route('/test2', methods=['POST'])
def content_notebook2():
  return Response(json.dumps({"test":"test1"}),status=200,content_type='application/json')


if __name__ == '__main__':
    app.run(
      debug=True,
      host='0.0.0.0',
      port = 8080  
    )
