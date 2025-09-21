You are an expert synthetic data generator. Your mission is to create a large and diverse dataset of **relevant segments** from educational videos. This data will be used to fine-tune a Large Language Model (LLM) to identify and extract core educational content, such as key explanations, definitions, and problem-solving demonstrations.

You will generate a list of JSON objects. Each JSON object represents a single data entry and must strictly adhere to the following structure:

```json
{{
  "video_topic": "A specific topic within a university-level discipline.",
  "segment_description": "A concise, third-person description of the core educational concept being taught in the video segment, including both visual and auditory elements.",
  "subtitle": "The verbatim transcript of the on-topic audio from the segment. This should sound like a natural and authentic explanation from an instructor.",
  "label": "Relevant"
}}
```

### **Instructions for Generating Data**

Follow these steps to create each JSON object:

1.  **Given a `video_topic`**: {}. Be precise. For example, instead of "Chemistry," use "Understanding Covalent Bonds in Organic Molecules."
2.  **Create the Relevant Scenario**: Use the **Types of Relevant Content** list as inspiration to create a realistic teaching moment. The `segment_description` must describe this core educational content, and the `subtitle` must contain the corresponding on-topic audio.
3.  **Set the `label`**: The `label` for every single entry you generate **must be 'Relevant'**.

### **Key Guidelines**

  * **Realism**: The `subtitle` should sound like a real instructor speaking, including natural pauses, rephrasing for clarity, and a conversational teaching tone. Avoid sounding like a textbook being read aloud.
  * **Diversity**: Extensively mix and match video topics with different types of relevant content. A definition in a philosophy lecture should feel different from a code walkthrough in a computer science tutorial.
  * **Clarity and Value**: The content of the `subtitle` should be genuinely educational, clearly explaining a concept, demonstrating a process, or defining a term.
  * **Volume**: Your primary goal is to generate as many unique, high-quality examples of relevant segments as possible in a single response.

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

-----

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

1.  **Given a `video_topic`**: {}. Be precise. The entire generation must focus exclusively on this single topic.
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