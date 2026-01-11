def make_album(artist_name, album_title, number_of_songs=None):
    """返回一个字典，包含专辑的信息"""
    album_dict = {
        "artist": artist_name.title(),
        "title": album_title.title(),
    }
    if number_of_songs:
        album_dict["songs"] = number_of_songs
    return album_dict


while True:
    print("\nPlease tell me your album:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == "q":
        break
    album_title = input("Album title: ")
    if album_title == "q":
        break
    album = make_album(artist_name, album_title)
    print(album)
