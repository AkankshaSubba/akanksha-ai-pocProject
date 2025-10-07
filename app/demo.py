import os
from openai import AzureOpenAI

endpoint = "https://ngaifpoc.cognitiveservices.azure.com/"
model_name = "gpt-4.1"
deployment = "gpt-4.1"

subscription_key = "Dr1tvfmZw9h5ponz3QBIRnYtmj8YhNsgDAoEhmrSn1d7PbbzmCYMJQQJ99BGACmepeSXJ3w3AAAAACOGOb0I"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Write a sentence about a rose",
        }
    ],
    max_completion_tokens=20,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment
)



def generate():
    endpoint = "https://ngaifpoc.cognitiveservices.azure.com/"
    ##model_name = "gpt-4.1"
    deployment = "gpt-4.1"

    subscription_key = "Dr1tvfmZw9h5ponz3QBIRnYtmj8YhNsgDAoEhmrSn1d7PbbzmCYMJQQJ99BGACmepeSXJ3w3AAAAACOGOb0I"
    api_version = "2024-12-01-preview"

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Write a haiku about me",
            }
        ],
        max_completion_tokens=20,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )
    print(response.choices[0].message.content)
    return response
        


print(response.choices[0].message.content)