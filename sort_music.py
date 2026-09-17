songs = [
    {"title": "Golden Hour", "artist": "JVKE", "genre": "Pop", "views": 980000},
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "views": 2500000},
    {"title": "Snooze", "artist": "SZA", "genre": "R&B", "views": 1200000},
    {"title": "N95", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "views": 850000},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop", "views": 2100000},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "views": 1750000}
]

def sort_by_views(songs):
    res = songs.copy()
    pass

def sort_by_favourite_genre(songs, favourite_genre):
    res = songs.copy()
    pass

print("=== SORT BY VIEWS ===")

result_views = sort_by_views(songs)

for song in result_views:
    print(song["title"], "-", song["views"], "views")


print("\n=== SORT BY FAVOURITE GENRE ===")

favourite_genre = "R&B"

result_genre = sort_by_favourite_genre(songs, favourite_genre)

for song in result_genre:
    print(song["title"], "-", song["genre"])