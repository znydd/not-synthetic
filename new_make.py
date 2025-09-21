from openai import OpenAI
import random

TEMP = set()
TOPIC = ['Business Administration/Management',
 'Accounting',
 'Finance',
 'Marketing',
 'Economics',
 'International Business',
 'Entrepreneurship',
 'Nursing',
 'Health Professions and Related Programs',
 'Biology/Biological Sciences (pre-med track)',
 'Biomedical Sciences',
 'Public Health',
 'Physical Therapy',
 'Pharmacy',
 'Medical Assisting',
 'Psychology',
 'Sociology',
 'Political Science',
 'Anthropology',
 'History',
 'Criminology/Criminal Justice',
 'Social Work',
 'Biology',
 'Biochemistry',
 'Microbiology',
 'Neuroscience',
 'Environmental Science',
 'Biotechnology',
 'Mechanical Engineering',
 'Electrical Engineering',
 'Civil Engineering',
 'Chemical Engineering',
 'Aerospace Engineering',
 'Industrial Engineering',
 'Engineering Technologies',
 'Computer Science',
 'Information Technology',
 'Software Engineering',
 'Data Science',
 'Cybersecurity',
 'Artificial Intelligence',
 'Elementary Education',
 'Secondary Education',
 'Special Education',
 'Educational Leadership',
 'Early Childhood Education',
 'English Language and Literature',
 'Philosophy',
 'Liberal Arts and Sciences/General Studies',
 'Visual and Performing Arts (e.g., Fine Arts, Theater, Music)',
 'Communications/Journalism',
 'Graphic Design',
 'Foreign Languages and Literatures',
 'Physics',
 'Chemistry',
 'Mathematics',
 'Statistics',
 'Astronomy',
 'Geology/Earth Sciences',
 'Agriculture and Related Sciences',
 'Architecture',
 'Law (Pre-Law tracks)',
 'Hospitality and Tourism Management',
 'Sports Management/Parks and Recreation',
 'Culinary Arts',
 'Veterinary Technology']

TOPIC_E = ['Law (Pre-Law tracks)',
 'Hospitality and Tourism Management',
 'Sports Management/Parks and Recreation',
 'Culinary Arts',
 'Veterinary Technology',
"Mapping EER Model Constructs to Relations, focusing on options for Specialization and Generalization."
"Database Systems: ER-to-Relational Mapping Algorithm",
"Functional Dependencies and Normalization for Relational Databases",
"Database Normalization and Functional Dependencies",
"A comprehensive tutorial on using various MySQL SELECT query keywords and functions for data retrieval.",
"An educational lecture on Indexing and Hashing in Database Systems, covering concepts like index files, B+ trees, static hashing, hash functions, and handling bucket overflows.",
"Database Indexing with B+ Trees",
"An educational lecture on Chapter 14: Indexing, covering basic concepts, types of indices, and B+-Trees for database systems.",
"Relational Database Design: ER-to-Relational Mapping Algorithm",
"An educational lecture on Transaction Processing in databases, covering Concurrency Control and Recovery.",
"Database Transactions and ACID Properties",
"Introduction to PID (Proportional-Integral-Derivative) Control System Theory in Robotics",
"Introduction to Robotics: Block Diagram Solving and Summing Points",
"Introduction to Robotics: Control System Theory",
"Introduction to Robotics: Robot Navigation",
"Introduction to Robotics: A lecture on Robot Navigation, focusing on Mapping and Exploration using the Occupancy Grid (OG) mapping algorithm and the Frontier Based Exploration technique.",
"An educational guide on how to prepare and deliver a webinar presentation for the ENG091 course.",
"A classroom lecture on analyzing and answering reading comprehension questions, focusing on structure, language, and content organization.",
"Guidance on Writing a Narrative Essay Outline",
"An introduction to data structures, focusing on the concepts of arrays, lists, and the operations of shifting and rotating array elements.",
"Probability Theory and Naive Bayes Classifier",
"A lecture on Support Vector Machines (SVM), covering the definition, application in classification and regression, and the concepts of hyperplanes, margins, and support vectors.",
"An educational lecture on the concept, benefits, and implementation of dummy headed linked lists in data structures.",
"Subnetting and IP Addressing in Computer Networks",
 ]


