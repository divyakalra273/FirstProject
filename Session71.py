from nltk.chat.util import Chat, reflections

# Chat is a Class which will handle Chat-Bot logic for us !
# reflections is a dictionary of key and value pairs, For a key as input we have an outcome as value
# print(reflections)
# print(reflections['i was'])
def chat(message):
    conversation = [
        [
            "Hi",
            ["Hey, What can i do for you ?", ]
        ],

        [
            "What is Your Name ?",
            ["My Name is John. Good to Talk to You !! What is your Name ?", ]
        ],

        [
            r"my name is (.*)",
            ["Hello %1, Its good to chat with You !! What programming languages you know?", ]
        ],

        [
            r"i know (.*)",
            ["OK!! So you can code in %1", "this is great that you know %1"]
        ],

    ]



    if message==conversation:
        chatBot = Chat(conversation, reflections)
    return chatBot.converse()

