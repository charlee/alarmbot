import os
from django.conf import settings

def get_voice_path(id):
    return os.path.join(settings.VOICE_DIR, 'voice-%s.mp3' % id)

