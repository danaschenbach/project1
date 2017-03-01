import fresh_tomatoes  
import media           

# create instances of class Movie found in media module
# commented out portion from instructor
#toy_story = media.Movie("Toy Story",
#                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
#                       "https://www.youtube.com/watch?v=vwyZH85NQC4")

#avatar = media.Movie("Avatar",
#                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
#                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#school_of_rock = media.Movie("School of Rock",
#                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
#                             "httpws://www.youtube.com/watch?v=3PsUJFEBC74")

#ratatouille = media.Movie("Ratatouille",
#                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
#                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#midnight_in_paris = media.Movie("Midnight in Paris",
#                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
#                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

#hunger_games = media.Movie("Hunger games",
#                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
#                           "https://www.youtube.com/watch?v=PbA63a7H0bo")
# original code ... well except for the links
a = media.Movie("The Incredible Hulk",
    "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xbqNb2PFKKA")
b = media.Movie("The Avengers",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://youtu.be/eOrNdBpGMv8")
c = media.Movie("Hell and back",
    "https://upload.wikimedia.org/wikipedia/en/2/26/Hell_and_Back_Movie_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=HtWHUpRXl2E")
d = media.Movie("Monty Python and the Holy Grail",
    "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",  # NOQA
    "https://www.youtube.com/watch?v=QSo0duY7-9s")
# instructor portion commented out
#movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]  # NOQA
# generates html page
movies = [a, b, c, d]
fresh_tomatoes.open_movies_page(movies)
            
