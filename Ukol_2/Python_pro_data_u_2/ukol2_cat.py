#   V zadání je uvedeno, že máme získat přesně 10 faktů, ale když jsem si otevřela odkaz: https://cat-fact.herokuapp.com/facts, tak je jich tam jen 5. V kódu níže tedy pracuji jen s těmito p5-ti fakty.

import requests
import json


timeout_seconds_1 = 0.001
timeout_seconds_2 = 2

try:
    response = requests.get("https://cat-fact.herokuapp.com/facts", timeout=timeout_seconds_2)
    data = response.json()

    filtered_text = [item['text'] for item in data if 'text' in item]
    print(filtered_text)

    numbered_list = [f"{i+1}. {sentence}" for i, sentence in enumerate(filtered_text)]
    for item in numbered_list:
        print(item)

except requests.Timeout:
    print("Jsi příliš nedočkavá.")


seznam =[
"1. Owning a cat can reduce the risk of stroke and heart attack by a third.",
"2. Most cats are lactose intolerant, and milk can cause painful stomach cramps and diarrhea. It's best to forego the milk and just give your cat the standard: clean, cool drinking water.",
"3. Domestic cats spend about 70 percent of the day sleeping and 15 percent of the day grooming.",
"4. The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.",
"5. Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs."
]

#print(seznam) #kontrolní print

with open("kocici_fakta.json", mode='w', encoding="utf-8") as output_file:
    json.dump(seznam, output_file, indent=4, ensure_ascii=False)