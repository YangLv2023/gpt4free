# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Project : gpt4free
# @Author : pei
# @Time : 2023-05-09 17:13
# @Describe : 
"""
from gpt4free import you
from flask import Flask, jsonify, request, redirect, render_template
import gpt4free
from gpt4free import Provider, quora, forefront
from gpt4free import usesless

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True
chat = {}
chat_gpt = []
num = 1
message_id = ""


@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
    global num, chat, message_id
    if request.method == 'GET':
        return render_template('index.html', response=None)
    if request.method == 'POST':
        prompt = request.form.get('content')
        response = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)
        message_id = response["id"]
        # response = gpt4free.Completion.create(Provider.Theb, prompt=prompt)
        # print('usage theb')
        # print(response)

        chat_gpt.append({"question": prompt, "answer": response['text']})
        chat[num] = {"ME": prompt, "GPT": response['text']}
        num += 1
        print(response['text'])
        return render_template('index.html', chat=chat)


if __name__ == '__main__':
    app.run()