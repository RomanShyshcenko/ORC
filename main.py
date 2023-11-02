from fastapi import FastAPI, File, UploadFile
import shutil
import pytesseract

app = FastAPI()


@app.post("/ocr")
async def root(image: UploadFile = File()):
    filepath = 'txtFile'
    with open(filepath, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(filepath, lang='eng')



