import webbrowser

class Movie ():
    """creating instances and generating output as a trailer"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """creating space in memory for details"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
		
    def show_trailer(self):
        """opens web browser for youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)