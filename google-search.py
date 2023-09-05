import json
from serpapi import GoogleSearch

params = {
  "q": "what is the powerhouse of the cell",
  "location": "Naperville, Illinois, United States",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "2035296457b5d92d8f577ee0cc9839423d51404936d3fa7b12223dfc0cf8581d"
}

search = GoogleSearch(params)
results = search.get_dict()

json_results = search.get_json()

# open results.json and write the json_results
# make the json file sorted and orderly
with open('results.json', 'w') as outfile:
    json.dump(json_results, outfile, indent=4, sort_keys=True)

outfile.close()

"""
Snippet is the whole thing in the box
Snippet_highlighted_words is the bolded words in the box
Example: if you say what is the powerhouse of the cell, snippet will say mitochondria and a sentence explaining,
while snippet_highlighted_words will just say mitochondria.
"""

"""
USE ANSWERBOX ON SERPAPI DOCUMENTATION TO DO THIS IN A SIMPLER WAY so that you dont have to parse the json explicitly
"""

# open results.json and search for organic_results and print the first result
with open('results.json') as json_file:
    data = json.load(json_file)
    for p in data['organic_results']:
        print('Title: ' + p['title'])
        print('Link: ' + p['link'])
        print('Snippet: ' + str(p['snippet_highlighted_words']))
        print('Snippet: ' + p['snippet'])
        break

"""
OTHER OPTION

# open results.json and search for answer_box and print the answer box
with open('results.json') as json_file:
    data = json.load(json_file)
    for p in data['answer_box']:
        print('Answer Box: ' + p['answer'])
        break
"""

# LINKKKK
# open results.json and search for the first link available and print the link and the website name
with open('results.json') as json_file:
    data = json.load(json_file)
    for p in data['organic_results']:
        print('Link: ' + p['link'])
        print('Website Name: ' + p['displayed_link'])
        break

