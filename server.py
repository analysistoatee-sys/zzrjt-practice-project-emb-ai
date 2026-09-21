from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


def analyze_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, "
        "'sadness': {}. The dominant emotion is {}."
    ).format(
        response["anger"],
        response["disgust"],
        response["fear"],
        response["joy"],
        response["sadness"],
        response["dominant_emotion"]
    )


@app.route("/emotionDetector")
def emotion_detector_route():
    return analyze_emotion()


@app.route("/sentimentAnalyzer")
def sentiment_analyzer_compatibility_route():
    return analyze_emotion()


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)