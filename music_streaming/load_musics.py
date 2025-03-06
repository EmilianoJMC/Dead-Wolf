import os
import django

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_streaming.settings')
django.setup()

from music_app.models import Album, Music

MUSICS_PATH = r""C:\Users\Miza\Downloads\Dead Wolf""

def load_musics():
    for album_name in os.listdir(MUSICS_PATH):
        album_path = os.path.join(MUSICS_PATH, album_name)
        if os.path.isdir(album_path):
            album, created = Album.objects.get_or_create(title=album_name)
            for music_file in os.listdir(album_path):
                music_path = os.path.join(album_path, music_file)
                if os.path.isfile(music_path):
                    Music.objects.get_or_create(
                        title=os.path.splitext(music_file)[0],
                        album=album,
                        file_path=music_path
                    )
            print(f'Album "{album_name}" processed.')

if __name__ == '__main__':
    load_musics()
