from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Bot')
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)

for files in os.listdir('C:/Mahesh/Work/python/chatterbot-corpus-master/chatterbot_corpus/data/Errors/'):
		data=open('C:/Mahesh/Work/python/chatterbot-corpus-master/chatterbot_corpus/data/Errors/'+files,'r').readlines()
		#bot.train(data)
		trainer.train(data)

while True:
	message=input('You:')
	if message.strip() !='Bye' :
		reply=bot.get_response(message)
		print('ChatBot:', reply)
	if message.strip() == 'Bye':
		print('ChatBot : Bye')
		break