def generate(prompt):
    global TEMP
    client = OpenAI(
        api_key="AIzaSyB-5Cx4p8yoqUnhctGRUIg1fR2bcaugog0", 
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    msg = [
        {"role": "system", "content": "You are one of the best expert specializing in Synthetic data generation."},
        {"role": "user", "content": prompt}
    ]
    temp = 0.0
    while True:
        temp = round(random.uniform(1.20, 1.80), 2) 
        if temp not in TEMP:
            TEMP.add(temp)
            break


    response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=msg,
    temperature=temp,
    )

    # print(response.choices[0].message.content)
    print(temp)
    return response.choices[0].message.content

def irr_prompt(topic):
    return f"""You are an expert synthetic data generator. Your mission is to create a large and diverse dataset of **irrelevant segments** from educational videos. This data will be used to fine-tune a Large Language Model (LLM) to detect and flag off-topic or disruptive content.

You will generate a list of JSON objects. Each JSON object represents a single data entry and must strictly adhere to the following structure:

```json
{{
  "video_topic": "A specific topic within a university-level discipline.",
  "segment_description": "A concise, third-person description of the irrelevant event happening in the video segment, including both visual and auditory elements.",
  "subtitle": "The verbatim transcript of the off-topic audio from the segment. This should sound natural and authentic.",
  "label": "Irrelevant"
}}
```

### **Instructions for Generating Data**

Follow these steps to create each JSON object:

1.  **Given a `video_topic`**: {topic}. Be precise. For example, instead of "Chemistry," use "Understanding Covalent Bonds in Organic Molecules. Also within the video topic
use all sort of sub-topic"
2.  **Create the Irrelevant Scenario**: Use the **Types of Irrelevant Scenarios** list as inspiration to create a realistic distraction that interrupts the educational content. The `segment_description` must describe this distraction, and the `subtitle` must contain the corresponding off-topic audio.
3.  **Set the `label`**: The `label` for every single entry you generate **must be 'Irrelevant'**.

### **Key Guidelines**

  * **Realism**: The `subtitle` should sound like a real person speaking, including natural hesitations, filler words ("um," "uh," "so"), and conversational phrasing.
  * **Diversity**: Extensively mix and match video topics with different types of irrelevant scenarios. An interruption in a history lecture should feel different from one in a coding tutorial.
  * **Creativity**: Combine different types of irrelevance for more complex and realistic examples (e.g., a pet walking into view while the instructor is troubleshooting a technical glitch).
  * **Volume**: Your primary goal is to generate as many unique, high-quality examples of irrelevant segments as possible in a single response.

-----

### **Examples**

**Example 1: Administrative Distraction**

```json
 {{
   "video_topic": "Mapping EER Model Constructs to Relations, focusing on options for Specialization and Generalization.",
   "segment_description": "The instructor provides administrative instructions about the exam, explaining how students should approach questions related to the mapping options if a specific method is not explicitly requested in the problem.",
   "subtitle": "In the exam, if no option is mentioned, you can use any applicable option. You have to choose one option for each subclass-superclass. And, um, if the option is mentioned, sometimes the option is mentioned, that's why you have to learn all four.",
   "label": "Irrelevant"
 }}
```

**Example 2: Technical & Audio Distraction**

```json
{{
  "video_topic": "Neuroscience: The Action Potential",
  "segment_description": "The instructor's lecture is interrupted by a series of loud notification sounds from their computer. The instructor gets flustered and verbally tries to troubleshoot the issue while the presentation slide remains static.",
  "subtitle": "So the sodium-potassium pump is crucial for restoring the... oh, hold on. Gosh, sorry about that. Let me figure out how to turn these notifications off. Is it in settings? I can never remember. One second, everyone.",
  "label": "Irrelevant"
}}
```

**Example 3: Off-Topic Personal Anecdote**

```json
{{
    "video_topic": "Civil Engineering: Principles of Stress and Strain in Materials",
    "segment_description": "The instructor pauses the lesson on material elasticity to tell a personal story about their weekend home renovation project, which is unrelated to the academic principles being taught.",
    "subtitle": "Which, you know, reminds me of this weekend. I was trying to install a new countertop and the whole thing just... it wouldn't fit. I spent hours on it. My back is still killing me. Anyway, where were we? Ah, yes, Young's modulus.",
    "label": "Irrelevant"
}}
```

-----

### **Source Material for Generation**

#### **Types of Irrelevant Scenarios**

  * **Audio-Only**: Background noise (dogs, traffic), off-camera interruptions (family questions), phone notifications, off-topic small talk, unrelated personal anecdotes, excessive filler words ("um," "ahh"), audio feedback/echo, unrelated music, technical troubleshooting audio ("Why isn't this working?"), participant chit-chat, coughing/sneezing, doorbells.
  * **Visual-Only**: Blank/frozen screens, irrelevant desktop pop-ups (email, social media), teacher checking phone, background distractions (pets, family walking by), screen saver activation, accidental display of personal photos/tabs, camera adjustments, ads/banners, accidental screen shares of wrong window.
  * **Audio-Visual Combined**: Pre-class setup routines ("Can you hear me?"), break announcements ("Let's take 5 minutes"), off-topic QNA, technical glitches with verbal commentary ("Hold on, let me fix this"), unrelated jokes/memes, non-academic polls ("What's your favorite food?"), extended goodbyes, waiting for software to load, participant introductions about hobbies, platform tutorials ("Here's how to use the chat").
  * **Silent/Blank Moments**: Extended silences while the instructor thinks, long waits for student responses, transition pauses between slides, muted segments where the instructor is talking, end-of-video dead air, instructor stepping away from the camera.

Proceed to generate a large list of diverse JSON objects, ensuring every entry has the label 'Irrelevant'."""

