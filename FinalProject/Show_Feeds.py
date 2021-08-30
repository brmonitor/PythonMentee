# Python Mentee - Final Project
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# A Web Server to fetch the latest news from the database and show them on the page, with links that take the user to
#   the original post on the source website.

#       _ You can just have a simple page to show the latest news, fetching them from the database.
#       _ Don't worry too much about Styles, that's not the intent of this challenge. Just showing the news on a simple
#           HTML page should be good enough.
#       _ Try to use a click track url, so u know how many people clicked on the news to see them on the original site.

import sqlite3
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def show_feeds():
    conn = sqlite3.connect("news_feed.db")
    c = conn.cursor()
    names = []
    lines = []

    for name in ["techcrunch", "mashable"]:
        names.append(name)
        c.execute(f"SELECT id FROM sites WHERE name = '{name}'")
        id = c.fetchone()[0]
        c.execute(f"SELECT published, title, link, published_parsed_secs FROM news_feeds WHERE site_id = '{id}' LIMIT 4")
        lines.append(c.fetchall())
    conn.close()

    return render_template('show_feeds.html', names=names, lines=lines)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
