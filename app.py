from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

def chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text
    return message

@app.route("/bot")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot_response(userText))
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)
