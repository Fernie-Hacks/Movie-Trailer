import webbrowser

#Movie Class
class Movie():
    #Adds a basic documentation to the class
    """ This class provides a way to store movie related information """

    #Constructor initializes all instance variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #The instance method show_trailer opens a web browser.
    #The link is the youtube movie trailers in the form of a string.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)        
        
