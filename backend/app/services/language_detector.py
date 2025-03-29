from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# For consistent results
DetectorFactory.seed = 0

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"