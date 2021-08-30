# Python Mentee - Final Project
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# A Web Server to fetch the latest news from the database and show them on the page, with links that take the user to
#   the original post on the source website.

#       _ You can just have a simple page to show the latest news, fetching them from the database.
#       _ Don't worry too much about Styles, that's not the intent of this challenge. Just showing the news on a simple
#           HTML page should be good enough.
#       _ Try to use a click track url, so u know how many people clicked on the news to see them on the original site.
# *** This is a copy of Show_Feeds.py but using SQLAlchemy ***
# source : SQLAlchemy ORM - https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_mapping.htm

from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Models import Sites, NewsFeeds

app = Flask(__name__)

engine = create_engine('sqlite:///news_feed.db', echo=False)
Base = declarative_base()


@app.route('/')
def show_feeds():
    names = []
    lines = []

    Session = sessionmaker(bind=engine)
    session = Session()
    for name in ["techcrunch", "mashable"]:
        names.append(name)
        ss = session.query(Sites).filter(Sites.name == name).all()
        id = ss[0].id

        ss = session.query(NewsFeeds).filter(NewsFeeds.site_id == id).all()
        lines.append(ss)
        session.close()
    return render_template('show_feeds2.html', names=names, lines=lines)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
