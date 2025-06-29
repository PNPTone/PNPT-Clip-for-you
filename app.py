import streamlit as st
import requests
import base64
import os
import subprocess

st.title("🖼️ PNPT Free Clip – Визуал по описанию (через Hugging Face)")

prompt = st.text_area("🎬 Опиши идею клипа:")
HF_TOKEN = st.secrets["HF_TOKEN"] if "HF_TOKEN" in st.secrets else "вставь_сюда_токен"

def generate_image(prompt):
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        with open("generated.png", "wb") as f:
            f.write(response.content)
        return "generated.png"
    else:
        st.error("Ошибка генерации: " + response.text)
        return None

if st.button("Создать визуал") and prompt:
    with st.spinner("🎨 Генерируем изображение..."):
        img_path = generate_image(prompt)
        if img_path:
            st.image(img_path, caption="Сгенерировано AI")

            # создаем видео из одного изображения
            subprocess.call(
                "ffmpeg -y -loop 1 -i generated.png -c:v libx264 -t 5 -pix_fmt yuv420p output.mp4",
                shell=True
            )

            st.success("✅ Видео готово!")
            st.video("output.mp4")