import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang='en')

st.title("OCR Text Extractor with PaddleOCR")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    result = ocr.predict(img_array)

    full_text = ""
    if result and "rec_texts" in result[0]:
        full_text = " ".join(result[0]["rec_texts"])
        st.subheader("✅ Extracted Text:")
        st.write(full_text)
    elif result:
        st.warning("OCR results found, but unexpected structure.")
    else:
        st.error("No text detected in the image.")