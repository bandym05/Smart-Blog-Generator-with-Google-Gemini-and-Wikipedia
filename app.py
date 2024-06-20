from flask import Flask, render_template, request
from langchain_community.document_loaders import WikipediaLoader
from google.colab import userdata
import google.generativeai as genai

app = Flask(__name__)
api_key = userdata.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['title']
    
    # Research the topic using Wikipedia
    wiki_loader = WikipediaLoader(query=topic, load_max_docs=1)
    wiki_summary = wiki_loader.load()[0].page_content[:200]  # Truncate summary

    # Generating blog sections using the Gemini API
    heading = model.generate_content(
        "Generate a clear and concise heading for a blog about " + topic
    ).text.strip()

    introduction = model.generate_content(
        "Write an engaging introduction to a blog about " + topic
    ).text.strip()

    content = model.generate_content(
        "Create detailed and informative content for a blog about "
        + topic + ". Include relevant facts and figures, and cite sources where necessary. Summarize the key points from the provided Wikipedia summary: "
        + wiki_summary
    ).text.strip()

    summary = model.generate_content(
        "Summarize the main points covered in the blog about " + topic
    ).text.strip()

    return render_template('blog.html', heading=heading, introduction=introduction, content=content, summary=summary)

if __name__ == '__main__':
    app.run()
