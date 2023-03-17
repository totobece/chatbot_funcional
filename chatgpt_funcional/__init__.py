from flask import Flask, render_template, request
import os
import openai
openai.api_key = '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'

conversation=[{"role": "system", "content": "actua como ronaldo nazario, el famoso jugador de futbol brasilero, cualquier pregunta que te haga sobre vos me la tenes que responder, ya sea sobre tu niñez o sobre tu carrera profesional como futbolista."}]

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def completion_response():
    user_input = request.args.get('msg')   
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return str(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    app.run()