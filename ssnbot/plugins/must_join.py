from ssnbot import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, LinkPreviewOptions
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"ʏᴏᴜ ᴍᴜꜱᴛ ᴊᴏɪɴ [ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ]({link}) ᴛᴏ ᴜꜱᴇ ᴍᴇ. ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴛʀʏ ᴀɢᴀɪɴ 🥺",
                    # disable_web_page_preview=True,
                    link_preview_options=LinkPreviewOptions(is_disabled=True),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🌲 ᴄʟɪᴄᴋ ʜᴇʀᴇ 🌲", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
