import os
import asyncio
import time
from telethon import TelegramClient, events
from dotenv import load_dotenv
from telethon.errors import FloodWaitError

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SOURCE_GROUP_ID = os.getenv("SOURCE_GROUP_CENTER")
TARGET_GROUP_ID = os.getenv("TARGET_GROUP_FINAL")

SOURCE_GROUP_INVITELINK = os.getenv("SOURCE_GROUP_INVITELINK")
CHANNEL_USERNAMES = [SOURCE_GROUP_INVITELINK]
# CHANNEL_USERNAMES = [SOURCE_GROUP_ID]

phone_number = os.getenv("PHONE_NUMBER")
client = TelegramClient('fury', API_ID, API_HASH).start(phone=phone_number)
forwarded_message_count = 0
last_reset_time = time.time()

async def copy_and_send_message(message, target_group_id):
    try:
        # if message.message:
        # target_group_id = await client.get_entity(TARGET_GROUP_INVITELINK)
        # await client.forward_messages(target_group_id, message)
        await client.forward_messages(TARGET_GROUP_ID, message)
        print("send successfully!")
        await asyncio.sleep(1.5)
    except FloodWaitError as e:
        print(f"FloodWait: Sleeping for {e.seconds} seconds.")
        await asyncio.sleep(e.seconds)
    except Exception as e:
        print(f"Error: {e}")

async def forward_to_group_with_limit(message, target_group_id, limit_per_minute=10):
    global forwarded_message_count, last_reset_time
        
    if time.time() - last_reset_time >= 60:
        forwarded_message_count = 0
        last_reset_time = time.time()
    if forwarded_message_count < limit_per_minute:
        await copy_and_send_message(message, target_group_id)
        forwarded_message_count += 1
    else:
        print("Rate limit reached. Waiting for the next cycle.")

@client.on(events.NewMessage(chats=CHANNEL_USERNAMES))
async def handler(event):
    print("new message arrived!")
    await forward_to_group_with_limit(event.message, TARGET_GROUP_ID)

async def main():
    await client.run_until_disconnected()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
