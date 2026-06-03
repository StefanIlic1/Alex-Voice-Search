from pocketsphinx import LiveSpeech
from serpapi import GoogleSearch
import pyttsx3
import os
import dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

engine = pyttsx3.init()
engine.setProperty('rate', 140) 

engine.say("My name is alex... what do you want")
engine.runAndWait()

for phrase in LiveSpeech():
    if "alex" in str(phrase):
          engine.say("what's up?")
          engine.runAndWait()
        
          phrase2 = str(LiveSpeech())
        
          params = {
          "q": phrase2,
          "location": "Naperville, Illinois, United States",
          "hl": "en",
          "gl": "us",
          "google_domain": "google.com",
          "api_key": API_KEY
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
                engine.say("what? did you say " + phrase2 + "?")
                engine.runAndWait()
          else:
              engine.say("what? did you say " + phrase2 + "?")
              engine.runAndWait()
