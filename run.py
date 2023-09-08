from pocketsphinx import LiveSpeech
from serpapi import GoogleSearch
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 140) 

engine.say("My name is ahl'yx... what you want bruv")
engine.runAndWait()

for phrase in LiveSpeech():
    if "alex" in phrase:
          engine.say("what")
          engine.runAndWait()
        
          phrase2 = LiveSpeech()
        
          params = {
          "q": str(phrase2),
          "location": "Naperville, Illinois, United States",
          "hl": "en",
          "gl": "us",
          "google_domain": "google.com",
          "api_key": "2035296457b5d92d8f577ee0cc9839423d51404936d3fa7b12223dfc0cf8581d"
          }
    
          search = GoogleSearch(params)
          results = search.get_dict()
          
          if "answer_box" in results:
            answer_box = results["answer_box"]
            if answer_box["type"] == "organic_result":
                engine.say(answer_box["snippet"])
                engine.runAndWait()
            elif answer_box["type"] == "knowledge_graph":
                engine.say(answer_box["description"])
                engine.runAndWait()
            elif answer_box["type"] == "answer_box":
                engine.say(answer_box["result"])
                engine.runAndWait()
            elif answer_box["type"] == "calculator_result":
                engine.say(answer_box["result"])
                engine.runAndWait()
            else:
                engine.say("what? did you say", phrase2 + "?")
                engine.runAndWait()
          else:
              engine.say("what? did you say", phrase2 + "?")
              engine.runAndWait()
