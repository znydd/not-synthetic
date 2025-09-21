You are an expert synthetic data generator. Your mission is to create a large and diverse dataset of **irrelevant segments** from educational videos. This data will be used to fine-tune a Large Language Model (LLM) to detect and flag off-topic or disruptive content.

You will generate a list of JSON objects. Each JSON object represents a single data entry and must strictly adhere to the following structure:

```json
{
  "video_topic": "A specific topic within a university-level discipline.",
  "segment_description": "A concise, third-person description of the irrelevant event happening in the video segment, including both visual and auditory elements.",
  "subtitle": "The verbatim transcript of the off-topic audio from the segment. This should sound natural and authentic.",
  "label": "Irrelevant"
}
```

### **Instructions for Generating Data**

Follow these steps to create each JSON object:

1.  **Given a `video_topic`**: {}. Be precise. For example, instead of "Chemistry," use "Understanding Covalent Bonds in Organic Molecules. Also within the video topic
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
 {
   "video_topic": "Mapping EER Model Constructs to Relations, focusing on options for Specialization and Generalization.",
   "segment_description": "The instructor provides administrative instructions about the exam, explaining how students should approach questions related to the mapping options if a specific method is not explicitly requested in the problem.",
   "subtitle": "In the exam, if no option is mentioned, you can use any applicable option. You have to choose one option for each subclass-superclass. And, um, if the option is mentioned, sometimes the option is mentioned, that's why you have to learn all four.",
   "label": "Irrelevant"
 }
```

**Example 2: Technical & Audio Distraction**

```json
{
  "video_topic": "Neuroscience: The Action Potential",
  "segment_description": "The instructor's lecture is interrupted by a series of loud notification sounds from their computer. The instructor gets flustered and verbally tries to troubleshoot the issue while the presentation slide remains static.",
  "subtitle": "So the sodium-potassium pump is crucial for restoring the... oh, hold on. Gosh, sorry about that. Let me figure out how to turn these notifications off. Is it in settings? I can never remember. One second, everyone.",
  "label": "Irrelevant"
}
```

**Example 3: Off-Topic Personal Anecdote**

```json
{
    "video_topic": "Civil Engineering: Principles of Stress and Strain in Materials",
    "segment_description": "The instructor pauses the lesson on material elasticity to tell a personal story about their weekend home renovation project, which is unrelated to the academic principles being taught.",
    "subtitle": "Which, you know, reminds me of this weekend. I was trying to install a new countertop and the whole thing just... it wouldn't fit. I spent hours on it. My back is still killing me. Anyway, where were we? Ah, yes, Young's modulus.",
    "label": "Irrelevant"
}
```

-----

### **Source Material for Generation**

#### **Types of Irrelevant Scenarios**

  * **Audio-Only**: Background noise (dogs, traffic), off-camera interruptions (family questions), phone notifications, off-topic small talk, unrelated personal anecdotes, excessive filler words ("um," "ahh"), audio feedback/echo, unrelated music, technical troubleshooting audio ("Why isn't this working?"), participant chit-chat, coughing/sneezing, doorbells.
  * **Visual-Only**: Blank/frozen screens, irrelevant desktop pop-ups (email, social media), teacher checking phone, background distractions (pets, family walking by), screen saver activation, accidental display of personal photos/tabs, camera adjustments, ads/banners, accidental screen shares of wrong window.
  * **Audio-Visual Combined**: Pre-class setup routines ("Can you hear me?"), break announcements ("Let's take 5 minutes"), off-topic Q\&A, technical glitches with verbal commentary ("Hold on, let me fix this"), unrelated jokes/memes, non-academic polls ("What's your favorite food?"), extended goodbyes, waiting for software to load, participant introductions about hobbies, platform tutorials ("Here's how to use the chat").
  * **Silent/Blank Moments**: Extended silences while the instructor thinks, long waits for student responses, transition pauses between slides, muted segments where the instructor is talking, end-of-video dead air, instructor stepping away from the camera.

Proceed to generate a large list of diverse JSON objects, ensuring every entry has the label 'Irrelevant'.