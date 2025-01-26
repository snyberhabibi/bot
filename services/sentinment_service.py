import openai

class SentimentAnalyzer:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def analyze_sentiment(self, texts):
        scores = []
        for text in texts:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Rate the sentiment of this text (-1 to 1): {text}",
                max_tokens=1
            )
            scores.append(float(response["choices"][0]["text"].strip()))
        return sum(scores) / len(scores)  # Average sentiment
