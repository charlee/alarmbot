from google.cloud import texttospeech
from google.oauth2 import service_account
from django.conf import settings


LANGUAGE_MAPPING = {
    'en-US': {
        'language_code': 'en-US',
        'name': 'en-US-Wavenet-F',
    },

    'zh-CN': {
        'language_code': 'cmn-CN',
        'name': 'cmn-CN-Wavenet-D',
    },
}


def generate_tts_voice(text, output_file, language='en-US'):

    credentials = service_account.Credentials.from_service_account_file(settings.GOOGLE_CLOUD_CREDENTIALS_FILE)
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    synthesis_input = texttospeech.SynthesisInput(text=text)

    language_params = LANGUAGE_MAPPING.get(language)

    voice = texttospeech.VoiceSelectionParams(**language_params)

    audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_file, 'wb') as out:
        out.write(response.audio_content)
  
