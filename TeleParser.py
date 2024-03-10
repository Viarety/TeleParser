from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import InputPeerChat
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio

api_id = your api_id
api_hash = 'your api_hash'

client = TelegramClient('TeleParser', api_id, api_hash)

async def get_user_info(username):
    async with client:
        try:
            target_group_entity = await client.get_entity(username)
            participants = await client.get_participants(target_group_entity, aggressive=True)
            for participant in participants:
                print(participant)
        except Exception as e:
            print(e)

username = input('Enter Telegram username: ')
asyncio.run(get_user_info(username))
