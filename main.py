from pyrogram import Client, filters
from os import environ

app = Client("AutoForwarder", api_id=int(environ["2092870"]), api_hash=environ["d7f5fb245e4c0b489cba4f7b45bc4173"],
             phone_number=environ["+917501563507"],
             session_string=environ["BQAf70YAH6LMJOSY5pr51OTjJilyYJibU_bJsMaqUyPaZUhQhcCIUYyBDOM3Pc-hpVjAOOXMN-8xLNiOhExnS4rsN4lQ0V2owAwLZJoTMjm22RZ2OZGqn9WFzUuWgUSCLkPQuBJF6vqN9uc1WbyzJMShCoq5IbGi_WQQyEF3hCucRHTmuVSQKsA1mKmn2IrbI7PXJ9oMLNAzLlr-VpHnfT3NeJDz1uo4zjsQ2T1SKzYiK-u5vP4AhxuryFdWXx3TPI-2bUmWl07KzmGDgWyDIQn3BOLcLf5TGp2Wjqvi0V7bmXt0UFTXMfjTGc48QJlVe50Y1iD9le4JJC5rKXqmSkV4A-CAYQAAAAFMoZQLAA"]
             )

@app.on_message(filters.regex(".start") & filters.me)
async def start(app, msg):
    await msg.reply("<b>Hello I'm A Auto Join Request Accept Bot\n\nMade In India :) By @PiroAyush</b>")

@app.on_message(filters.regex("/accept") & filters.me)
async def run(app, msg):
    await msg.reply("")
    X = "acceser"
    get = await app.get_messages(chat_id=X, message_ids=3)
    getint = int(get.text)
    while get.text != "none":
        get = await app.get_messages(chat_id=X, message_ids=3)
        await app.approve_all_chat_join_requests(getint)
        if get.text == "none":
            break        

print("Bot Is Alive..")
app.run()
