import webbrowser


class Movie():
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def showTrailer(self):
        webbrowser.open(self.trailer)