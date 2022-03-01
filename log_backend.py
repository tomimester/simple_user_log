from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from time import gmtime, strftime
from datetime import datetime
import random

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {
    "origins":["https://yourwebsite.com","https://yoursubdomain.yourwebsite.com"],
    "methods": "POST",
    "allow_headers":"*"}})

@app.route("/d36t/", methods=['POST'])
def logtest():
    if (request.origin == "https://yourwebsite.com" or request.origin == "https://yoursubdomain.yourwebsite.com") and request.headers['User-Type'] == "none":
        a = str(request.get_data()).replace('nehezazelet','\t')
        logtime = datetime.utcnow().strftime('%Y-%m-%d\t%H:%M:%S.%f')[:-3]
        #ip = request.headers.get(request.remote_addr) #('X-Forwarded-For', request.remote_addr)
        if request.headers.getlist("X-Forwarded-For"):
            ip = request.headers.getlist("X-Forwarded-For")[0]
            ip = ip.split(',')[0].split('.')
            ip[2] = 'xxx'
            ip[3] = 'xxx'
            ip = '.'.join(ip)
        else:
            ip = request.remote_addr
        useragent = request.headers['User-Agent']
        file_name = datetime.utcnow().strftime('%Y-%m-%d-%H')
        full_path = "/home/tomi/logproject/yourwebsite_log/" + file_name
        ip_log = open(full_path, 'a+')
        ip_log.write(logtime + '\t' + ip + '\t' + a + '\t' + useragent + '\n')
        ip_log.close()
        return('hi')
    else:
        return("error")

@app.route('/amialive/')
@cross_origin()
def api():
    return('yes')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
