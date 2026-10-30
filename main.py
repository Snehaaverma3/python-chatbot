import datetime
import time
name = input("Sneha")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour < 12:
     print("Good Morning", name)
     
elif 12 <= presentHour < 17:
           print("Good Afternoon", name)
elif 17 <= presentHour < 21:
                 print("Good Evening", name)
else:
                       print("Good Night", name)

print("Welcome to your chatbot")
print("You can ask me basic question, Type 'bye' to exit the chat")

responses = {
"hello": "hi, welcome how can i help you",
"how are you":"I am fine, thanku for asking",
"who are you": "I am a chatbot, nice to meet you!",
"what is your name":
"I am ChatBot, your virtual AI assistant.",
"what can you do": "I can answer basic questions, chat with you, and help you practice Python!",
"good morning": "Good morning! Hope you have a wonderful day ahead!",
"good night": "Good night! Sleep well and take care!",
"thank you": "You're very welcome! Let me know if you need anything else.",
"thanks": "Happy to help!",
"bye": "Goodbye! Have a great day ahead!"
} 
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
            
    return "I am not able to tell that yet, I am still in learning mode"

while True:
  userInput = input("please ask me a question: ")
  reply = getResponseOfBot (userInput)
  print("Bot Responses:", reply)
  if "bye" in userInput. lower ():
   break
  