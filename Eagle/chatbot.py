from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(usrText):
    print('step2'+usrText)
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter'
   )
    trainer = ListTrainer(bot)
    print('step3'+usrText)
    while True:
        print('step4'+usrText)
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break
        

        
