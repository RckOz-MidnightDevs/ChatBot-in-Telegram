import telebot
from telebot import types
import random

TOKEN = "Mi Token Asignado al crear el bot"
bot = telebot.TeleBot(TOKEN)

# Diccionario de emociones con varias playlists y mensajes
EMOCIONES = {
    "alegre": {
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
            "https://open.spotify.com/playlist/37i9dQZF1DX1g0iEXLFycr"
        ],
        "mensaje": "¡Genial que estés alegre! Mantén la energía positiva con ritmos alegres.",
        "consejo": "Puedes bailar un poco o tararear tus canciones favoritas 😃",
        "imagen": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExemxubzVuaHQ4MWlmczN3NmU4bDl2ZG5pYjBua2FnYjNremEyb2dyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ac0fCix8D3oN7DwCEB/giphy.gif"
    },
    "triste": {
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
            "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"
        ],
        "mensaje": "Veo que te sientes triste… La música puede ayudarte a levantar el ánimo.",
        "consejo": "Intenta escuchar la playlist mientras respiras profundo, 3 veces.",
        "imagen": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGJtOWJqa2xrdGR6d2U1MTdiYXk5b2N4YnptMW9qbWRwaXdrMTZzNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S6dJse528X4MpfAWGE/giphy.gif"
    },
    "estresado": {
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj",
            "https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7"
        ],
        "mensaje": "Parece que estás estresado 😰. Respira y relájate.",
        "consejo": "Cierra los ojos unos minutos y escucha música instrumental para liberar tensión.",
        "imagen": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm5kN2xkMHRxNHE3dnFtdHZub3VmdTgyYnB5Y3c0c21kNDVid3d5MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1E5tMWZNIrViEmr667/giphy.gif"
    },
    "relajado": {
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ",
            "https://open.spotify.com/playlist/37i9dQZF1DWXbttAJcbphz"
        ],
        "mensaje": "Perfecto 😌, estás relajado. Mantén este momento de calma.",
        "consejo": "Disfruta la música suave y concéntrate en tu respiración.",
        "imagen": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnl4N2Rwcjk0ZG95aW1zN25vNDZsbzNhOWs0anZvOGhpcGRxMzZrbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ewzF6uunnPn6L5amuW/giphy.gif"
    }
}

# Actividades
ACTIVIDAD = {
    "trabajo": "Actividad trabajo",
    "estudio": "Actividad estudio",
    "relajación": "Actividad relajación"
}

# Tipos de música
MUSICA = {
    "clásica": "https://open.spotify.com/playlist/37i9dQZF1DX8NTLI2TtZa6",
    "pop": "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",
    "rock": "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U",
    "electrónica": "https://open.spotify.com/playlist/37i9dQZF1DX4dyzvuaRJ0n",
    "relajante": "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ"
}

# Paso 1: Selección de emoción
@bot.message_handler(commands=['start'])
def start_msg(message):
    user_name = message.from_user.first_name
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("😃 Alegre", callback_data="alegre"),
        types.InlineKeyboardButton("😢 Triste", callback_data="triste"),
        types.InlineKeyboardButton("😰 Estresado", callback_data="estresado"),
        types.InlineKeyboardButton("😌 Relajado", callback_data="relajado")
    ]
    markup.add(*btns)
    bot.send_message(message.chat.id,
                     f"🎵 ¡Hola {user_name}! Soy Rck tu asistente de Musicoterapia.\n"
                     "Selecciona cómo te sientes:",
                     reply_markup=markup)

# Manejo de botones
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_name = call.from_user.first_name
    if call.data in EMOCIONES:
        data = EMOCIONES[call.data]
        playlist_random = random.choice(data["playlists"])
        bot.send_animation(call.message.chat.id, data["imagen"],
                       caption=f"{data['mensaje']} {user_name}\n💡 Consejo: {data['consejo']}\n🎵 Playlist: {playlist_random}")
        # Paso 2: seleccionar actividad
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [
            types.InlineKeyboardButton("💻 Trabajo", callback_data="trabajo"),
            types.InlineKeyboardButton("📚 Estudio", callback_data="estudio"),
            types.InlineKeyboardButton("🛀 Relajación", callback_data="relajación")
        ]
        markup.add(*btns)
        bot.send_message(call.message.chat.id,
                         "Selecciona tu actividad actual:",
                         reply_markup=markup)

    elif call.data in ACTIVIDAD:
        # Paso 3: seleccionar tipo de música
        markup = types.InlineKeyboardMarkup(row_width=2)
        btns = [types.InlineKeyboardButton(k.title(), callback_data=k) for k in MUSICA]
        markup.add(*btns)
        bot.send_message(call.message.chat.id,
                         "¡Perfecto! Ahora selecciona el tipo de música que te gusta:",
                         reply_markup=markup)

    elif call.data in MUSICA:
        playlist = MUSICA[call.data]
        bot.send_message(call.message.chat.id,
                         f"🎶 Aquí tienes una playlist de {call.data}: {playlist}")
    else:
        bot.send_message(call.message.chat.id, "Ups… algo salió mal 😅")

# Manejo de texto escrito
@bot.message_handler(func=lambda m: True)
def text_message(message):
    user_name = message.from_user.first_name
    text = message.text.lower()
    if text in EMOCIONES:
        data = EMOCIONES[text]
        playlist_random = random.choice(data["playlists"])
        bot.send_animation(message.chat.id, data["imagen"],
                       caption=f"{data['mensaje']} {user_name}\n💡 Consejo: {data['consejo']}\n🎵 Playlist: {playlist_random}")
    elif text in ACTIVIDAD:
        bot.send_message(message.chat.id,
                         f"{user_name}, seleccionaste la actividad: {text}")
    elif text in MUSICA:
        bot.send_message(message.chat.id,
                         f"🎶 Aquí tienes una playlist de {text}: {MUSICA[text]}")
    else:
        bot.send_message(message.chat.id,
                         "No entendí. Usa /start para elegir con botones.")

# Mecanismo de reconexión automática
print("Bot avanzado con playlists aleatorias, nombre de usuario e imágenes iniciado…")
while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Error de polling: {e}")
        import time
        time.sleep(5)