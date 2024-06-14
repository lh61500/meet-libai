import ollama

stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': '请用中文介绍一下你自己?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)