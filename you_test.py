# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Project : gpt4free
# @Author : pei
# @Time : 2023-05-09 17:13
# @Describe : 
"""
from gpt4free import usesless
from gpt4free import you
from flask import Flask, jsonify, request, redirect, render_template
import gpt4free
from gpt4free import Provider, quora, forefront

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True
chat = []
message_id = ""



@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
    if request.method == 'GET':
        return render_template('index.html', res='None')
    if request.method == 'POST':
        prompt = request.form.get('content')
        print(prompt)
        # response = you.Completion.create(prompt=prompt, chat=chat)
        # req = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)
        #req = gpt4free.Completion.create(provider=gpt4free.Provider.UseLess, prompt=prompt, parentMessageId=message_id)


        # usage You
        # req = gpt4free.Completion.create(Provider.You, prompt=prompt)

        # usage Poe  无法返回
        # token = quora.Account.create(logging=False)
        # req = gpt4free.Completion.create(Provider.Poe, prompt=prompt, token=token, model='ChatGPT')


        # usage forefront  无法访问
        # create an account
        account_data = forefront.Account.create(logging=False)

        # get a response
        for response in forefront.StreamingCompletion.create(
                account_data=account_data,
                prompt=prompt,
                model='gpt-4'
        ):
            print(response.choices[0].text, end='')
        req = response.choices[0].text

        # usage theb
        # req = gpt4free.Completion.create(Provider.Theb, prompt=prompt)

        # usage cocalc
        #req = gpt4free.Completion.create(Provider.CoCalc, prompt=prompt, cookie_input='')


        # chat.append({"question": prompt, "answer": req['text']})
        print(req)
        return render_template('index.html', res=req)


if __name__ == '__main__':
    app.run()