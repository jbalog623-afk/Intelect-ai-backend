# Intelect-ai-backend
Intelect is an AI-powered assistant that turns ideas into actionable insights. From generating content to analyzing data, Intelect helps you work smarter, faster, and more efficiently
# Intelect Food AI Backend

Flask backend for generating menu descriptions and social media posts using OpenAI GPT-4.

## Deployment

- Connect to Render Web Service
- Add `OPENAI_API_KEY` environment variable
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app --bind 0.0.0.0:$PORT`
