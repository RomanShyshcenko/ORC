## 1. ORC(optical character recognition)
### Orc app that translate images with English text to just normal text. It's realized with Fastapi + pytesseract all what you need is just to upload the image with text to '/orc' endpoint, and it will return to you a text!

***
# 2. Set-up and run
### Install tesseract on your machine

```
# Linux
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev 

# Mac
brew install tesseract

#Windows
https://github.com/UB-Mannheim/tesseract/wiki#tesseract-installer-for-windows
```

### Set-up project

```
# Create virtual environment.
python3 -m venv env

# Activate it.
source env/bin/activate

# Install dependencies.
pip insatll -r requirements.txt

# Finali run the server and enjoy!
uvicorn main:app --reload
```
### You can find some image for test like this in test_data folder.

[![test-data.jpg](https://i.postimg.cc/YS1MMnj5/test-data.jpg)](https://postimg.cc/7CYpNN39)
***
# 3. Note
### If you want to use this app with other languishes read this [tutorial](https://pyimagesearchcom/2020/08/03/tesseract-ocr-for-non-english-languages/). I recommend reading tesseract installation tutorial for more understanding if you will modify project https://tesseract-ocr.github.io/tessdoc/Installation.html  