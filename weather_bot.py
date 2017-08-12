import misc
from bothandler import BotHandler
import datetime
from time import sleep

bot = BotHandler(misc.token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():
	new_offset = None
	today = now.day
	hour = now.hour

	while True:
		bot.get_updates(new_offset)

		last_update = bot.get_last_update()

		last_update_id = last_update['update_id']
		last_chat_id = last_update['message']['chat']['id']
		last_chat_text = last_update['message']['text']
		last_chat_name = last_update['message']['chat']['first_name']
		print(last_update_id)

		if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
			bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
			today += 1

		elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
			bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
			today += 1

		elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
			bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
			today += 1

		new_offset = last_update_id + 1
		sleep(2)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
