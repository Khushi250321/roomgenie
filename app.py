# ----------  app.py  ----------
import streamlit as st
import openai
import os

# ↓ Streamlit Cloud injects your key from secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="RoomGenie", layout="centered")
st.title("🏡 RoomGenie – AI Interior Design Assistant")

st.write(
    "1️⃣ *Upload* a photo of your room (optional)\n"
    "2️⃣ *Describe* the style you want\n"
    "3️⃣ *Generate* a brand-new look powered by DALL·E 3 💡"
)

uploaded = st.file_uploader("Upload room photo (optional)", type=["jpg", "jpeg", "png"])
prompt   = st.text_input("Describe the style you want",
                         placeholder="e.g. minimalist boho bedroom with warm lighting")

if st.button("✨ Generate AI Design"):
    if prompt.strip() == "":
        st.warning("Please enter a style description 🙂")
        st.stop()

    with st.spinner("Calling DALL·E 3 – please wait…"):
        try:
            response = openai.images.generate(
                model   = "dall-e-3",
                prompt  = prompt,
                size    = "1024x1024",
                quality = "standard",
                n       = 1,
            )
            url = response.data[0].url
        except Exception as e:
            st.error(f"❌ OpenAI error: {e}")
            st.stop()

    st.subheader("🎨 Your AI-generated design")
    st.image(url, use_column_width=True)

    st.subheader("🛒 Suggested Products")
    st.markdown(
        "- *Wall art set* – [link](https://www.amazon.in/s?k=wall+art)\n"
        "- *Accent chair* – [link](https://www.amazon.in/s?k=accent+chair)\n"
        "- *Warm floor lamp* – [link](https://www.amazon.in/s?k=floor+lamp)"
    )
