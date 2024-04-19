from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation

app = Flask(__name__)

def digKeywords(text, wordsToBeKeyedd=5):
    # Tokenize 
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stopWords = set(stopwords.words('english') + list(punctuation))
    filteredWords = [word for word in words if word not in stopWords]

    # Word frequency
    frequencyDistribution = FreqDist(filteredWords)

    # Top keywords
    keywords = frequencyDistribution.most_common(wordsToBeKeyedd)

    return [word for word, _ in keywords]

@app.route('/digKeywords', methods=['POST'])
def fetchKeywords():
    data = request.get_json()
    text = data['text']
    keywords = digKeywords(text)
    return jsonify({"keywords": keywords})

if __name__ == '__main__':
    app.run(debug=True)
