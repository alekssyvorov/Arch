from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    # Для выполнения ДЗ, потом удалю
    global constant
    for i in range(randint(1, 20)):
        constant.append(randint(-50, 50))
    return render_template('index.html', constant=constant)

@app.route('/hw2')
def hw():
    global constant
    elem = constant.pop()
    print(elem)
    return render_template('hw2.html', elem=elem)


@app.route('/posts')
def posts():
    return render_template('posts.html')


if __name__ == '__main__':
    constant = []
    app.run(host="0.0.0.0", port=10000, debug=True)

