import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-description", methods=["POST"])
def generate_description():
    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"description": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # <--- notice the comma 500 is here, line ends

if __name__ == "__main__":
    # This must be **not indented inside the function**
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
