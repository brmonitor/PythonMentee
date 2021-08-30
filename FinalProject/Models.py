# Python Mentee - Final Project
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# SQLAlchemy source for the Final Project
# source : SQLAlchemy ORM - https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_mapping.htm


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///news_feed.db', echo=True)
Base = declarative_base()


class Sites(Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url_feed = Column(String, nullable=False)
    newsfeeds = relationship("NewsFeeds", back_populates="sites")


class NewsFeeds(Base):
    __tablename__ = 'news_feeds'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    published = Column(String, nullable=False)
    published_parsed_secs = Column(REAL, nullable=False)
    site_id = Column(Integer, ForeignKey('sites.id'))
    sites = relationship("Sites", back_populates="newsfeeds")
