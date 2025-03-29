from googletrans import Translator
from langdetect import detect

translator = Translator()

def translate_text(text: str, target_lang: str = "en") -> dict:
    try:
        source_lang = detect(text)
        result = translator.translate(text, dest=target_lang)
        return {
            "original_text": text,
            "translated_text": result.text,
            "source_language": source_lang,
            "target_language": target_lang
        }
    except Exception as e:
        return {"error": str(e)}