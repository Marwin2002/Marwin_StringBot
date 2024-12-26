from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🦋 𝑺𝒕𝒂𝒓𝒕 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 🦋", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🍨 𝑹𝒆𝒕𝒖𝒓𝒏 𝑯𝒐𝒎𝒆 🍨", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🧊 𝑩𝒐𝒕 𝑺𝒕𝒂𝒕𝒖𝒔 𝒂𝒏𝒅 𝑴𝒐𝒓𝒆 𝑩𝒐𝒕𝒔 🧊", url="https://t.me/ELUpdates/8")],
        [
            InlineKeyboardButton("👻 𝑯𝒐𝒘 𝒕𝒐 𝑼𝒔𝒆 👻", callback_data="help"),
            InlineKeyboardButton("🌲 𝑨𝒃𝒐𝒖𝒕 🌲", callback_data="about")
        ]
        
    ]

    START = """
**Hey {}

Welcome to {}

If you don't trust this bot, 
> Please stop reading this message
> Delete this chat

Still reading?
You can use me to generate Pyrogram and Telethon string session. Use below buttons to learn more !

By @The_Architect04**
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @ELUpdates

Source Code : [Click Here](https://github.com/EL-Coders/SessionStringBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @CoderELAlpha
    """
