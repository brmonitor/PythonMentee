# Python Mentee - Final Project
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# A Python script that takes care of fetching the latest news and saving them to the database

#   _ Create a Python Script that can be run anytime, and it's smart enough to fetch the latest news from the websites
#       and store them in the database.
#   _ Make sure the script doesn't save duplicated news (from the same website, it's okay if two different websites have
#       the same news).
#   _ If Using Flask, you can search for something like "Flask Scripts" that will make it easy to use the flask context
#       to access database and application settings.
#   - Additional Tip: Check if for the websites "Rss" feed, which is a structured way to find latest information,
#       so you don't need to parse HTML from the websites. Example: https://techcrunch.com/feed/

import feedparser
import sqlite3
from time import mktime


def store_feed(name):
    conn = sqlite3.connect("news_feed.db")
    c = conn.cursor()

    c.execute(f"SELECT id, url_feed FROM sites WHERE name = '{name}'")

    id, url_feed = c.fetchone()

    print(id, url_feed)

    news_feed = feedparser.parse(url_feed)

    for e in news_feed.entries:
        #    e = news_feed.entries[1]

        print(name)
        print(e.keys())
        print(e)
        print('title : ', e['title'])
        print('link : ', e['link'])
        # print('links : ', e['links'])
        print('published : ', e['published'])
        pp_secs = mktime(e['published_parsed'])
        print('published_parsed', pp_secs, type(pp_secs))

        #   Insert the news in news_feeds table
        c = conn.cursor()
        c.execute('INSERT INTO news_feeds(title, link, published, published_parsed_secs, site_id) VALUES(?,?,?,?,?)',
                  (e['title'], e['link'], e['published'], pp_secs, id))
    conn.commit()


if __name__ == '__main__':
    store_feed("techcrunch")
    store_feed("mashable")
    # store_feed("theverge")
