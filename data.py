from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🦋 ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ 🦋", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🧃 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🧃", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("🍬 ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛꜱ 🍬", url="https://t.me/The_Architect04/13")],
        [
            InlineKeyboardButton("👻 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ 👻", callback_data="help"),
            InlineKeyboardButton("🌲 ᴀʙᴏᴜᴛ  🌲", callback_data="about")
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
🌴 **Available Commands** 🌴

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - To start a new
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @The_Architect04

Source Code : [Click Here](https://t.me/The_Architect04)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @Marwin_ll
    """
