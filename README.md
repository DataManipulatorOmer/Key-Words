# NLP Text Analysis API

## Overview
This repository contains the code for a Flask API that leverages Natural Language Processing (NLP) techniques to extract key insights from text. The API allows users to input text data and receive the most important keywords present in the text.

## Features
- Tokenization of input text
- Removal of stopwords and punctuation
- Calculation of word frequency
- Extraction of top keywords
- RESTful API endpoints for easy integration

## Usage
To use the API, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Send a POST request to the `/extract_keywords` endpoint with JSON data containing the text you want to analyze.
5. Receive a JSON response containing the extracted keywords.

## Example
```python
import requests

url = 'http://localhost:5000/extract_keywords'
text = "Natural language processing (NLP) is a field of artificial intelligence concerned with the interaction between computers and humans in natural language. It enables computers to understand, interpret, and generate human language in a valuable way."

response = requests.post(url, json={'text': text})
print(response.json())
