from flask import Flask, render_template, request, jsonify

from groq import Groq

client = Groq(
    api_key="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"
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": text,
        }
    ],
    model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    app.run()
