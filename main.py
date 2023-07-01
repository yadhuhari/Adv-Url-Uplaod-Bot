from viberbot import Api
from flask import Flask, request, Response
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage


app = Flask(__name__)
viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://site.com/avatar.jpg',
    token='445da6az1s345z78-dazcczb2542zv51a-e0vc5fva17480im9'
))

@app.route('/incoming', methods=['POST'])
def incoming():
	logger.debug("received request. post data: {0}".format(request.get_data()))
	# handle the request here
	return Response(status=200)

@app.route('/incoming', methods=['POST'])
def incoming():
  viber.send_messages(to=viber_request.get_sender().get_id(),
        messages=[TextMessage(text="sample message")])

context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=443, debug=True, ssl_context=context)
