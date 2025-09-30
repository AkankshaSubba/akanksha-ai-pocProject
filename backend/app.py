from flask import Flask, render_template,request
import os
from openai import AzureOpenAI

app = Flask(__name__)

endpoint = "https://venka-mdof0Fqm-northcentralus.cognitiveservices.azure.com/"
##model_name = "gpt-4.1"
deployment = "gpt-4o-mini"
subscription_key = "3CXKHVaK01iK8EF0PJplfddIoVAn0fJUF28lRq4FulGH0LSQCbTjJQQJ99BGACHrzpqXJ3w3AAAAACOGj6WK"
api_version = "2025-01-01-preview"


client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

@app.route('/', methods=['GET','POST'])
def index():
    chatresponse = ''
    text1=''
    if request.method == 'POST':
        prompt= request.form.get("text1")
        text = generate(prompt)
        print(text.choices[0].message.content)
        chatresponse = text.choices[0].message.content
    return render_template('index.html',chatresponse=chatresponse,text1=text1)


def generate(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_completion_tokens=20,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
