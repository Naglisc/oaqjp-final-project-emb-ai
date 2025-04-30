from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    if request.method == 'POST':
        text_to_analyze = request.form['text']
        emotion_result = emotion_detector(text_to_analyze)

        if emotion_result is None:
            return "Klaida vykdant emocijų analizę."
        else:
            anger = emotion_result['anger']
            disgust = emotion_result['disgust']
            fear = emotion_result['fear']
            joy = emotion_result['joy']
            sadness = emotion_result['sadness']
            dominant_emotion = emotion_result['dominant_emotion']

            formatted_response = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
            return formatted_response

    return "Kažkas negerai su užklausa."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)