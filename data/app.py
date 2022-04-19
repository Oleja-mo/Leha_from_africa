from flask import Flask

#здесь будет класс нашего приложения (в прошлом переменная app)
class MyApp(Flask):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
