from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter')
    trainer = ListTrainer(chatbot)
    for file in os.listdir('C:/Mahesh/Work/python/Eagle/data/'):
        convData = open('C:/Mahesh/Work/python/Eagle/data/' + file,'r').readlines()
        trainer.train(convData)
        #chatbot.set_trainer(ListTrainer)
        #chatbot.train(convData)
        #print("Training completed")
    

setup()
