import json
from openai import OpenAI
import os
import random

PROMPT = """Rephrase the `video_topic`, `segment_description` and `subtitle` of the given json example and make 10 unique examples of json array
out of it exact same example just rephrase in a really good way. Keep realism and if any subtitle is really large then make it small by
condensing but make it looks like a real subtitle.
"""

def generate(prompt):
    client = OpenAI(
        api_key="AIzaSyC1M-UEamTHXS09n_jTYMDg5opb6kYxkmQ", 
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert assistant specializing in rephrasing sentences in unique way without changing its meaning."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.9,
    )

    # print(response.choices[0].message.content)
    return response.choices[0].message.content
    


def msg_gen():
    # load the ref file 
    # iterate every link irr
    # get llm out and save on array, keep seperation
    # append the whole thing on .txt
    global PROMPT
    with open("ref_data.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    msg = {"video_topic":"",
            "segment_description":"",
            "subtitle":"",
            "label":"Irrelevant"
           }
    with open("data/rephrased.txt", 'a', encoding="utf-8") as g:
        for vid in data:
            g.write(vid['link']+"\n")
            msg["video_topic"] = vid["video_topic"]
            ln = len(vid["irrelevant_segments"])
            for idx, segment in enumerate(vid["irrelevant_segments"]):
                msg["segment_description"]= segment["segment_description"]
                msg["subtitle"]= segment["subtitle"]
                prompt = f"```json[{msg}]```\n"
                prompt+=PROMPT
                # print(prompt)
                resp = generate(prompt)
                g.write(resp+"\n")
                print(f"=========={idx}/{ln}===========")
            print(f"✅ DONE {vid["link"]}")
        print("✅✅✅✅✅✅✅✅ ALL DONE")



    
def main():
    msg_gen()
    print("heno")

if __name__ == "__main__":
    main()
