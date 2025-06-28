import streamlit as st
import openai
import os
import requests
import subprocess

# Введите ваш API-ключ OpenAI
openai.api_key = "вставь_сюда_свой_API_ключ"

st.title("🎬 PNPT Clip For You – AI-клипмейкер")

prompt = st.text_area("📝 Введи описание клипа:")
music_file = st.file_uploader("🎵 Загрузи трек (MP3)", type=["mp3"])

if st.button("Создать видео") and prompt and music_file:
    with st.spinner("🎨 Генерируем изображения..."):
        response = openai.Image.create(prompt=prompt, n=5, size="512x512")
        urls = [img["url"] for img in response['data']]

        os.makedirs("frames", exist_ok=True)
        for i, url in enumerate(urls):
            img_data = requests.get(url).content
            with open(f"frames/frame{i}.png", "wb") as f:
                f.write(img_data)

        with open("temp_music.mp3", "wb") as f:
            f.write(music_file.read())

        subprocess.call(
            "ffmpeg -y -r 1 -i frames/frame%01d.png -i temp_music.mp3 "
            "-c:v libx264 -vf fps=25 -pix_fmt yuv420p -shortest output.mp4",
            shell=True
        )

        st.success("✅ Готово! Вот твой клип:")
        st.video("output.mp4")