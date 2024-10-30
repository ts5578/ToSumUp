from transformers import pipeline

class EmailSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

    def summarize_email(self, content, max_length=1000, min_length=100):  # Increased max_length and min_length
        # Check if content length is adequate
        if len(content.split()) < 5:  # Require at least 5 words for summarization
            raise ValueError("Content too short for summarization.")

        print(f"Content for summarization: '{content}'")  # Log the content being summarized

        try:
            summary = self.summarizer(content, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error during summarization processing: {e}")  # Log any processing errors
            raise
