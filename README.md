# Smart Blog Generator with Google Gemini and Wikipedia

![growtika-nGoCBxiaRO0-unsplash](https://github.com/bandym05/Smart-Blog-Generator-with-Google-Gemini-and-Wikipedia/assets/58115126/75614be4-ea99-42de-b185-5e2d1a11345e)

Photo by <a href="https://unsplash.com/@growtika?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Growtika</a> on <a href="https://unsplash.com/photos/an-abstract-image-of-a-sphere-with-dots-and-lines-nGoCBxiaRO0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

This solution utilizes the Gemini API and Wikipedia to automatically generate a blog post based
on a given topic.

Several processes are automatically initiated as you type your blog title in the Blog Generator Input Field, to get the full blog post out. To begin with, the scripting system employs the LangChain to search on Wikipedia and pull out a brief description or summary of the topic. It also assists in doing a summary which will give a basic understanding of a blog and its essential issues.

Then, specific Google Generative AI models are used to create various segments of the blog post. The generative model is initiated and employed as a basis for the generation of simple and more comprehensive heading related with the blog topic. After it, a catchy heading to come up with an interesting introduction that would surely hook the readers and the tone to the blog is set.

The generative model also searches for detailed and much information to post on the blog. This content entails factual information, statistics/quantitative information, and related information sourced from reliable literature and within the given topic. Please make sure that all created blog posts are informative and cover a wide range of topics.
The last step is to use the generative model to learn how to sum up in the knowledge of the points that the blog has highlighted. This conclusion gives a brief idea of the most essential points that can be found in the blog.

Once all the sections are generated, these are the heading, introduction, content and summary which are contained within a dictionary. Hence, you can then easily mobilize these sections whenever needed, for instance to print to the console or as part of a blog post template, depending on the specific context. This process enables you to come up with a blog post within the shortest time possible and be assured that it provides informative content on the topic that you have settled on.

![Blogger](https://github.com/bandym05/Smart-Blog-Generator-with-Google-Gemini-and-Wikipedia/assets/58115126/d03bd5b8-b2cb-4730-b66d-678f1cbf7f92)


## Functionality:
- Generates a clear and concise heading, engaging introduction, detailed content, and
comprehensive summary for a blog post.
- Leverages Wikipedia summaries to provide factual information and citations.

## Challenges and Improvements:
- **Limited factual depth:** While the code leverages Wikipedia, it can be further enhanced by
incorporating additional fact-checking mechanisms or integrating with other knowledge
sources.
- **Style and tone control:** Currently, the generated content reflects the Gemini model's
general writing style. Customization options for tailoring the tone and style to specific
requirements could be beneficial.

## Flask Application Installation and Usage:

### Prerequisites

1. **Python 3.7+**
2. **Pip (Python package installer)**
3. **Git**

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

### Set Up Virtual Environment

It's a good practice to use a virtual environment to manage your dependencies.

#### On Unix-based systems (Linux, macOS)

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### Get Your Own Gemini API Key

1. **Sign up for access to the Google Gemini API**: Visit the [Google Gemini API website](https://ai.google.dev/aistudio) and sign up for an API key.
2. **Copy the API key**: Once you have signed up, you will receive an API key.

### Set Up Environment Variables

You need to set your Gemini API key as an environment variable. This can be done in a few different ways:

#### Method 1: Using the Command Line (Temporary)

This method sets the environment variable for the duration of the terminal session.

##### On Unix-based systems (Linux, macOS)

```bash
export GEMINI_API_KEY=your_actual_api_key
python app.py
```

##### On Windows

```cmd
set GEMINI_API_KEY=your_actual_api_key
python app.py
```

#### Method 2: Using a `.env` File (Recommended for Local Development)

1. **Install `python-dotenv`** (if not already installed):

   ```bash
   pip install python-dotenv
   ```

2. **Create a `.env` file** in the root of your project and add your API key:

   ```
   GEMINI_API_KEY=your_actual_api_key
   ```

3. **Modify your `app.py` to load the `.env` file**:

   ```python
   from flask import Flask, render_template, request
   from langchain_community.document_loaders import WikipediaLoader
   import google.generativeai as genai
   from dotenv import load_dotenv
   import os

   load_dotenv()  # Load environment variables from .env file

   app = Flask(__name__)

   api_key = os.getenv('GEMINI_API_KEY')
   if not api_key:
       raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

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
   ```

### Running the Application

After setting the environment variables, you can run the application using:

```bash
python app.py
```

### Accessing the Application

Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.


## Running the colab notebook

**Prerequisites:**

● A Google Colab account

**Steps:**

**1. Import the Notebook to Colab:**
- Download the notebook in this repository
- Go to https://colab.research.google.com/.
- Click "File" -> "Open notebook" -> "Upload Notebook".
- Select the .ipynb file containing this code and upload it.

**3. Generate and Save Gemini API Key:**
- Go to the Google AI Studio.
- Create a new project or select an existing one.
- In the "APIs" section, click on "Create API Key".
- Give your API key a descriptive name and click "Create".
- Copy the generated API key.

**5. Save API Key as Secret in Colab:**
- **Open the Secrets Tab:** [1] Click the key icon located on the left sidebar of your Colab notebook. This
opens the "Secrets" tab.
- **Add a New Secret:** [1] Click the "Add a new secret" button in the "Secrets" tab.
- **Enter Key Details:** [1] In the "Name" field, enter a descriptive name for your secret (e.g.,
"GEMINI_API_KEY"). [2] In the "Value" field, paste the Gemini API key you copied from the
Google AI Studio..
- **Save the Secret:** [1] Click the "Save" button.
- **This stores your API key securely within your Colab environment and prevents it
from being accidentally exposed in your code.**

**6. Run the Code:**
- Replace "Climate Change" in the example usage with your desired blog post
topic.
- Run all the code cells in the notebook.
- The generated blog post sections (heading, introduction, content, summary) will
be printed.

**Notes:**
- This code utilizes the langchain, wikipedia, and google.colab libraries. Ensure they are
installed in your Colab environment before running the code.
- Consider exploring the capabilities of the Gemini API and Wikipedia to further
customize the blog post generation process.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
