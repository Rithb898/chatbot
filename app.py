from flask import Flask, render_template, request, jsonify
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
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
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "You are designed to provide simple and concise answers. Your responses should be clear and to the point."
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": text,
        }
    ],
    model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    app.run()
