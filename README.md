# Blog-Generator-System-Using-Google-Gemini

This solution utilizes the Gemini API, Langchain and Wikipedia to automatically generate a blog post based
on a given topic.

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

## Installation and Usage:

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
