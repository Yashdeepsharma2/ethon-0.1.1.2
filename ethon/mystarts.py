from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("🤖 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/videoderXT"),
                               Button.url("🔍 sᴜᴘᴘᴏʀᴛ", url="https://t.me/videoderXT")],
                              [Button.url("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/videoderXT")],
                              [Button.url("💝 Bot List", url="https://t.me/vidder_botz")]]) 
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/videoderXT")]])
    
