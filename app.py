import streamlit as st

st.title("🔊 Тест загрузки MP3-файла")

music_file = st.file_uploader("🎵 Загрузите MP3", type=["mp3"])

if music_file is not None:
    st.success("✅ Файл получен!")
    st.write(f"**Имя файла:** {music_file.name}")
    st.write(f"**Размер:** {round(len(music_file.read()) / 1024, 2)} KB")

    music_file.seek(0)
    st.audio(music_file, format='audio/mp3')