import gpt4free
from gpt4free import Provider, quora, forefront

# usage You
response = gpt4free.Completion.create(Provider.You, prompt='请写一首李白的诗')
print('usage You')
print(response)

# usage Poe 报错
# token = quora.Account.create(logging=False)
# response = gpt4free.Completion.create(Provider.Poe, prompt='请写一首李白的诗', token=token, model='ChatGPT')
# print(response)

# usage forefront 报错
# token = forefront.Account.create(logging=False)
# response = gpt4free.Completion.create(
#     Provider.ForeFront, prompt='请写一首李白的诗', model='gpt-4', token=token
# )
# print(response)
# print(f'END')

# usage theb
response = gpt4free.Completion.create(Provider.Theb, prompt='请写一首李白的诗')
print('usage theb')
print(response)

# usage cocalc  报错
response = gpt4free.Completion.create(Provider.CoCalc, prompt='请写一首李白的诗', cookie_input='')
print('usage cocalc')
print(response)
