# PNPT Free Clip – генерация видео из изображения

Генерация AI-изображения по описанию через Hugging Face API (Stable Diffusion) и создание видео.

## Установка

1. Установи зависимости:
```
pip install -r requirements.txt
```

2. Получи токен Hugging Face: https://huggingface.co/settings/tokens
3. Вставь токен в Streamlit Secrets или прямо в код как строку:
```
HF_TOKEN = "твой_токен_сюда"
```

4. Запусти:
```
streamlit run app.py
```