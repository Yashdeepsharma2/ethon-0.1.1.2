from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("🤖 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/videodertxt"),
                               Button.url("🔍 sᴜᴘᴘᴏʀᴛ", url="https://t.me/videodertxt")],
                              [Button.url("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/KingVJ01")],
                              [Button.url("💝 Bot List", url="https://t.me/vidder_botz")]]) 
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/Kingvj01")]])
    
