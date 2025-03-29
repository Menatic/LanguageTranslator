from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this import
from pydantic import BaseModel
from langdetect import detect
from googletrans import Translator

app = FastAPI(title="Language Translator API")

# Add these CORS middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str = "en"

@app.post("/translate")
async def translate(request: TranslationRequest):
    try:
        source_lang = detect(request.text)
        translator = Translator()
        translation = translator.translate(
            request.text, 
            dest=request.target_language
        )
        return {
            "original_text": request.text,
            "translated_text": translation.text,
            "source_language": source_lang,
            "target_language": request.target_language
        }
    except Exception as e:
        return {"error": str(e)}