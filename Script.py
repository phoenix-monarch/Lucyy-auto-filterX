class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴɪᴍᴇ ᴡᴇʙsᴇʀɪᴇs , ɪᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴɪᴏʏ</b>"""

    HELP_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
ᴄʟɪᴄᴋ /more ᴛᴏ ꜱᴇᴇ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.</b>"""

    ABOUT_TXT = """<b>× ᴍʏ ɴᴀᴍᴇ :  {}
× ᴍʏ ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/xenxd'>ᴍɪᴋєʏ ꜱᴀɴσ</a>
× ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
× ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a>
× ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴀɴɢᴏ ᴅʙ</a>
× ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://app.koyeb.com/'>ᴋᴏʏᴇʙ</a>

× ʀᴇqᴜᴇꜱᴛ ɢʀᴏᴜᴘ - <a href='https://t.me/+jCyXfaJkBXBmMDg1'>ᴍᴏᴠɪᴇ ꜱᴇᴀʀᴄʜ ʜᴜʙ</a></b>

× ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href='https://t.me/team_netflix'>ᴛᴇᴀᴍ ɴᴇᴛғʟɪx | ᴏʀɪɢɪɴᴀʟꜱ</a></b>"""

    SOURCE_TXT = """<b>ɴᴏᴛᴇ:
× ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀɴ  ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ ⚠️.
× ꜱᴏᴜʀᴄᴇ - <a href="https://t.me/weebs_support">ʜᴇʀᴇ</a>

× ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴏᴜʀ ᴀʟʟ ᴄʜᴀɴɴᴇʟꜱ - @Team_Netflix
× Dᴇᴠᴇʟᴏᴘᴇʀ - <a href="https://t.me/xenxd">ᴍɪᴋєʏ ꜱᴀɴσ</a></b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>

1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/team_netflix)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ.
4.ᴜꜱᴇ /set_template ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴩʟᴀᴛᴇ ꜰᴏʀ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ -</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ
ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code>
• /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.</code>

<b>•ᴀᴜᴛᴏ ᴊᴏɪɴ ᴀᴄᴄᴇᴩᴛ • 
ɪ ᴄᴀɴ ᴀᴄᴄᴇᴩᴛ ɴᴇᴡ ᴜꜱᴇʀꜱ ɪɴ yᴏᴜʀ ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ.
ᴡᴀyꜱ ᴛᴏ ᴅᴏ:-
»ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛꜱ. ᴛʜᴀᴛ'ꜱ ᴀʟʟ!!!</b>"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋꜱ ꜰᴏʀ ᴍʏ ᴀᴅᴍɪɴꜱ
 ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """<b>× ᴛᴏᴛᴀʟ ғɪʟᴇs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
× ᴛᴏᴛᴀʟ ᴄʜᴀᴛs - <code>{}</code>
× ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{}</code>
× ғʀᴇᴇ sᴛᴏʀᴀɢᴇ - <code>{}</code></b>"""

    LOG_TEXT_G = """#New_Group
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#New_User
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ

ʀᴇᴀᴅ ɪɴsᴛʀᴜᴄᴛɪᴏɴs ꜰᴏʀ ʙᴇᴛᴛᴇʀ ʀᴇsᴜʟᴛs ☟

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)

powered by - @ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ</b>"""

    GROUP_TXT = """
<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟

🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ.</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ᴍɪᴋєʏ ꜱᴀɴσ
• ᴜꜱᴇʀɴᴀᴍᴇ : @xenxd , @pervert_sanpai
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/xenxd'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
©ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Uncharted

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
©ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
©ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> <code>{file_name}</code>

<b>
╭─────── • ◆ • ───────╮
🔅 ᴘᴏᴡᴇʀᴇᴅ ʙʏ :  <a href="https://t.me/wizard_nation">ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ</a>
╰─────── • ◆ • ───────╯

╭─────── • ◆ • ───────╮
▫️ ᴄʜᴀɴɴᴇʟ : @team_netflix
▫️ main channel : @netflix_complex
╰─────── • ◆ • ───────╯</b>"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

