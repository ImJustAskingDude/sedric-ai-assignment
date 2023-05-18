from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class TranscriptionResultFileContentTranscript:
    transcript: str


@dataclass(frozen=True)
class TranscriptionResultFileContentResults:
    transcripts: List[TranscriptionResultFileContentTranscript]


@dataclass(frozen=True)
class TranscriptionResultFileContent:
    jobName: str
    results: TranscriptionResultFileContentResults


# {
#     "jobName": "18ff38cb-7f9d-46a9-b43e-da06676934bd",
#     "accountId": "093767042774",
#     "results": {
#         "transcripts": [
#             {
#                 "transcript": "You still listening, gentlemen? That last few minutes might have been a little confusing. You'd like to know who I was talking to, wouldn't you? And I'll tell you what she looks like. You might find it interesting. She's beautiful but rather cool. She always wears a white shirt and she's got a good figure, but in a calm sort of way."
#             }
#         ],
#         "items": [
#             {
#                 "start_time": "0.56",
#                 "end_time": "0.759",
#                 "alternatives": [{"confidence": "0.998", "content": "You"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "0.769",
#                 "end_time": "1.049",
#                 "alternatives": [{"confidence": "0.999", "content": "still"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "1.059",
#                 "end_time": "1.35",
#                 "alternatives": [{"confidence": "0.999", "content": "listening"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": ","}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "1.36",
#                 "end_time": "1.879",
#                 "alternatives": [{"confidence": "0.995", "content": "gentlemen"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "?"}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "2.549",
#                 "end_time": "2.72",
#                 "alternatives": [{"confidence": "0.996", "content": "That"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "2.73",
#                 "end_time": "3.0",
#                 "alternatives": [{"confidence": "0.999", "content": "last"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.009",
#                 "end_time": "3.16",
#                 "alternatives": [{"confidence": "0.999", "content": "few"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.17",
#                 "end_time": "3.41",
#                 "alternatives": [{"confidence": "0.999", "content": "minutes"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.42",
#                 "end_time": "3.549",
#                 "alternatives": [{"confidence": "0.998", "content": "might"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.559",
#                 "end_time": "3.63",
#                 "alternatives": [{"confidence": "0.995", "content": "have"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.64",
#                 "end_time": "3.759",
#                 "alternatives": [{"confidence": "0.998", "content": "been"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.769",
#                 "end_time": "3.779",
#                 "alternatives": [{"confidence": "0.997", "content": "a"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.789",
#                 "end_time": "3.96",
#                 "alternatives": [{"confidence": "0.998", "content": "little"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "3.97",
#                 "end_time": "4.71",
#                 "alternatives": [{"confidence": "0.999", "content": "confusing"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "."}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "5.44",
#                 "end_time": "5.639",
#                 "alternatives": [{"confidence": "0.995", "content": "You'd"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "5.65",
#                 "end_time": "5.789",
#                 "alternatives": [{"confidence": "0.999", "content": "like"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "5.8",
#                 "end_time": "5.889",
#                 "alternatives": [{"confidence": "0.999", "content": "to"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "5.9",
#                 "end_time": "5.989",
#                 "alternatives": [{"confidence": "0.999", "content": "know"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "6.0",
#                 "end_time": "6.25",
#                 "alternatives": [{"confidence": "0.999", "content": "who"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "6.26",
#                 "end_time": "6.269",
#                 "alternatives": [{"confidence": "0.999", "content": "I"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "6.28",
#                 "end_time": "6.4",
#                 "alternatives": [{"confidence": "0.999", "content": "was"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "6.409",
#                 "end_time": "6.76",
#                 "alternatives": [{"confidence": "0.999", "content": "talking"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "6.769",
#                 "end_time": "6.889",
#                 "alternatives": [{"confidence": "0.998", "content": "to"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": ","}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "6.9",
#                 "end_time": "7.17",
#                 "alternatives": [{"confidence": "0.996", "content": "wouldn't"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "7.179",
#                 "end_time": "7.46",
#                 "alternatives": [{"confidence": "0.999", "content": "you"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "?"}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "8.039",
#                 "end_time": "8.13",
#                 "alternatives": [{"confidence": "0.75", "content": "And"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.14",
#                 "end_time": "8.199",
#                 "alternatives": [{"confidence": "0.87", "content": "I'll"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.21",
#                 "end_time": "8.369",
#                 "alternatives": [{"confidence": "0.999", "content": "tell"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.38",
#                 "end_time": "8.439",
#                 "alternatives": [{"confidence": "0.997", "content": "you"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.449",
#                 "end_time": "8.569",
#                 "alternatives": [{"confidence": "0.999", "content": "what"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.579",
#                 "end_time": "8.699",
#                 "alternatives": [{"confidence": "0.998", "content": "she"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.71",
#                 "end_time": "8.909",
#                 "alternatives": [{"confidence": "0.998", "content": "looks"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "8.92",
#                 "end_time": "9.369",
#                 "alternatives": [{"confidence": "0.999", "content": "like"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "."}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "10.06",
#                 "end_time": "10.189",
#                 "alternatives": [{"confidence": "0.999", "content": "You"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "10.199",
#                 "end_time": "10.359",
#                 "alternatives": [{"confidence": "0.999", "content": "might"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "10.369",
#                 "end_time": "10.609",
#                 "alternatives": [{"confidence": "0.999", "content": "find"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "10.619",
#                 "end_time": "10.67",
#                 "alternatives": [{"confidence": "0.998", "content": "it"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "10.68",
#                 "end_time": "11.5",
#                 "alternatives": [{"confidence": "0.999", "content": "interesting"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "."}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "12.21",
#                 "end_time": "12.659",
#                 "alternatives": [{"confidence": "0.968", "content": "She's"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "12.67",
#                 "end_time": "13.579",
#                 "alternatives": [{"confidence": "0.999", "content": "beautiful"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "13.59",
#                 "end_time": "13.699",
#                 "alternatives": [{"confidence": "0.999", "content": "but"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "13.71",
#                 "end_time": "14.06",
#                 "alternatives": [{"confidence": "0.999", "content": "rather"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "14.069",
#                 "end_time": "14.89",
#                 "alternatives": [{"confidence": "0.999", "content": "cool"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "."}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "15.0",
#                 "end_time": "15.25",
#                 "alternatives": [{"confidence": "0.998", "content": "She"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "15.26",
#                 "end_time": "15.55",
#                 "alternatives": [{"confidence": "0.999", "content": "always"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "15.56",
#                 "end_time": "15.789",
#                 "alternatives": [{"confidence": "0.996", "content": "wears"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "15.8",
#                 "end_time": "15.81",
#                 "alternatives": [{"confidence": "0.997", "content": "a"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "15.819",
#                 "end_time": "16.149",
#                 "alternatives": [{"confidence": "0.999", "content": "white"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "16.159",
#                 "end_time": "16.69",
#                 "alternatives": [{"confidence": "0.997", "content": "shirt"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "16.7",
#                 "end_time": "16.94",
#                 "alternatives": [{"confidence": "0.996", "content": "and"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "16.95",
#                 "end_time": "17.29",
#                 "alternatives": [{"confidence": "0.995", "content": "she's"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "17.299",
#                 "end_time": "17.45",
#                 "alternatives": [{"confidence": "0.997", "content": "got"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "17.459",
#                 "end_time": "17.469",
#                 "alternatives": [{"confidence": "0.998", "content": "a"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "17.479",
#                 "end_time": "17.649",
#                 "alternatives": [{"confidence": "0.999", "content": "good"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "17.659",
#                 "end_time": "18.12",
#                 "alternatives": [{"confidence": "0.999", "content": "figure"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": ","}],
#                 "type": "punctuation",
#             },
#             {
#                 "start_time": "18.129",
#                 "end_time": "18.26",
#                 "alternatives": [{"confidence": "0.998", "content": "but"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "18.27",
#                 "end_time": "18.45",
#                 "alternatives": [{"confidence": "0.997", "content": "in"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "18.639",
#                 "end_time": "18.649",
#                 "alternatives": [{"confidence": "0.996", "content": "a"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "19.1",
#                 "end_time": "19.709",
#                 "alternatives": [{"confidence": "0.997", "content": "calm"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "19.719",
#                 "end_time": "19.969",
#                 "alternatives": [{"confidence": "0.998", "content": "sort"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "19.979",
#                 "end_time": "20.069",
#                 "alternatives": [{"confidence": "0.997", "content": "of"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "start_time": "20.079",
#                 "end_time": "20.62",
#                 "alternatives": [{"confidence": "0.998", "content": "way"}],
#                 "type": "pronunciation",
#             },
#             {
#                 "alternatives": [{"confidence": "0.0", "content": "."}],
#                 "type": "punctuation",
#             },
#         ],
#     },
#     "status": "COMPLETED",
# }
