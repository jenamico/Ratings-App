import model
import csv
from datetime import datetime



#-------------------------#
# populate Users table
#-------------------------#
# def load_users(session):
def load_users(filepath):
    # get a session started
    session = model.connect()

    # use u.user for ID, age, zip
    # email and password not in data set
    with open(filepath, 'rb') as u_file:
        # open a file
        user_data = csv.reader(u_file, delimiter='|')
        # read a line
        for row in user_data:
            # parse a line
            user_id = row[0]
            user_age = row[1] 
            user_zip = row[4]
            # create an object with the given seed data
            this_user_object = model.User(id = user_id, age = user_age, zipcode = user_zip)
            # add the object in THIS row to a session
            session.add(this_user_object)
        # commit all the rows
        session.commit()

##testing: call user function here:
# load_users("./seed_data/u.user")


#-------------------------#
# populate Movies table
#-------------------------#
#def load_movies(session):
def load_movies(filepath):
    # get a session started, yo.
    session = model.connect()

    # use u.item
    with open(filepath, 'rb') as m_file:
        # open a file
        movie_data = csv.reader(m_file, delimiter='|')
        # read a line
        for row in movie_data:
            # parse a line
            movie_id = row[0]
            """
            TODO: remove date from movie title
            """            
            title = row[1]
            title = title.decode("latin-1")
            imdb_url = row[4]

            # get date, with conditional for blank entries in data
            release_date_string = row [2]
            # print "release_date_string: ", release_date_string, "\n"
            if release_date_string == "":
                print "no date found"
                release_date = None
                # print "release_date: ", release_date
            else:
                # process the date string into a $#%@#^@# datetime object
                release_date = datetime.strptime(release_date_string, "%d-%b-%Y")
            # print "release_date: ", release_date

            # create an object with the given seed data
            this_movie_object = model.Movie(id = movie_id, movie_title = title, release = release_date, imdb_url= imdb_url)

            # add the object in THIS row to a session
            session.add(this_movie_object)
            # repeat until done
        
        # commit all the rows
        session.commit()

##testing: call movie function here:
# load_movies("./seed_data/u.item")


#-------------------------#
# populate Ratings table
#-------------------------#
# def load_ratings(session):
def load_ratings(filepath):
    # use u.data

    # get a session started
    session = model.connect()

    with open(filepath, 'rb') as r_file:
        # open a file
        ratings_data = csv.reader(r_file, delimiter='\t') # this file uses TABS as spacers
        # read a line
        for row in ratings_data:
            # parse a line
            row_movie_id = row[1]    
            row_user_id = row[0]
            row_rating = row[2]

            # find the corresponding movie id and user id
            # create an object with the given seed data
            # do not need to pass rating_id -- will auto-increment as set up in Class def
            this_rating_object = model.Rating(movie_id = row_movie_id, 
                                            user_id = row_user_id, this_rating = row_rating)
            # add the object in THIS row to a session
            session.add(this_rating_object)
        # commit all the rows
        session.commit()

##testing: call user function here:
load_ratings("./seed_data/u.data")



#-------------------------#
# PULL IT ALL TOGETHER AND RUN
#-------------------------#
def main(session):
    # You'll call each of the load_* functions with the session as an argument
    """
    load_users(session)
    load_movies(session)
    load_ratings(session)
    """
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)


"""
NOTE!!!! DO NOT FORGET THIS!!!!
*****
in the event that db needs to be deleted and rebuilt:

remember to do this in interactive python shell
(python -i model.py)

engine = create_engine("sqlite:///ratings.db", echo=True)
Base.metadata.create_all()

"""