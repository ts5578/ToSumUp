from flask import Flask, request, jsonify
from email_summarizer import EmailSummarizer



app = Flask(__name__)
summarizer = EmailSummarizer()

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    content = data.get("content", "")
    
    # Check if content is non-empty
    if not content:
        return jsonify({"error": "Content is missing or too short"}), 400

    try:
        summary = summarizer.summarize_email(content)
        return jsonify({"summary": summary})
    except Exception as e:
        # Log the exception message for debugging
        print(f"Error during summarization: {e}")  # Log the error
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
