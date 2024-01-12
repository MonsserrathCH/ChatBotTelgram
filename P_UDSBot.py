"""
Chatbot dedicado a la Unidad de Posgrados de la UNAM dedicado a mejorar la comunicación entre los usuarios 
y la Unidad de Sistemas para la resolución de problemas técnicos y la prestación de asistencia.
"""

# Importación de las librerías necesarias
import telebot
from telebot import types
from config import *
import threading
import logging
import time
import asyncio

# Inicialización y asociación del bot con el TOKEN
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Función que responde a los comandos de inicio (start, ayuda, help) y envía un mensaje de bienvenida.
@bot.message_handler(commands=["start","ayuda","help"])
def cmd_start(message):
    """Da la bienvenida al usuario"""
    print(message.chat.id)
    bot.reply_to(message, "¡Hola y bienvenido! Para comenzar el chat, simplemente envía cualquier mensaje. ¡Un simple 'Hola' está bien 🤖")
    
# Ejecutar el bot mientras se reciba una respuesta de tipo texto
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    bot.send_chat_action(message.chat.id, 'typing')
    # Verificar que el mensaje sea válido y de lo contrario indicar que el comando seleccionado no está disponible
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    # Opciones de ayuda ante mensaje válido
    else:
        #bot.send_message(message.chat.id, "¡Hola! 👋 Somos la Unidad de Sistemas. Por favor, selecciona una opción para que podamos ayudarte de la mejor manera posible. 💻")
        button_grado = types.InlineKeyboardButton('Ayuda en salas de grado', callback_data='grado')
        button_auditorio = types.InlineKeyboardButton('Ayuda en auditorio', callback_data='auditorio')
        button_soporte = types.InlineKeyboardButton('Soporte a equipo de cómputo', callback_data='soporte')
        button_num_aula = types.InlineKeyboardButton('Ayuda en aula de clase', callback_data='numAula')

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_soporte)
        keyboard.add(button_grado)
        keyboard.add(button_auditorio)
        keyboard.add(button_num_aula)
        bot.send_message(message.chat.id, text='¡Hola! 👋 Somos la Unidad de Sistemas. Por favor, selecciona una opción para que podamos ayudarte de la mejor manera posible. 💻', reply_markup=keyboard)

# Da la bienvenida al usuario

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    print(type(call.data))

    #  SALAS DE GRADO
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
        bot.send_message(call.message.chat.id, text='¿En qué sala de grado podemos asistirte?', reply_markup=keyboard)
    
    # Respuesta según la opción seleccionada
    if call.data == 'D208':
        bot.send_message(call.message.chat.id, "¡Entendido! Hemos notificado al personal de sistemas, quienes estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el D208. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")        

    if call.data == 'D209':
        bot.send_message(call.message.chat.id, "¡Entendido! Hemos notificado al personal de sistemas, quienes estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el D209. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")        

    if call.data == 'D307':
        bot.send_message(call.message.chat.id, "¡Entendido! Hemos notificado al personal de sistemas, quienes estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el D307. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")        

    if call.data == 'D308':
        bot.send_message(call.message.chat.id, "¡Entendido! Hemos notificado al personal de sistemas, quienes estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el D308. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")        
    
    #  AUDITORIOS
    # Crear botones para diferentes auditorios
    if call.data == "auditorio":
        button_a1 = types.InlineKeyboardButton('Auditorio-1', callback_data='Auditorio-1')
        button_a2 = types.InlineKeyboardButton('Auditorio-2', callback_data='Auditorio-2')

        # Crear un teclado en línea con los botones
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_a1)
        keyboard.add(button_a2)
        bot.send_message(call.message.chat.id, text='¿En qué auditorio podemos asistirte?', reply_markup=keyboard)

    # Respuesta según la opción seleccionada 
    if call.data == "soporte":
        bot.send_message(call.message.chat.id, "¡Por supuesto! 😊 Por favor, para brindarte el mejor soporte, te invitamos a solicitar un ticket a través de la siguiente liga: https://zafiro.posgrado.unam.mx/soporteUDS/")

    if call.data == 'Auditorio-1':
        bot.send_message(call.message.chat.id, "¡Perfecto! Hemos informado a nuestros operadores de cabina para brindarte apoyo. Estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el Auditorio 1. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")  
    
    if call.data == 'Auditorio-2':
        bot.send_message(call.message.chat.id, "¡Perfecto! Hemos informado a nuestros operadores de cabina para brindarte apoyo. Estarán en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia!😊")
        bot.send_message("-4039475376", "¡Hola equipo! Tenemos usuarios que necesitan apoyo en el Auditorio 2. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")  

   # AULAS
    if call.data == 'numAula':
        bot.send_message(call.message.chat.id, "Entendido. Por favor, indica el número de aula y describe brevemente cuál es tu problema o solicitud para que podamos brindarte la mejor asistencia posible.")
        bot.register_next_step_handler(call.message, handle_num_aula_problem)

def handle_num_aula_problem(message):
    user_chat_id = message.chat.id
    user_message = message.text

    # Enviar el mensaje al grupo con la información del usuario
    bot.send_message("-4039475376", f"¡Hola equipo! Tenemos un usuario ({user_chat_id}) con la siguiente solicitud en un aula específica: {user_message}. ¿Quién puede brindar asistencia? ¡Gracias!🏃‍♂️")
    bot.send_message(user_chat_id, "Hemos recibido tu solicitud. El equipo de soporte la revisará y estará en el lugar en un plazo de 5 a 10 minutos. ¡Gracias por tu paciencia! 😊")

# Función para asegurar la escucha continua del bot ante nuevos mensajes
def recibirMensajes():
    bot.infinity_polling()

# Asegurar que lo esté haciendo desde un hilo separado
if __name__ == '__main__':
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibirMensajes)
    hilo_bot.start()
    print('Bot iniciado')

    # Agregar un pequeño retraso para permitir que el hilo del bot se inicie completamente
    time.sleep(2)
    
    # Esto evitará que el programa principal termine antes de que el hilo del bot se complete
    hilo_bot.join()
