# telbot

## Simple Telegram bot only for sending message to chat room with 30 lines of code

Setup

1. pip install git+https://github.com/khursani8/telbot

Code

```python
from telbot import telbot
token = "token"
sender = telbot.Sender(token)
sender.get_chat_id() # need to start conversation with bot first
sender.send("test")
```