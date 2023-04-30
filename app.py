from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


class AddUser():
    def __init__(self, login, password1, password2, email):
        self.login = login
        self.password1 = password1
        self.password2 = password2
        self.email = email
class Checker:
    def check_login(self):
        import string
        flag = False
        if len(self.login) > 5:
            for s in self.login:
                if s in string.ascii_letters:
                    flag = True
                else:
                    flag = False
                    break
        return flag

    def check_password(self):
        if len(self.password1) > 5 and self.password1 == self.password2:
            return True
        else:
            print('Пароли не совпадают')
            return False

    def check_email(self):
        if self.email.count('@') == 1:
            return True
        else:
            print('Емейл не содержит @')
            return False

    def saveUSer(self):
        if self.check_login() and self.check_password() and self.check_email():
            return True
        else:
            print('Данные не верны')

@app.route('/registration-user', methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        login = request.form['login']
        password1 = request.form['password1']
        password2 = request.form['password2']
        email = request.form['email']
        user = AddUser(login, password1, password2, email)


    return render_template('registration-user.html')


@app.route('/posts')
def posts():
    return render_template('posts.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)

