from flask import Flask

app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def my_voca(word):
    voca = {'apple': '사과', 'banana': '바나나'}
    
    for key, values in voca.items():
        
        if word in voca.keys():
            return (f'{key}은(는) {values}!')
        else:
            return (f'{word}은(는) 나만의 단어장에 없는 단어입니다!')

if __name__ == '__main__': 
    app.run(debug=True)