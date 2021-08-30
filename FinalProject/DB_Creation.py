# Python Mentee - Final Project
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# A Python script that takes care of fetching the latest news and saving them to the database
#   _ A database to fetch the news from the websites above on a regular basis

import sqlite3


def create_db_tables():
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect("news_feed.db")
    c = conn.cursor()

    # site table
    create_site_table_sql = """CREATE TABLE IF NOT EXISTS sites (id integer PRIMARY KEY,  
                                                                name text NOT NULL, 
                                                                url_feed  text NOT NULL);"""
    c.execute(create_site_table_sql)

    # news_feed table
    create_news_feed_table_sql = """CREATE TABLE IF NOT EXISTS news_feeds (  id      integer PRIMARY KEY,  
                                                                            title   text NOT NULL, 
                                                                            link   text NOT NULL,
                                                                            published text NOT NULL, 
                                                                            published_parsed_secs real NOT NULL,
                                                                            site_id integer NOT NULL,
                                                                            FOREIGN KEY (site_id) REFERENCES sites (id)
                                                                            );"""
    c.execute(create_news_feed_table_sql)

    # inserting the 3 sites
    insert_site_sql = "INSERT INTO sites(name, url_feed) VALUES(?,?);"
    sites = [{'name': 'techcrunch', 'url_feed': 'https://techcrunch.com/feed'},
             {'name': 'mashable',   'url_feed': 'https://mashable.com/feed'},
             {'name': 'theverge',   'url_feed': 'https://www.theverge.com/feed'}]

    for s in sites:
        c.execute(insert_site_sql, [s['name'], s['url_feed']])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_db_tables()
