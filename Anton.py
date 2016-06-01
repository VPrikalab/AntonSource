import telebot
token ='225829342:AAFoaGLUlvz2DBRC-yO7-bS9nw8UC9vMDCs'
Father_id=115491916
Anton= telebot.TeleBot(token)
@Anton.message_handler(content_types=["text"])
def response_message(message):
	print message.chat.id
	Anton.send_message(message.chat.id,"Hello, i am Anton")
if __name__ =='__main__':
	Anton.polling(none_stop=True)
