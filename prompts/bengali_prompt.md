## **Primary Goal:**

Your primary task is to act as an intelligent multimodal video analysis tool. Your goal is to analyze the provided long-form educational video to identify and timestamp all segments that are irrelevant to the core academic topic. Following this identification, you will structure your complete findings into a single JSON object.

## **Video for Analysis:**

[Insert the link to the long educational video here. This can be a raw webinar recording, an unedited lecture, or a classroom session.]

## **Instructions for Analysis:**

Before generating the output, first determine if the video is in Bengali then you must first holistically understand the entire video to accurately in Bengali determine its main educational topic. This topic will serve as the baseline for identifying deviations. Once you have a clear understanding of the central theme, proceed with the following steps.

### **Criteria for Irrelevance:**

An "irrelevant segment" is defined as any portion of the video that deviates from the main educational subject matter. You should identify segments including, but not limited to:

*   **Off-Topic Discussions:** Conversations, stories, or anecdotes shared by the instructor or students that are not related to the academic content.
*   **Unrelated Questions and Answers:** Student questions or discussions that are tangential or irrelevant to the lesson's focus.
*   **Significant Pauses or Silence:** Extended periods where there is no active teaching, and the on-screen content (like a slide or whiteboard) is static and not being explained.
*   **Technical Difficulties:** Segments focused on resolving audio, video, or connectivity issues where no educational content is being delivered.
*   **Social Chatter:** Casual, non-academic conversations or small talk between participants.
*   **Administrative/Logistical Discussions:** Portions of the video focused on scheduling, grading, or other logistical matters not central to the subject being taught.

### **Required Output Format:**

Your final output must be a single, valid JSON object and all the output field will be in English. Do not include any text or explanations outside of the JSON structure.

The JSON object should have a top-level key `video_topic` and another top-level key `irrelevant_segments`, which is an array of objects. Each object within this array represents a single detected irrelevant segment.
For `start`, `end` in the `timestamps` field first carefully analyse the whole video length then put the irrelevant segement timestamps. Be careful about the timestamps as they are very sensitive.
Here `HH:MM:SS` means `Hours:Minutes:Seconds`

Ensure all string values within the JSON are in English. If the original language of the transcription is Bengali, you must provide an English translation.

**JSON Structure:**

```json
{
  "video_topic": "A concise title for the main educational subject of the entire video.",
  "irrelevant_segments": [
    {
      "timestamps": {
        "start": "HH:MM:SS",
        "end": "HH:MM:SS"
      },
      "segment_description": "A detailed description of why this segment is irrelevant, based on a combined analysis of visual, auditory, and activity cues from the video.",
      "subtitle": "The transcription of the spoken words from this segment. If the original language is Bengali, this must be the English translation."
    },
    {
      "timestamps": {
        "start": "HH:MM:SS",
        "end": "HH:MM:SS"
      },
      "segment_description": "Description for the next irrelevant segment found in the video.",
      "subtitle": "Transcription for the next irrelevant segment."
    }
  ]
}
```
