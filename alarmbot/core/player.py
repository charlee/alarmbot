from subprocess import Popen
from django.conf import settings

def play_mp3(file):
    p = Popen([settings.MP3_PLAYER, file])
