import streamlit as st
from PIL import Image
from main import predict
import requests
from io import BytesIO
st.set_page_config(page_title="Smart Image Analyzer", layout="centered")

st.title("🔥 Smart Image Analyzer")
st.write("Upload an image and get AI predictions")
def clear_url():
    st.session_state.url = ""
col1, col2 = st.columns([4, 1])
with col1:
    image_url = st.text_input("Paste image URL", key="url")
with col2:
    st.button("Clear", on_click=clear_url)
if image_url:
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    except:
        st.error("Invalid image URL")
    st.image(image, caption="Image from URL", width="content")
    with st.spinner("Analyzing image..."):
        results = predict(image)
    st.write("## 🧠 Predictions")
    for label, prob in results:
        st.write(f"**{label}** — {round(prob*100, 2)}%")
        st.progress(prob)
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width="content")
    with st.spinner("Analyzing image..."):
        results = predict(image)
    st.write("## 🧠 Predictions")
    for label, prob in results:
        st.write(f"**{label}** — {round(prob*100, 2)}%")
        st.progress(prob)
    best_label, best_prob = results[0]
    st.success(f"Top Prediction: {best_label} ({round(best_prob*100,2)}%)")
st.divider()
st.caption("Built using PyTorch + Streamlit")