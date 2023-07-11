from flask import Flask

app = Flask (__name__)

@app.route('/')
def main():
    return "<h1>Hello, chuvack</h1><dr><a href='/index'>страница 2</a"

@app.route('/index/<x>/<y>')
def index(x,y):
    return f'res: {int(x) + int(y)}' +' Питон начло проекта'

if __name__=='__main__':
    app.run()