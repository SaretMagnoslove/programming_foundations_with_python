import webbrowser


class Movie():
    """ class for storing information about movies """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def showTrailer(self):
        webbrowser.open(self.trailer)
