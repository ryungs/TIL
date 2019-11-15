import random

from flask import Flask, jsonify # Flask 앞에 대문자라서 class이다

app = Flask(__name__)

@app.route('/') # 고급문법, 데코레이터라고 부른다 '/'는 루트라고 부른다
def index():
    return 'Hi!'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

    
    
@app.route('/hi/<string:name>')
def hi(name):
    return (f'hi {name}!')



if __name__ == '__main__': 
    app.run(debug=True)