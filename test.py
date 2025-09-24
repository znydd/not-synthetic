from openai import OpenAI
import json
import re


def get_msg(info):
    return [
        {"role":"user",
        "content":[
                {"type":"text",
                "text":f"""You are an AI assistant specializing in educational content analysis.
                Your task is to analyze segments from educational videos with 3 fields
    video_topic: The overall subject of the entire video lecture.
    segment_description: A brief summary of the actions and content within the specific video clip.
    subtitle: The verbatim transcription of the audio from the segment.
    and classify them as either "Relevant" or "Irrelevant" to the main video topic. This is a binary classification task and your answer will only consist
    **"Relevant"** or **"Irrelevant"** nothing else. 

    Here is the 3 fields of a segment:

    {info}

    This Segment is:
    """}]}]

def llm_res(fields):
    client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="not-needed")
    response = client.chat.completions.create(model="gemma-3-1b-it-BF16.gguf", messages=get_msg(fields),stream=False)
    llm_output = response.choices[0].message.content
    # pattern = r"<think>.*?</think>"
    # return re.sub(pattern, "", llm_output, flags=re.DOTALL).strip()
    return llm_output

def main():
    with open("data/relevant_full.json", "r", encoding='utf-8') as f:
        data = json.load(f)
    with open("test/relevant_test_base.txt", "a",encoding="utf-8") as g:
        for idx, seg in enumerate(data):
            fields = ""
            fields+="video_topic: "+seg["video_topic"]+"\n"+"segment_description: "+seg["segment_description"]+"\n"+"subtitle: "+seg["subtitle"]
            resp = llm_res(fields)
            print(resp)
            g.write(resp+"\n")
            print(f"✅✅ {idx}/2602 ✅✅")

if __name__ == "__main__":
    main()

