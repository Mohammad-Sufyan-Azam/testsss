from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
database = client.students
collection = database.get_collection("whatsapp")

def message_decoder(message):
    return {
        "id": message["id"],
        "time" : message["time"],
        "content" : message["content"]
    }

# Retrieve all messages with some logic
async def get_messages(grp_number):
    messages = []
    data =  collection.find_one({"group_number": grp_number})
    for msg in data["messages_1"]: # type: ignore
        messages.append(msg)
    return messages


@app.get("/")
async def root(): # type: ignore 
    # messages = []
    # data =  collection.find_one({"group_number": 1})
    # for msg in data["messages_1"]: # type: ignore
    #     messages.append(msg)
    # return messages
    return await get_messages(1)


# schema example 
# {
#   "_id": {
#     "$oid": "654005999477c954ba744cff"
#   },
#   "group_number": 1,
#   "messages_1": [
#     {
#       "id": 1,
#       "content": "hi sir"
#     },
#     {
#       "id": 2,
#       "content": "hi sir1"
#     }
#   ]
# }

