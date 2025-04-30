import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        response_json = response.json()
        if 'emotionPredictions' in response_json and response_json['emotionPredictions']:
            emotions = response_json['emotionPredictions'][0]['emotion']
            formatted_output = {
                'anger': emotions.get('anger', 0.0),
                'disgust': emotions.get('disgust', 0.0),
                'fear': emotions.get('fear', 0.0),
                'joy': emotions.get('joy', 0.0),
                'sadness': emotions.get('sadness', 0.0)
            }

            dominant_emotion = max(formatted_output, key=formatted_output.get)
            formatted_output['dominant_emotion'] = dominant_emotion
            return formatted_output
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during Emotion Predict API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

if __name__ == '__main__':
    text1 = "I love this new technology."
    emotion1 = emotion_detector(text1)
    print(f"Emotions for '{text1}': {emotion1}")

    text2 = "This is a terrible situation."
    emotion2 = emotion_detector(text2)
    print(f"Emotions for '{text2}': {emotion2}")