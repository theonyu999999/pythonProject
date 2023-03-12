# Make me something about Tesla.
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = ""

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

response =  openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "hello?"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": "What is Busan Global Village?"},
        {"role": "assistant", "content": "Busan Global Village is an area in the city of Busan, South Korea that is designed to promote cultural understanding and international exchange. It is home to a diverse group of foreigners and provides a space for people from all over the world to come together and share their cultures with one another. The area is comprised of several buildings, which are used for cultural events, language classes, and other community activities. It is a great place to experience a variety of cultures without leaving Busan."},
        {"role": "user", "content": "tell me about Kerbal Space Program 2."},
        {"role": "assistant", "content": "Kerbal Space Program 2 is an upcoming space flight simulation video game that follows on the success of the first Kerbal Space Program game. It is being developed by Intercept Games and published by Private Division. \n\nIn Kerbal Space Program 2, players will build and manage their own space program, constructing rockets, spaceplanes, rovers, and other space vehicles. They'll need to manage resources, plan missions, and execute real-world physics-based spaceflight maneuvers in order to explore and colonize other planets and celestial bodies. The game offers a variety of new features, such as new parts and engines, multiplayer mode, and an expanded technology tree. Additional improvements have been made to the game graphics and audio, making for a more immersive player experience.Kerbal Space Program 2 is highly anticipated by fans of the original game, and is expected to be released on PC, PS4 and Xbox One in 2022."},
        {"role": "user", "content": "can i say korean"},
    ]
)
print(response)