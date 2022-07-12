# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@Broken_boyxd)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @Broken_boyxd
API_HASH = getenv("API_HASH", "7f10cf5e8390a3ff33c7bbc581469984")
API_ID = int(getenv("API_ID", "9620148"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝘼𝙎𝙎𝙄𝙎𝙏𝘼𝙉𝙏")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "brokenx_Assistant")
BOT_IMAGE = getenv("BOT_IMAGE", https://te.legra.ph/file/e70f61a413b17c6add2a1.jpg"")
BOT_NAME = getenv("BOT_NAME", "𝘽𝙍𝙊𝙆𝙀𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_TOKEN = getenv("BOT_TOKEN", "5552389598:AAEg1gXRcldx6dSjaKluOncqHqACgn5vnoY")
BOT_USERNAME = getenv("BOT_USERNAME", "broken_vccbot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "- ❛𝗠𝘁𝘀 ➻ 𝗕𝗿𝗼𝗸𝗲𝗻 𝗕𝗼𝘆 [🇮🇳]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Broken_boyxd")
SOURCE_CODE = getenv("SOURCE_CODE","https://t.me/Broken_boyxd")
STRING_SESSION = getenv("STRING_SESSION", "BQCecf7z7zSiCheLeynO8BINwZSu0hmIiS5jDDH8qpspM4Fhve8k99LxrvfNmc9IpObX4cqTXf97BSDWp-s6O2yHoiSylMK9sEvkPPlg24OQLrhYpZWbiPNPR-E4EwmEFKkc6TDFl1vn24jQG8KdzHQD7KQBGDWlqcFgVFkiU8IrLHP43DtGQJUiMuDYVlU4lfHju-xgeW6q6Sp60v2ptulAt2lm3j-QAD-esTeQGgrV1VyvJw8AH2smDRWUIRiPJcfa365WER3LZ-bUpRdT7WQ4vmfZGeIaVLR6mXySWPYZzCAkSziwg454bkXG1Cw2raduJc4EOLFula3h8tpxfcV_AAAAAUBfQeEA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5374951905").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/MYSTERIOUS_CHATS")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RTH_FIGHTERS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (- ❛𝗠𝘁𝘀 ➻ 𝗕𝗿𝗼𝗸𝗲𝗻 𝗕𝗼𝘆 [🇮🇳]) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/MYSTERIOUS_CHATS")