× ᴛɪᴛᴛʟᴇ: <a href={url}>{title}</a>
× ɢᴇɴʀᴇ: {genres}
× ʀᴇʟᴇᴀsᴇ: <a href={url}/releaseinfo>{year}</a>
× ʀᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a> / 10
× ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ: {message.from_user.mention}

× ɴᴏᴛᴇ: ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ

©ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ</b>"""
    REPRT_MSG = """ Reported To Admin"""
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""
    
    FILE_READY_TXT = """
<b>ʜᴇʏ 👋 {}📫 ʏᴏᴜʀ ғɪʟᴇ ɪꜱ ʀᴇᴀᴅʏ 👇</b>

<b>📂 ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{}</code>
<b>⚙️ ғɪʟᴇ ꜱɪᴢᴇ</b> : <b>{}</b>

<b>✍️ ɴᴏᴛᴇ ❗️ This File & Message Will Deleted within 3 Mins..!</b>
"""

    TTS_TXT = """Help: <b> TTS 🎤 module:</b>
Translate text to speech
<b>Commands and Usage:</b>
• /tts <text> : convert text to speech"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ

ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:
➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
✒️ /telegraph - Send me Picture or Vide Under (5MB)
<b>NOTE:</b>
• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""
    
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 🚶🏼‍♂️
<b>Commands:</b>
• /alive - To check you are alive.
• /help - To get help.
• /ping - <b>To get your ping.</b>
<b>🛠️Usage🛠️ :</b>
• This commands can be used in pm and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
 
    STICKER_TXT = """<b>ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀ ɪᴅ..</b>

• ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:
 
◉ Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """🔰  Stylish Font Module  🔰
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ꜰᴏɴᴛ ꜱᴛʏʟᴇ 

COMMAND : /font your text (optional)
         Eg:- /font Hello
 <i>This feature added by @wizards_network"""
    
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""
    
    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ꜱʜᴏʀᴛ ᴀ ᴜʀʟ </i></b>

➤ ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    CARB_TXT = """<b>Help</b> 🔰  Carbon Module  🔰
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""
    
    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂
<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""
    
    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝙿𝙸𝙽 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴../</b>
<b>𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙿𝙻𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴::</b>
<b>📌𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴📌</b>
◉ /pin :- 𝚃𝙾 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂
◉ /unpin :- 𝚃𝙾 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝙰𝙰𝙶𝙴"""
    
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
𝟣. /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
𝟤. /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
3. /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
4. /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
5. /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""
    
    FILE_CHANNEL_TXT = """
<b>Hai 👋 {}</b> 😍
    
<code>{}</code>
    
╭─────── • ◆ • ───────╮
🔅 ᴘᴏᴡᴇʀᴇᴅ ʙʏ :  <a href="https://t.me/wizard_nation">ᴡɪᴢᴀʀᴅ ɴᴇᴛᴡᴏʀᴋ</a>
╰─────── • ◆ • ───────╯
▫️ ᴄʜᴀɴɴᴇʟ : @team_netflix
▫️ main channel : @netflix_complex
╰─────── • ◆ • ───────╯
"""
    
    LOGO = """

██████╗░░██████╗░░░░░░░████████╗██╗░░██╗███████╗░░░░░░███████╗██╗██╗░░░░░███████╗░░░░░░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░
██╔══██╗██╔═══██╗░░░░░░╚══██╔══╝██║░░██║██╔════╝░░░░░░██╔════╝██║██║░░░░░██╔════╝░░░░░░██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗
██║░░██║██║██╗██║█████╗░░░██║░░░███████║█████╗░░█████╗█████╗░░██║██║░░░░░█████╗░░█████╗██║░░██║██║░░██║██╔██╗██║██║░░██║██████╔╝
██║░░██║╚██████╔╝╚════╝░░░██║░░░██╔══██║██╔══╝░░╚════╝██╔══╝░░██║██║░░░░░██╔══╝░░╚════╝██║░░██║██║░░██║██║╚████║██║░░██║██╔══██╗
██████╔╝░╚═██╔═╝░░░░░░░░░░██║░░░██║░░██║███████╗░░░░░░██║░░░░░██║███████╗███████╗░░░░░░██████╔╝╚█████╔╝██║░╚███║╚█████╔╝██║░░██║
╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░░░░░░╚═╝░░░░░╚═╝╚══════╝╚══════╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝"""