def rel_prompt(topic):
    return f"""
You are an expert synthetic data generator. Your mission is to create a large and diverse dataset of **relevant segments** from educational videos. This data will be used to fine-tune a Large Language Model (LLM) to identify and extract core educational content, such as key explanations, definitions, and problem-solving demonstrations.

You will generate a list of JSON objects. Each JSON object represents a single data entry and must strictly adhere to the following structure:

```json
{{
  "video_topic": "A specific topic within a university-level discipline.",
  "segment_description": "A concise, third-person description of the core educational concept being taught in the video segment, including both visual and auditory elements.",
  "subtitle": "The verbatim transcript of the on-topic audio from the segment. This should sound like a natural and authentic explanation from an instructor.",
  "label": "Relevant"
}}
````

### **Instructions for Generating Data**

Follow these steps to create each JSON object:

1.  **Given a `video_topic`**: {topic}. Be precise. The entire generation must focus exclusively on this single topic.
2.  **Create the Relevant Scenario**: Use the **Types of Relevant Content** list as inspiration to create a realistic teaching moment. The `segment_description` must describe this core educational content, and the `subtitle` must contain the corresponding on-topic audio.
3.  **Set the `label`**: The `label` for every single entry you generate **must be 'Relevant'**.

### **Key Guidelines**

  * **Realism**: The `subtitle` should sound like a real instructor speaking, including natural pauses, rephrasing for clarity, and a conversational teaching tone. Avoid sounding like a textbook being read aloud.
  * **Diversity**: Generate a wide range of different content types (explanations, demonstrations, etc.) for the **single, provided video topic**.
  * **Clarity and Value**: The content of the `subtitle` should be genuinely educational, clearly explaining a concept, demonstrating a process, or defining a term.
  * **Volume**: Your primary goal is to generate as many unique, high-quality examples of relevant segments as possible in a single response, all focused on the provided topic.

-----

### **Examples**

**Example 1: Core Concept Explanation**

```json
{{
  "video_topic": "Biology: The Process of Photosynthesis in Plants",
  "segment_description": "The instructor explains the two main stages of photosynthesis, the light-dependent reactions and the Calvin cycle, using a diagram on the slide to point out where each occurs within the chloroplast.",
  "subtitle": "Okay, so fundamentally, photosynthesis is a two-part process. First, you have the light-dependent reactions, happening right here in the thylakoid membranes. This is where the plant captures solar energy... um, to create ATP and NADPH. Then, that energy is used in the second stage, the Calvin cycle, which happens out here in the stroma, to convert carbon dioxide into glucose.",
  "label": "Relevant"
}}
```

**Example 2: Worked Problem / Demonstration**

```json
{{
  "video_topic": "Computer Science: Python 'for' loops",
  "segment_description": "The instructor is screen-sharing their code editor and live-codes a 'for' loop in Python to iterate through a list of numbers and print only the even ones, explaining the logic of the modulo operator as they type.",
  "subtitle": "So let's say we have a list of numbers, we'll call it `my_list`. To go through each item, we use a for loop. We'll say `for number in my_list:`. Now, inside the loop, we only want to print the even ones. The trick for that is the modulo operator. We can check if `number % 2 == 0`. If that's true, it means there's no remainder when divided by two, so... it's an even number. Let's print it.",
  "label": "Relevant"
}}
```

**Example 3: Definition of a Key Term**

```json
{{
    "video_topic": "Sociology: Theories of Social Stratification",
    "segment_description": "The instructor faces the camera and defines the core sociological concept of 'social stratification', providing a clear and concise explanation of what the term means and giving a brief example.",
    "subtitle": "Before we can compare theories from Weber and Marx, we need a solid definition of our key term: social stratification. Essentially, it refers to a society's categorization of its people into rankings based on factors like wealth, income, education, family background, and power. Think of it as a system of layers, or strata, where some groups have more resources than others.",
    "label": "Relevant"
}}
```
### **Source Material for Generation**

#### **Types of Relevant Content**

  * **Core Explanations**: Defining a key term, explaining a fundamental theory or concept, presenting a hypothesis, explaining the steps of a biological or chemical process.
  * **Demonstrations & Walkthroughs**: Solving a math or physics problem step-by-step, live-coding a function or algorithm, demonstrating a laboratory technique, analyzing a piece of literature or art, walking through a software interface.
  * **Analysis & Comparison**: Comparing and contrasting two different theories, analyzing a historical event or case study, interpreting the results of a scientific experiment, critiquing a philosophical argument.
  * **Summaries & Recaps**: Summarizing the key takeaways from a chapter or unit, recapping a previous lecture's content before introducing a new topic, providing a high-level overview of a complex system.
  * **Instructional Guidance**: Explaining how to use a specific formula, outlining the structure of an essay or lab report, providing context for an upcoming topic.
  * **Visual Aid Explanation**: Describing a diagram, chart, map, or model shown on screen to illustrate a point.
  * **On-Topic QNA**: Answering a student's question that directly clarifies a core concept for the rest of the class.

Proceed to generate a large list of diverse JSON objects, ensuring every entry has the label 'Relevant'.

    """



def msg_gen():
    global TOPIC
     
    with open("data/rel_new.txt", 'a', encoding="utf-8") as g:
        for idx, topic in enumerate(TOPIC_E):
            resp = generate(rel_prompt(topic))
            g.write(resp+"\n")
            print(f"✅ DONE {idx}/{28}")
        print("FULL DONE ✅✅✅✅✅✅")





    
def main():
    msg_gen()
    print("heno")

if __name__ == "__main__":
    main()
