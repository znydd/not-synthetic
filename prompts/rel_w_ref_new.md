You are an expert synthetic data generator. Your mission is to create a large and diverse dataset of **relevant segments** from educational videos. This data will be used to fine-tune a Large Language Model (LLM) to identify and extract core educational content.

You will generate a list of JSON objects. Each JSON object represents a single data entry and must strictly adhere to the following structure:

```json
{
  "video_topic": "A specific topic from the provided list.",
  "segment_description": "A concise, third-person description of the core educational concept being taught in the video segment.",
  "subtitle": "The verbatim transcript of the on-topic audio from the segment. This should sound like a natural and authentic explanation from an instructor.",
  "label": "Relevant"
}
```

### **Instructions for Generating Data**

Follow these steps to create each JSON object:

1.  **Select a `video_topic`**: Choose a topic **exclusively** from the **Video Topics** list provided below.
2.  **Create the Relevant Scenario**: Use the **Types of Relevant Content** list as inspiration to create a realistic teaching moment that fits the selected topic. The `segment_description` must describe this core content, and the `subtitle` must contain the corresponding audio.
3.  **Set the `label`**: The `label` for every single entry you generate **must be 'Relevant'**.

### **Key Guidelines**

  * **Realism**: The `subtitle` should sound like a real instructor speaking, including natural pauses, rephrasing for clarity, and a conversational teaching tone.
  * **Diversity**: Mix and match the provided video topics with different types of relevant content.
  * **Clarity and Value**: The content should be genuinely educational, clearly explaining a concept or demonstrating a process from the chosen video topic.
  * **Volume**: Your primary goal is to generate as many unique, high-quality examples as possible in a single response.

-----

### **Examples**

**Example 1: Core Concept Explanation**

```json
{
  "video_topic": "Functional Dependencies and Normalization for Relational Databases",
  "segment_description": "The instructor explains the concept of a functional dependency (FD) using the notation X -> Y, clarifying that the value of attribute set X uniquely determines the value of attribute set Y.",
  "subtitle": "So, the core idea here is what we call a functional dependency. Let's say we have two sets of attributes, X and Y. We write it as X with an arrow pointing to Y. This simply means that the value of X uniquely determines the value of Y. If you know the value for X in any given row, you will know for certain what the value for Y is. It cannot be anything else. This is the foundation for all of normalization.",
  "label": "Relevant"
}
```

**Example 2: Worked Problem / Demonstration**

```json
{
  "video_topic": "Subnetting and IP Addressing in Computer Networks",
  "segment_description": "The instructor demonstrates how to subnet a Class C network address, 192.168.1.0, into four smaller subnets by borrowing two bits from the host portion of the address.",
  "subtitle": "Okay, let's do a practical example. We have the address 192.168.1.0 with a default /24 mask. The requirement is to create four subnets. So, to get four subnets, how many bits do we need to borrow? We use the formula two to the power of n... so two to the power of two gives us four. We'll borrow two bits from the host portion. Our new subnet mask will be /26, or 255.255.255.192. Now let's calculate the network addresses for each of these new subnets.",
  "label": "Relevant"
}
```

**Example 3: Definition of a Key Term**

```json
{
    "video_topic": "A lecture on Support Vector Machines (SVM), covering the definition, application in classification and regression, and the concepts of hyperplanes, margins, and support vectors.",
    "segment_description": "The instructor defines the 'margin' in the context of an SVM classifier, explaining it as the distance between the separating hyperplane and the closest data points from either class.",
    "subtitle": "Now you'll hear the term 'margin' a lot with SVMs. What is it? The margin is simply the distance between the decision boundary—our hyperplane—and the nearest data point from either class. These nearest points are called support vectors. The goal of the SVM is not just to find any hyperplane that separates the data, but to find the one that maximizes this margin, which gives us better generalization.",
    "label": "Relevant"
}
```

-----

### **Source Material for Generation**

#### **Video Topics (Use Only These)**

  * Mapping EER Model Constructs to Relations, focusing on options for Specialization and Generalization.
  * Database Systems: ER-to-Relational Mapping Algorithm
  * Functional Dependencies and Normalization for Relational Databases
  * Database Normalization and Functional Dependencies
  * A comprehensive tutorial on using various MySQL SELECT query keywords and functions for data retrieval.
  * An educational lecture on Indexing and Hashing in Database Systems, covering concepts like index files, B+ trees, static hashing, hash functions, and handling bucket overflows.
  * Database Indexing with B+ Trees
  * An educational lecture on Chapter 14: Indexing, covering basic concepts, types of indices, and B+-Trees for database systems.
  * Relational Database Design: ER-to-Relational Mapping Algorithm
  * An educational lecture on Transaction Processing in databases, covering Concurrency Control and Recovery.
  * Database Transactions and ACID Properties
  * Introduction to PID (Proportional-Integral-Derivative) Control System Theory in Robotics
  * Introduction to Robotics: Block Diagram Solving and Summing Points
  * Introduction to Robotics: Control System Theory
  * Introduction to Robotics: Robot Navigation
  * Introduction to Robotics: A lecture on Robot Navigation, focusing on Mapping and Exploration using the Occupancy Grid (OG) mapping algorithm and the Frontier Based Exploration technique.
  * An educational guide on how to prepare and deliver a webinar presentation for the ENG091 course.
  * A classroom lecture on analyzing and answering reading comprehension questions, focusing on structure, language, and content organization.
  * Guidance on Writing a Narrative Essay Outline
  * An introduction to data structures, focusing on the concepts of arrays, lists, and the operations of shifting and rotating array elements.
  * Probability Theory and Naive Bayes Classifier
  * A lecture on Support Vector Machines (SVM), covering the definition, application in classification and regression, and the concepts of hyperplanes, margins, and support vectors.
  * An educational lecture on the concept, benefits, and implementation of dummy headed linked lists in data structures.
  * Subnetting and IP Addressing in Computer Networks

#### **Types of Relevant Content**

  * **Core Explanations**: Defining a key term, explaining a fundamental theory or concept, presenting a hypothesis, explaining the steps of a process.
  * **Demonstrations & Walkthroughs**: Solving a problem step-by-step, live-coding a function or algorithm, demonstrating a technique.
  * **Analysis & Comparison**: Comparing and contrasting two different theories, analyzing a case study, interpreting results.
  * **Summaries & Recaps**: Summarizing key takeaways, recapping previous content before introducing a new topic.
  * **Visual Aid Explanation**: Describing a diagram, chart, map, or model shown on screen to illustrate a point.

Proceed to generate a large list of diverse JSON objects, ensuring every entry has the label 'Relevant'.