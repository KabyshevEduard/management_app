from celery import Celery
import requests


TOKEN = '7792093776:AAHFQ1VqGrCty6SO67USekTTsZrkcP9U53Q'
url = f'https://api.telegram.org/bot{TOKEN}/'
database_url_redis = 'redis://172.18.0.4'

app = Celery(__name__, broker=database_url_redis, backend=database_url_redis)
app.conf.update(timezone='Europe/Moscow')


@app.task(name='save_file')
def save_file(binary_content, path):
    with open(path, 'xb') as file_on_disk:
        file_on_disk.write(binary_content)
    return True

@app.task(name='notify')
def send_notification(who, chat_title):
    chat_id = None
    response = requests.get(url + 'getUpdates')
    response = response.json()
    for t in response['result']:
        obj = t.get('my_chat_member')
        if obj != None:
            chat = obj['chat']
            if chat['title'] == chat_title:
                chat_id = chat['id']

    requests.post(url + 'sendMessage', json={'chat_id': chat_id, 'text': f'{who} добавил документ'})
    return True


if __name__ == '__main__':
    app.start()
