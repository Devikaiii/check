class script(object):
    START_TXT = """Hello {},
It's Power Full Here ð
Add Me To Your Group And Make Sure Iam Admin There!
And Enjoy My Pever Show.....!!!ðĪŠ
Powered by @raixpiro_bot """
    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðð·ðī ð·ðīðŧðŋ ðĩðūð ðžð ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """âŊ ðžð ð―ð°ðžðī: {}
â ððŦððð­ðĻðŦ : <a href=https://t.me/rithesh_rkrm_17>ãáīÉŠĘáīã</a>
â ððð§ð ðŪðð ð : [ððēð­ðĄðĻð§ ð.ð.ðð]
â ððĒððŦððŦðē : [ððēðŦðĻð ðŦððĶ ððŽðēð§ððĒðĻ ð.ð.ðð]
â ððĄðð§ð§ððĨ : [ãáīÉŠĘáīãððĻð­ðŽ]
â ððð­ððððŽð:[ððððððŧðđ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://t.me/rai_info17  

<b>DEVS:</b>
- <a href=https://t.me/rithesh_rkrm_17>ãáīÉŠĘáīã</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/rai_info17)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specified user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban  - <code>to ban a user.</code>
âĒ /unban  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code>
â ððūðð°ðŧ ðððīðð: <code>{}</code>
â ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code>
â ðððīðģ ðððūðð°ðķðī: <code>{}</code> ðžððą
â ðĩððīðī ðððūðð°ðķðī: <code>{}</code> ðžððą"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
