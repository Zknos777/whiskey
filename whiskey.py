from telethon.sessions import StringSession
import asyncio
from telethon.sync import TelegramClient


# Замените значения на свои API_ID, API_HASH и токен бота
api_id = 28549753
api_hash = 'e791cfb046dd21c5080701aa733a2a51'
client = TelegramClient(StringSession(), api_id, api_hash)
    
async def whiskey(): 
    text = '/whiskey@WhiskeyUseBot'
    while True:              
         await client.send_message('https://t.me/+xSK71gkKO2hjMjIy', text)
         await asyncio.sleep(3661)
         
        
if __name__ == '__main__':
    print("#Start")
    with client:
        client.loop.run_until_complete(whiskey())
    print('Stop')