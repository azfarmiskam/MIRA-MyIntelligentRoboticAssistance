
import wolframalpha
import pyttsx3
import random

p = ("the answer is ", "it is ", "okay, ", "it's easy, ")
app_id = "55KWPY-9WX74R7U2L"
engine = pyttsx3.init()
# Taking input from user
while True:

    question = input('Question: ')
    client = wolframalpha.Client(app_id)
    res = client.query(question)

# Includes only text from the response
    answer = next(res.results).text
    engine.say(random.choice(p)+answer)
    print(answer)
    engine.runAndWait()
