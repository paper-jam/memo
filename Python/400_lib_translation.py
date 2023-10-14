# -- ===== TextBlob - analyse de texte
#  Textblob -> obsolète
# from googletrans import Translator

# ==> Important: If you want to use a stable API, I highly recommend you to use Google’s official translate API.

# translator = Translator()
# translator.translate("안녕하세요.")
# # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

# translator.translate("안녕하세요.", dest="ja")
# # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

# translator.translate("veritas lux mea", src="la")
# # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

text = "minister"

import deepl

translator = deepl.Translator("xxxxxxxxxxxxxx")
# result = translator.translate_text(text, target_lang=target_language)
# translated_text = result.text
