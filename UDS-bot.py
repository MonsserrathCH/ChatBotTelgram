"""
Chatbot dedicado a la Unidad de Posgrados de la UNAM dedicado a mejorar la comunicación entre los usuarios 
y la Unidad de Sistemas para la resolución de problemas técnicos y la prestación de asistencia.
"""
import telebot
from telebot import types
from config import *
import threading
import logging

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)

# Inicialización y asociación del bot con el TOKEN
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Función que responde a los comandos de inicio (start, ayuda, help) y envía un mensaje de bienvenida.
@bot.message_handler(commands=["start","ayuda","help"])
def cmd_start(message):
    """Da la bienvenida al usuario"""
    print(message.chat.id)
    bot.reply_to(message, "Bienvenido, favor de mandar un mensaje para iniciar el chat")
    
# Ejecutar el bot mientras se reciba una respuesta de tipo texto
@bot.message_handler(content_types=["text"])

# FUNCIÓN ENCARGADA DE DAR EL FLUJO
def bot_mensajes_texto(message):
    bot.send_chat_action(message.chat.id, 'typing')
    # Verificar que el mensaje sea válido y de lo contrario indicar que el comando 
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
     # Opciones de ayuda ante mensaje válido
    else:
        #bot.send_message(message.chat.id, "Somos la Unidad de Sistemas, ¿En qué te podemos ayudar?")
        button_soporte = types.InlineKeyboardButton('Soporte a equipo de cómputo', callback_data='soporte')
        button_grado = types.InlineKeyboardButton('Ayuda en salas de grado', callback_data='grado')
        button_auditorio = types.InlineKeyboardButton('Ayuda en auditorio', callback_data='auditorio')
        button_aula = types.InlineKeyboardButton('Ayuda en Aulas de clase', callback_data='aula')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_soporte)
        keyboard.add(button_grado)
        keyboard.add(button_auditorio)
        keyboard.add(button_aula)
        bot.send_message(message.chat.id, text='Somos la Unidad de Sistemas, ¿En qué te podemos ayudar?', reply_markup=keyboard)
    """Da la bienvenida al usuario"""


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    print(type(call.data))
    # Crear botones para diferentes salas de grado
    if call.data == "grado":
        button_208 = types.InlineKeyboardButton('D-208', callback_data='D208')
        button_209 = types.InlineKeyboardButton('D-209', callback_data='D209')
        button_307 = types.InlineKeyboardButton('D-307', callback_data='D307')
        button_308 = types.InlineKeyboardButton('D-308', callback_data='D308')

        # Crear un teclado en línea con los botones
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_208)
        keyboard.add(button_209)
        keyboard.add(button_307)
        keyboard.add(button_308)
        bot.send_message(call.message.chat.id, text='¿En qué salon tienes problemas?', reply_markup=keyboard)
    
    # Respuesta según la opción seleccionada
    if call.data == "soporte":
        bot.send_message("Favor de solicitar el ticket por medio de la siguiente liga: ")

    if call.data == 'D208':
        bot.send_message(call.message.chat.id, "Ya se notificó a personal de Sistemas, llegan entre 5 a 10 minutos a sitio")
        bot.send_message("-812816203", "Favor de apoyar en el D208, usuarios necesitan apoyo en sitio")        

    if call.data == 'D209':
        bot.send_message(call.message.chat.id, "Ya se notificó a personal de Sistemas, llegan entre 5 a 10 minutos a sitio")
        bot.send_message("-812816203", "Favor de apoyar en el D209, usuarios necesitan apoyo en sitio")        

    if call.data == 'D307':
        bot.send_message(call.message.chat.id, "Ya se notificó a personal de Sistemas, llegan entre 5 a 10 minutos a sitio")
        bot.send_message("-812816203", "Favor de apoyar en el D307, usuarios necesitan apoyo en sitio")        


    if call.data == 'D308':
        bot.send_message(call.message.chat.id, "Ya se notificó a personal de Sistemas, llegan entre 5 a 10 minutos a sitio")
        bot.send_message("-812816203", "Favor de apoyar en el D308, usuarios necesitan apoyo en sitio")        


    if call.data == 'auditorio':
        bot.send_message(call.message.chat.id, "Ya se notificó a operadores de Cabina sobre el apoyo, llegan entre 5 a 10 minutos a sitio")
        bot.send_message("-812816203", "Favor de apoyar en el Auditorio, usuarios necesitan apoyo en sitio")        

    #if call.data.split('#')[0] == call.data.split('#')[1]:
    #    bot.send_message(call.message.chat.id,  '✅ Correct!')
    #else:
    #    bot.send_message(call.message.chat.id,  '❌ Wrong!\n♻️ The answer is: %s' % call.data.split('#')[1])


# Función para asegurar la escucha continua del bot ante nuevos mensajes
def recibirMensajes():
    bot.infinity_polling()

if __name__ == '__main__':
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot",target=recibirMensajes)
    hilo_bot.start()
    print('Bot iniciado')




