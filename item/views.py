from django.shortcuts import render
from .models import Album, Locale, Song
from pprint import pprint
from . import json

# Create your views here.
def get_json(request):
    my_files = json.files
    pprint(len(my_files))
    # locales = set()
    # for fi in my_files:
    #     pprint(fi["locales"])
    #     for aa in fi["locales"]:
    #         locales.add(aa)
    # print(locales)
    # for loc in locales:
    #     print(loc)
    #     locale = Locale()
    #     locale.locale_name = loc
    #     locale.save()
    
    # # 앨범
    # for item in my_files:
    #     # pprint(item)
    #     album = Album()
    #     album.album_title = item["album_title"]
    #     album.save()
    #     # print()
    #     for locale_name in item["locales"]:
    #         # print(locale_name)
    #         locale = Locale.objects.get(locale_name=locale_name)
    #         album.locales.add(locale)

    # song
    for item in my_files:
        # pprint(item)
        album_title = item["album_title"]  # 앨범이름
        # song = Song()
        print()
        for song in item["songs"]:
            print(song)
            song_ob = Song()
            song_ob.title = song["title"]
            song_ob.length = song["length"]
            song_ob.track = song["track"]
            song_ob.album = Album.objects.get(album_title=album_title) 
            song_ob.save()
            

    return None

