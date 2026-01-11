def make_album(artist_name, album_title, number_of_songs=None):
    """返回一个字典，包含专辑的信息"""
    album_dict = {
        "artist": artist_name.title(),
        "title": album_title.title(),
    }
    if number_of_songs:
        album_dict["songs"] = number_of_songs
    return album_dict


album = make_album("metallica", "ride the lightning")
print(album)
album = make_album("pink floyd", "the dark side of the moon")
print(album)
album = make_album("the beatles", "abbey road", 16)
print(album)
