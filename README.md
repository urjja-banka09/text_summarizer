# text_summarizer
1. Set Up Your Project
Create a directory for your project and set up a virtual environment. Install Flask and other required dependencies by creating a requirements.txt file.
Flask==2.0.1
nltk==3.6.5
gensim==4.2.2

Run the following commands in your terminal:
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
pip install -r requirements.txt
2. Folder Structure
Organize your project with a structure like the following:
/text_summarizer
  /templates
    index.html
  app.py
  requirements.txt
Run the Flask app with the following command:
python app.py
Visit http://127.0.0.1:5000/ in your web browser to interact with the summarization app.


