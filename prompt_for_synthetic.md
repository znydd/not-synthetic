**Persona:**

You are a Senior AI Data Architect. Your mission is to construct a benchmark synthetic dataset for fine-tuning a state-of-the-art language model (Gemma 3). The dataset's purpose is to teach the model to identify and segment "irrelevant" content within long, unedited educational videos. Your work must be meticulous, creative, and adhere strictly to the specified format.

**Primary Goal:**

Generate a large, diverse, and high-quality synthetic dataset of irrelevant video clip information. Each data entry must be a JSON object containing three specific keys: `whole_video_topic`, `description`, and `subtitle_transcription`.

**Critical Context & Definitions:**

An "irrelevant segment" is defined as any portion of an educational video that does not directly contribute to the pedagogical goals of the lesson. Your generated data must encompass the full spectrum of such scenarios.

<instructions>

**Step-by-Step Instructions:**

1.  **Internalize the Core Task:** Your primary directive is to create varied examples of off-topic or non-educational moments that commonly occur in live online classes, webinars, and workshops.

2.  **Analyze the Reference Examples:** Carefully study the provided few-shot examples within the `<examples>` block. These are your gold standard for style, tone, and structure.

3.  **Generate [150] New, Unique Entries:** Create a list of 150 new synthetic data entries. Do not simply rephrase or slightly alter the provided examples.

4.  **Prioritize Diversity:** This is a critical requirement. Ensure your generated data is diverse in two dimensions:
    *   **Scenario Diversity:** Distribute your examples across all of the following categories of irrelevance:
        *   **Technical Glitches:** Audio problems, screen share failures, software crashes, lag, presentation file issues.
        *   **Administrative Logistics:** Discussing schedules, assignments, links, resources, or how to use the webinar platform.
        *   **Pre-Session Banter:** Casual small talk and greetings while waiting for all attendees to join.
        *   **Off-Topic Anecdotes:** Personal stories or tangents not directly related to the subject matter.
        *   **External Interruptions:** Distractions from the instructor's environment (e.g., pets, family, deliveries, background noise).
        *   **Managing Audience (Off-Topic):** Reading and responding to irrelevant chat questions or comments.
        *   **Extended Pauses & Fillers:** Awkward silences, waiting for polls to complete, instructor temporarily stepping away.
    *   **Topic Diversity:** Use a very wide range of `whole_video_topic` values, from technical fields (e.g., "Cloud Computing with AWS," "C# for Beginners") to humanities (e.g., "Shakespearean Literature," "Post-War European History") and creative skills (e.g., "Watercolor Painting Techniques," "Music Theory 101").

5.  **Maintain Realism:** The `subtitle_transcription` should sound natural and unscripted, including filler words (`uh`, `um`, `so`), self-corrections, and colloquialisms typical of a live speaking situation. The `description` should be a concise, objective observation of the visual and contextual cues.

6.  **Adhere Strictly to Output Format:** This is non-negotiable. The final output must be a single, machine-readable JSON array.

</instructions>

**Output Format Specification:**

*   Your entire response **must** be a single, valid JSON array.
*   The array must contain exactly [150] JSON objects.
*   Each object must contain only these three keys: `whole_video_topic`, `description`, `subtitle_transcription`.
*   **Do not** include any introductory text (like "Here is the dataset you requested:"), concluding summaries, or any explanations outside of the main JSON array itself. Your response should begin with `[` and end with `]`.

<examples>
```json
[
  {
    "whole_video_topic": "Introduction to Quantum Computing",
    "description": "The instructor is looking at the screen, seemingly confused. His cursor is moving around the video conferencing software's settings menu. The main presentation slide is not visible.",
    "subtitle_transcription": "Okay, hold on everyone... is my screen sharing? I clicked the button but I don't think it's working. Can you see my slides or just my face? Someone let me know in the chat... ah, okay. Thanks, David. Let me try this again. Apologies for the delay."
  },
  {
    "whole_video_topic": "Data Visualization with Tableau",
    "description": "Close-up shot of the instructor's face as he talks directly to the camera in a casual tone before the main content has started. There are no educational visuals on screen.",
    "subtitle_transcription": "Alright, it's just about the top of the hour. We'll give everyone another minute or two to trickle in before we get started. I see a few familiar names in the attendee list, good to see you all again. Hope you're having a great week. I'm just getting over a bit of a cold myself."
  },
  {
    "whole_video_topic": "Advanced SEO Strategies",
    "description": "The video shows a static slide with the webinar title. The instructor is speaking, but the words are about logistics for a future session, not the current topic.",
    "subtitle_transcription": "And before I forget, for next week's session, make sure you have downloaded the project files from the portal. I sent an email about it yesterday. If you have any trouble, just email the support address. Okay, so... let's see where we were."
  }
]
</examples>
Proceed with generating the dataset.