from telethon.sessions import StringSession
import asyncio
from telethon.sync import TelegramClient


# Замените значения на свои API_ID, API_HASH и токен бота
session1='1BVtsOJcBu3HSGsLSmeQK-Ci78-bJ3ye4FELttDF5DpitkCBTKbORYKDEFiV7nzjzKAnNv6wWSPiD0K7eQbRJfTukljKXDcFEdIaEbbdW1pnNWgBgd-4X9wgcZ7dnFtqh5OchR1pPOWOq3buL0EbtfxGp0o30M1T8ZqGmUOOvGN5tEDSZTelUxDeTYXgBTwBpskFUoZzg-ALBjgZHB36238xeyKBSYxEJ_pMNpTa8me-zsJOp4nDQih6saAA4XVK5Vbtin6h38oWLUm-vcsNoPS5dTjj2tKz7OPNtoNTogVLT-Pc9Hj3Vftx8QX9VpblavTwPedL-TuttTBidYFW7Zp5fjOL-znE=' #OGqueen
session2 = "1ApWapzMBu3d_6R-rPwedz48w3u5TQly52OUx536rBUP22ORDnVVGaCSL374OC1FeyyNZv9ozYD8xYghi1OzHuofVF_1z14sBcIBgVR2S79Ag-puv2eMGZiLenORjhlUGqsE0tchR3nui4mElbo-kyesecN7HOVdHDA816pPiCokMo97Jom9R5UYZj6FsBOM_ZEzJWWbUGis9EJ6Exj3-SKWcEOlJyAudL1xtKtE8dAEkRXRATJqthzoCUY6-VFcmqGOBZnrmEXuZjyVklKGP76qr04t7pe-y6GdgSkVStwB17cHnrgYjnek70GMTxybpIF-YxCsAsB6Ruw5B85x5BtU3MO_9DYE=" #SergoAFK930


session3 = '1BJWap1sBuxVlChp0vtLyxmAR3uV-PzquPn4_poLhZGtofHZtd83NQSYJHXWlyv8pTyHs0JIwJFf-R_JpNO4Um02ipPLSBxYZ3Usca9vUyeihGjchYmTvCATB3RCJPRBbiSLEdtZbcBUCCUvtCwGy7RljaWDhW7pdJhMlwGwaZXsBCPzFiZolrd5sdwY_IXDc0D6oYSfPN3aUdfHlhUKfQ6JFBoOckIbfEXwXHeS4Jl4lISm5Z73Klwr_eLq9HFAOAlaP-hyQqefnjc51T6bjoVGdMdbU7atnPkM_vLbSrff6m0BUp34LOL9x1Mzw8j95hdE63BQf-jDVNkjNTOT0yAUw938SGNE=' #Sergo372

session4 = '1ApWapzMBu6tE5xQAtlyQDEl7CwBOZeY21V040NCpdOSMVTDk8CfUM65lyeVrP43lvi9b17vAfhL0m4ITW0FtzS7y_SDizuRH8Ys5o2W2UoO-M5RCZkXjLbILAEowKs_GxnvgvRcAYosrOkodPogX2rI98s0yEQmJdgoKtjVMlmW36c5yMCu9JfPj3bFCbgMYMKjp0MfefExTANI4142Wrbgs3xlTdWF6UWfqhs1uVJ5q_5xSFINPJ9JBYl_FU9lDMrNjY-kE21MM0H822sPyzJ5qhNGShd_2YzJCISZrxwInad_Jd7gYDSo-CVxmuJRkhNcMlVkLeeGkJcl6DLbVyc-aWuLTcqc=' #vik




api_id = 28549753
api_hash = 'e791cfb046dd21c5080701aa733a2a51'
client = TelegramClient(StringSession(), api_id, api_hash)
clients = [TelegramClient(StringSession(x), api_id, api_hash) for x in (session1, session2, session3, session4)]




#async def get_session():
#    string = client.session.save()
#    print(string)


async def whiskey(client): 
    text = '/whiskey@WhiskeyUseBot'
    #text = 'Ебать Ногинск'
    chatid= 'https://t.me/+xSK71gkKO2hjMjIy' #братвп
    #chatid = 'https://t.me/+7TbtH5r8k5w3NmFi' #test
    await client.start()
    await asyncio.sleep(5)
    print('Logged?')
    while True:              
         await client.send_message(chatid, text)
         await asyncio.sleep(3661)

                  
async def tsks():
    tasks = [asyncio.ensure_future(whiskey(x)) for x in clients]
    await asyncio.wait(tasks)
    
                    
if __name__ == '__main__':
    print("#Start")
    ioloop = asyncio.get_event_loop()
    print('Asynchronous:')
    ioloop.run_until_complete(tsks())
   # ioloop.close()
    print('Stop')