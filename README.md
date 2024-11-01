# Email Summarizer

This project is a simple email summarizer that uses NLP (Natural Language Processing) techniques to condense lengthy emails into brief summaries. It is implemented as a web application with a user-friendly interface.


$${\color{red}Currently\space does\space not\space work\space with\space large\space emails.Working\space on\space it.}$$


## Features

- Summarizes emails using the BART model from Hugging Face Transformers.
- Displays the summarized text in a clear, bold, and colored format.
- Simple and intuitive user interface.

## Technologies Used

- **Python**: Backend service using Flask.
- **Transformers**: Hugging Face Transformers library for NLP.
- **HTML/CSS**: Frontend interface.
- **JavaScript**: Handles user interactions.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <https://github.com/yourusername/email-summarizer.git>
   cd email-summarizer
   
2. **Set up a virtual environment (optional but recommended):**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    
    ```
    
3. **Install the required packages:**
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4. **Run the application:**
    
    ```bash
    python app.py
    
    ```

## How to Use

1. Open the mail you want to summarize.
2. Add the extension on top right corner. 
3. Click the **"Summarize Email"** button.
4. The summarized result will be displayed below the button.


## Sample Result

![Email Summarizer Button](https://github.com/user-attachments/assets/eef1b5ba-66f2-42d1-a0ac-8a1d2586d14b)

![Summarizer Result](https://github.com/user-attachments/assets/4bf384e9-91b3-448f-a70d-f0370e33a16b)



## Customization

You can customize the summarization parameters in the `email_summarizer.py` file:

```python
def summarize_email(self, content, max_length=600, min_length=50):

```

- `max_length`: Maximum length of the summary.
- `min_length`: Minimum length of the summary.

Adjust these values based on your requirements.
## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
