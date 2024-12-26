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
        [
            InlineKeyboardButton("👻 𝑯𝒐𝒘 𝒕𝒐 𝑼𝒔𝒆 👻", callback_data="help"),
            InlineKeyboardButton("🌲 𝑨𝒃𝒐𝒖𝒕 🌲", callback_data="about")
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
