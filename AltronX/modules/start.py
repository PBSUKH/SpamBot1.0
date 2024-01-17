from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("☆ 𝐂ᴏᴍᴍᴀɴᴅs ☆", data="help_back")
        ],
        [
        Button.url("☆ 𝐂ʜᴀɴɴᴇʟ ☆", "https://t.me/ll_BAD_MUNDA_WORLD_ll"),
        Button.url("☆ 𝐒ᴜᴘᴘᴏʀᴛ", "https://t.me/ll_THE_BAD_BOT_ll")
        ],
        [
        Button.url("☆ 𝐁ᴀᴅ 𝐎ᴘ ☆", "https://t.me/II_BAD_MUNDA_II")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝐇ᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝐈 𝐀𝐦 [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝐃ᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ :~ [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](https://t.me/II_BAD_MUNDA_II)**\n\n"
        TEXT += f"» ** 𝐋ᴇɢᴇɴᴅ sᴘᴀᴍ x ᴠᴇʀsɪᴏɴ :** `3.2`\n"
        TEXT += f"» **𝐓ᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/911bc5ee7330f9dc72ee8.jpg",
                caption=TEXT, 
                buttons=PythonButton)
