from google.cloud import translate_v2 as translate
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'sharp-harbor-306003-4a27401f8846.json'
client = translate.Client()

print(client.detect_language("Bonjour"))


def translate_to_English(text):
    result = client.translate(text, target_language='en')
    return result["translatedText"]

def detect_language(text):
    return client.detect_language(text)

def translate_to_other_language(text, target):
    result = client.translate(text, target_language=target)
    return result["translatedText"]


