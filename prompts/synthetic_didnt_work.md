I am trying to make synthetic dataset for fine tuning a LLM to detect irrelevant segments or clips from a long educational video(unedited class or live class recording, webinder or seminer etc type of video). 
My approach is I have 3 information about a clip from that long educational video which are 
1) The topic of the whole video
2) Description of that clip(it contains everything on that clip like OCR info, activity info, basically what is happening or being taught on that clip)
3) The subtitle/transcript of that clip for auditori information

With these information the LLM will decide if this clip is irrelevant or not.
the data generation process will be like, I will provide an reference example which I have collected from an actual real life video
and the LLM have to create data entry like this with the above 3 field. Genereted data should be unique but its style, tone and content 
should be same like the reference example but the it will be in different words, not just a mere rephrase also keep realism with the
generated data. Also don't include any other irrelevant type just follow the one that will be provided. With these requirement create a 
prompt for Gemini 2.5 Pro to make these synthetic dataset




========================================================================================================================================


**Your Role:** You are an expert data scientist specializing in creating synthetic data for machine learning applications. Your current task is to generate a high-quality, realistic dataset for fine-tuning a Large Language Model (LLM). This LLM's purpose is to identify and flag irrelevant segments within long, unedited educational videos, such as class recordings, webinars, or seminars.

**The Goal:** Generate a user-specified number of unique, realistic data entries. Each entry must be a JSON object representing an "Irrelevant" clip from a longer educational video. An irrelevant clip, for the purpose of this task will be like the given in the <example></example>,but for rough context it may be a segment where the instructor or the listener discussing that off topic of the educational content or showing slides or board or doing other stuff but no one is talking.

**Key Requirements:**

1.  **JSON Format:** The output must be a valid JSON array of objects. Each object represents a single data entry and must contain the keys: `whole_video_topic`, `segment_description`, `subtitle`, and `label`.
2.  **Maintain Realism:** The content of each field should be authentic. The language should be natural and reflect real-world scenarios where it is an environment where instructor is teaching and students/listeners are listening or asking question just like a online class or it can be just the teacher is teaching and the video is unedited. 
3.  **Ensure Uniqueness:** Each JSON object you generate must be unique. Do not simply copy the reference example. Instead follow the tone and style of the example and create all the entries unique but don't change the topic but every should be worded differently in different and unique way.
4.  **Specific Irrelevance Type to Focus:** Focus **only** on the given example. Do not generate other type.
5.  **Adhere to Structure:** Strictly follow the JSON structure and key names as shown in the reference example. The value for the `label` key must always be "Irrelevant".

---

**Reference Example (for style, tone, and structure):**

```json
[
  {
    "video_topic": "Mapping EER Model Constructs to Relations, focusing on options for Specialization and Generalization.",
    "segment_description": "The instructor begins the online class by performing a routine audio check to ensure all participants can hear her before starting the lecture.",
    "subtitle": "Okay, hello, can you hear my voice? Yes ma'am.",
    "label": "Irrelevant"
  }
]
```

---

**Your Task:**

Now, generate **[10]** new, unique data entries in a single JSON array, following all the requirements listed above.