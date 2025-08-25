# app.py
import streamlit as st
from PIL import Image
import numpy as np
import easyocr
import re

reader = easyocr.Reader(['en'])

st.title("OCR Application with EasyOCR")
st.write("Upload an image; it will extract text and numbers into a TXT file.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Processing...")

    image_np = np.array(image)

    result = reader.readtext(image_np)

    extracted_text = "\n".join([detection[1] for detection in result])

    st.text_area("Extracted Text", extracted_text, height=200)

    txt_filename = "extracted_text.txt"
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write("=== Full Text ===\n")
        f.write(extracted_text + "\n\n")

    st.success(f"Text saved to `{txt_filename}`!")

    with open(txt_filename, "rb") as f:
        st.download_button(
            label="Download TXT file",
            data=f,
            file_name=txt_filename,
            mime="text/plain"
        )
