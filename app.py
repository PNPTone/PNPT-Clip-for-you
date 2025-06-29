import streamlit as st
import openai
import os
import requests
import subprocess

# Введите ваш API-ключ OpenAI
openai.api_key = "вставь_сюда_свой_API_ключ"

st.title("🖼️ PNPT Clip – Визуал по описанию (без звука)")

prompt = st.text_area("🎬 Опиши идею клипа:")

if st.button("Создать визуал") and prompt:
    with st.spinner("🎨 Генерируем изображения..."):
        response = openai.Image.create(prompt=prompt, n=5, size="512x512")
        urls = [img["url"] for img in response['data']]

        os.makedirs("frames", exist_ok=True)
        for i, url in enumerate(urls):
            img_data = requests.get(url).content
            with open(f"frames/frame{i}.png", "wb") as f:
                f.write(img_data)

        subprocess.call(
            "ffmpeg -y -r 1 -i frames/frame%01d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p output.mp4",
            shell=True
        )

        st.success("✅ Визуал готов!")
        st.video("output.mp4")