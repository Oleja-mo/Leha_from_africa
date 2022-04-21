from flask import Flask
from flask_restful import Api
from data import db_session


class MyApp(Flask):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
        db_session.global_init("db/blogs.db")
        #self.register_blueprint(news_api.blueprint)
        self.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
        self.config['JSON_AS_ASCII'] = False
        self.api = Api(self)


app = MyApp(__name__)