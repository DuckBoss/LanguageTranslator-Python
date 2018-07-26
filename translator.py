from papago import Translator as naver_ts
from googletrans import Translator as google_ts

client_id = "<your client_id>"
client_secret = "<your client_secret>"

papago_translator = naver_ts(client_id, client_secret)
google_translator = google_ts()

to_translate = input("Input something to translate: ")
raw_translate_naver = papago_translator.translate(to_translate)
raw_translate_google = google_translator.translate(to_translate)

translated_lang_naver = raw_translate_naver.text
translated_lang_google = raw_translate_google.text

print("Naver Papago Translation: " + translated_lang_naver)
print("Google Translation: " + translated_lang_google)
