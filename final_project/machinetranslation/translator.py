import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' This function translates input english text to French'''

    translated_text = language_translator.translate(
    english_text,model_id='en-fr').get_result()
    a_list= translated_text["translations"]
    t_list = a_list[0]
    french_text = t_list["translation"]
    return french_text


def french_to_english(french_text):
    ''' This function translates input french text to English'''

    translated_text = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    a_list= translated_text["translations"]
    t_list = a_list[0]
    english_text = t_list["translation"]
    return english_text

