"""
This function is the server file
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector as analyze_emotion
app = Flask('app_emotion')

"""return index.html"""
@app.route("/")
def render_index_page():
    return render_template('index.html')

"""emotion detector route"""
@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = analyze_emotion(text_to_analyze)

    if response[1] == 200:
        if response[0]['dominant_emotion'] not in response[0]:
            return ("Invalid Text! Please try again!")
        anger = response[0]['anger']
        disgust = response[0]['disgust']
        fear = response[0]['fear']
        joy = response[0]['joy']
        sadness = response[0]['sadness']
        dominant_emotion = response[0]['dominant_emotion']
        return (
        "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {},"
        " 'joy': {} and 'sadness': {}. The dominant emotion is {}."
        ).format(anger, disgust, fear, joy, sadness, dominant_emotion)
    if response[1] == 400:
        return "Invalid Text! Please try again!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
