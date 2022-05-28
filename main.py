from telethon.sync import TelegramClient

api_id = 13381418
api_hash = '5e996b084179f5841b224a34d6de47ca'
phone_number = '89152427309'

if __name__ == '__main__':
    client = TelegramClient('history_lurker', api_id=api_id, api_hash=api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter code: '))

    chat = -1001638634191
    english_alphabet = set('abcdefghijklmnopqrstuvwxyz')

    with TelegramClient('history_lurker', api_id, api_hash) as client:
        history_message = []
        p = 0
        for message in client.iter_messages(chat):
            english_words = [b for b in str(message.text).lower().split() if not (english_alphabet.isdisjoint(b.lower()))]
            if 'the' in english_words:
                english_words.remove('the')

            for i in history_message:
                a = set(english_words)
                b = set(i)
                if a & b:
                    p = 1
                    print(message.sender_id, ':', message.text)
                    client.delete_messages(chat, message)

            if p == 0:
                history_message.append(english_words)
        if len(history_message) >= 100:
            history_message.reverse()
            del history_message[:4]