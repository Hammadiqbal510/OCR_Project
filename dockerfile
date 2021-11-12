FROM python
WORKDIR /OCR_MODELS
COPY . .

RUN pip install pillow
RUN pip install easyocr
# RUN pip install -r requirements.txt
WORKDIR /easyocr
CMD ["python3","easy_ocr.py"]