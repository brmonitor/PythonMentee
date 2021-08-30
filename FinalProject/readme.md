##### How to run the Final Project code

**Programs and files**
1. DB_creation.py : Create **news_feed.db** with **sites** (and insert the 3) and **news_feeds** tables
2. News_fetcher.py : Fetch the news from the 3 sites 
3. Show_Feeds.py  : Flask app to show the feeds in the **show_feeds.html** template  
4. Models.py : SQLAlchemy needed to the **Show_Feeds2.py** below 
5. Show_Feeds2.py : Flask app, Show_Feeds.py's SQLAlchemy ORM version. It uses the **show_feeds2.html** template
6. news_feed.db : db created using programs 1 and 2 

To test you may just download the files and run **Show_Feeds.py** or **Show_Feeds2.py** in PyCharm, then you will be using
the news_feed.db and no need to run programs 1 and 2 above 
