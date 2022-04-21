from flask import render_template

from app import app
from api.news import NewsListResource, NewsResource, News
from api.register_login import RegisterRes, LoginRes
from data import db_session

'''@app.route('/', defaults={'path': ''})
@app.route('/a/<path:path>')
@app.route('/u/<path:path>')
@app.route("/")
def root(path):
    return app.send_static_file('index.html')'''


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News)
    return render_template("index.html", news=news)


app.api.add_resource(NewsListResource, '/api/v2/news')
app.api.add_resource(NewsResource, '/api/v2/news/<int:news_id>')

app.api.add_resource(RegisterRes, '/api/register')
app.api.add_resource(LoginRes, '/api/login')
# main_app.api.add_resource(NewsList, '/api/news')
if __name__ == '__main__':
    app.run()
