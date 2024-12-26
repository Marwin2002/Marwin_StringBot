from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🦋 ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ 🦋", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🍨 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🍨", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("👻 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ 👻", callback_data="help"),
            InlineKeyboardButton("🌲 ᴀʙᴏᴜᴛ  🌲", callback_data="about")
        ]
        
    ]

    START = """
**ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ, 
> ᴘʟᴇᴀꜱᴇ ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
> ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ

ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ ! 

ʙʏ @The_Architect04**
    """

    HELP = """
👀 **Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs** 👀

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
/start - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ
/restart - ᴛᴏ ꜱᴛᴀʀᴛ ᴀ ɴᴇᴡ
"""

    ABOUT = """
🍹 **Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ** 🍹

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙʏ @The_Architect04

ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/AnonymousX1025/StringGenBot)

ꜰʀᴀᴍᴇ ᴡᴏʀᴋ : [ᴘʏʀᴏᴛɢꜰᴏʀᴋ](https://t.me/pyrotgfork/160)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ ](https://www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @Marwin_ll
    """
