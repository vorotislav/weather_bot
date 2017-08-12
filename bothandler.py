import requests


class BotHandler:

	def __init__(self, token):
		self.token = token
		self.api_url = "http://api.telegram.org/bot{}/".format(token)

	def get_updates(self, offset = None, timeout = 30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		resp = requests.get(self.api_url + method, params)
		result_json = resp.json()['result']
		return result_json

	def get_last_update(self):
		get_result = self.get_updates()

		if len(get_result) > 0:
			last_update = get_result[-1]
		else:
			last_update = get_result[len(get_result)]
		return last_update

	def send_message(self, chat_id, text):
		print('send mes: ' + text)
		params = {'chat_id': chat_id, 'text': text}
		method = 'sendMessage'
		resp = requests.get(self.api_url + method, params)
		return resp
