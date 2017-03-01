import webbrowser

class Movie():  # create the class movie to be used by entertainment_center.py
    def __init__(self, movie_title, poster_image, trailer_youtube):  # define instances within class movie 
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # define operation within class movie
        webbrowser.open(self.trailer_youtube_url)
        
    
