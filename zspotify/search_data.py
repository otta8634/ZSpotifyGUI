class Result:
    def __init__(self, index):
        self.index = index


class Track(Result):
    def __init__(self, index, id, title, artists, album="", img="",release_date="", duration=-1,explicit=False):
        super().__init__(index)
        self.id = id
        self.title = title
        self.artists = artists
        self.album = album
        self.img = img
        self.release_date = release_date
        self.duration = duration
        self.explicit = explicit

class Album(Result):
    def __init__(self, index, id, title,artists, total_tracks, release_date="", img="", explicit=False):
        super().__init__(index)
        self.id = id
        self.title = title
        self.artists = artists
        self.img = img
        self.total_tracks = total_tracks
        self.release_date = release_date
        self.explicit = explicit

class Artist(Result):
    def __init__(self, index, id, name, img=""):
        super().__init__(index)
        self.id = id
        self.name = name
        self.img = img

class Playlist(Result):
    def __init__(self, index,id, title,creator, total_tracks, img=""):
        super().__init__(index)
        self.id = id
        self.title = title
        self.creator = creator
        self.total_tracks = total_tracks
        self.img=img
