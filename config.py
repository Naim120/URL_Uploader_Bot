import os

class Config(object):
    TG_BOT_TOKEN = "5076867859:AAGZzC3YIN64IMOboZTZJ6LD8bXhIQo7n6A" # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = 1492128 # Get this value from https://my.telegram.org/apps
    
    API_HASH = "496a1aab7943406f28e3de49fff16ea2" # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = 1185346119 # Your(owner's) telegram id
    
    MONGO_STR = "mongodb+srv://skdb:skdb12@cluster0.o9bn9.mongodb.net/skdb?retryWrites=true&w=majority"
" # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "./DOWNLOADS" # The download location for users. (Don't change anything in this field!)
