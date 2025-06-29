import streamlit as st
import requests
import json
import subprocess
import os

st.title("🖼️ PNPT Free Clip – Визуал по описанию (через Hugging Face, исправлено)")

prompt = st.text_area("🎬 Опиши идею клипа:")
HF_TOKEN = "вставь_сюда_токен"

def generate_image(prompt):
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": prompt}
    try:
        response = requests.post(
            api_url,
            headers=headers,
            data=json.dumps(payload).encode("utf-8")
        )
        if response.status_code == 200:
            with open("generated.png", "wb") as f:
                f.write(response.content)
            return "generated.png"
        else:
            st.error("Ошибка Hugging Face API: " + response.text)
            return None
    except Exception as e:
        st.error(f"Ошибка запроса: {e}")
        return None

if st.button("Создать визуал") and prompt:
    with st.spinner("🎨 Генерируем изображение..."):
        img_path = generate_image(prompt)
        if img_path:
            st.image(img_path, caption="Сгенерировано AI")

            subprocess.call(
                "ffmpeg -y -loop 1 -i generated.png -c:v libx264 -t 5 -pix_fmt yuv420p output.mp4",
                shell=True
            )

            st.success("✅ Видео готово!")
            st.video("output.mp4")