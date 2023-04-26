from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    # Для выполнения ДЗ, потом удалю
    global constant
    for i in range(randint(1, 20)):
        constant.append(randint(-50, 50))
    return render_template('index.html', constant=constant)

@app.route('/hw2')
def hwDelete():
    '''
    Функция удаляет со списка элемент и возвращает его, передает в рендер шаблона, где он выводится
    :return: удаленный элемент списка
    '''
    global constant
    if len(constant):
        elem = constant.pop()
    return render_template('hw2.html', elem=elem)


@app.route('/posts')
def posts():
    return render_template('posts.html')


if __name__ == '__main__':
    constant = []
    app.run(host="0.0.0.0", port=10000, debug=True)


