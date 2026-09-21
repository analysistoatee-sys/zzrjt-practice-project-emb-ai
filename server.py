"""Flask web application for emotion detection."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


def analyze_emotion():
    """Analyze text submitted through the web interface."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/emotionDetector")
def emotion_detector_route():
    """Return the emotion analysis result."""
    return analyze_emotion()


@app.route("/sentimentAnalyzer")
def sentiment_analyzer_compatibility_route():
    """Support the existing web interface route."""
    return analyze_emotion()


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
