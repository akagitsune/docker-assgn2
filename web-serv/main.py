from flask import Flask
from flask import request
import redis

r = redis.Redis(host='redisdb')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/add', methods=['GET'])
def add_something():
    key = request.args.get('key')
    value = request.args.get('value')
    r.set(key, value)
    retstr = '[{}]:[{}] added'.format(key, value)
    return retstr

@app.route('/get', methods=['GET'])
def get_something():
    key = request.args.get('key')
    value = str(r.get(key))
    if value is None:
        return 'Value for key {} not found'.format(key)
    retstr = 'Key {} has value {}'.format(key, value)
    return retstr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#print("Hello world!")