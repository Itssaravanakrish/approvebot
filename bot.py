import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("Support Group 👥", url="https://t.me/No1_Bots_SupportGroup"),
      InlineKeyboardButton("Updates Channel 📢", url="https://t.me/No1_Bots")
      ],[
      InlineKeyboardButton("Bot List 🤖", url=f"https://t.me/No1_Bots/11")
      ]]
    await message.reply_text(text="**__Heyy, {user} Iam Auto Approved Join Request Bot**__

**__• I can Auto approve new join requests In Channels And Groups
• Make Me Admin In Ur Channel Or Group With Invite Users Permission, Then See The magic ✨.**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
        print("Welcome....")

print("Auto Approved Bot")
pr0fess0r_99.run()
