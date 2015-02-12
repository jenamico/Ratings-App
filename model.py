from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref 
from sqlalchemy.orm import sessionmaker, scoped_session


ENGINE = None
Session = None 

Base = declarative_base()

### Class declarations go here

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

    def __repr__(self):
        return "%d, %s, %s, %d, %s" % (self.id, self.email, self.password, self.age, self.zipcode)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    movie_title = Column(String(64), nullable = True)
    release = Column(DateTime(timezone = False), nullable = True)
    imdb_url = Column(String(100))

    def __repr__(self):
        return "%d, %s, %s, %s" % (self.id, self.movie_title, self.release, self.imdb_url)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    movie_id = Column(Integer, ForeignKey ('movies.id'), nullable = True)
    user_id = Column(Integer, ForeignKey ('users.id'), nullable = True)
    rating = Column(Integer, nullable = True)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie",backref=backref("movies", order_by=id))

    def __repr__(self):
        return "%d, %d, %d, %d" % (self.id, self.movie_id, self.user_id, self.rating)


### End class declarations

# global ENGINE
# global Session
engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

  


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()