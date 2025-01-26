import openai

class SentimentAnalyzer:
    def __init__(self, openai_api_key):
        """
        Initialize the SentimentAnalyzer with an OpenAI API key.

        Args:
            openai_api_key (str): Your OpenAI API key.
        """
        if not openai_api_key:
            raise ValueError("OpenAI API key is required.")
        openai.api_key = openai_api_key

    def analyze_sentiment(self, texts):
        """
        Analyze the sentiment of a list of texts and return the average sentiment score.

        Args:
            texts (list of str): A list of text inputs for sentiment analysis.

        Returns:
            float: Average sentiment score (-1.0 to 1.0) across all texts.
        """
        if not texts:
            raise ValueError("Input texts cannot be empty.")
        
        try:
            # Combine texts into a single prompt for efficiency
            prompt = "Analyze the sentiment of each text (-1 for negative, 0 for neutral, 1 for positive):\n"
            for i, text in enumerate(texts, start=1):
                prompt += f"{i}. {text}\n"

            # Send a single API request for all texts
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=50,
                temperature=0
            )
            
            # Parse the response
            response_text = response["choices"][0]["text"].strip()
            scores = self._parse_scores(response_text, len(texts))
            return sum(scores) / len(scores)  # Return the average sentiment score

        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return 0.0  # Return neutral sentiment on error

    @staticmethod
    def _parse_scores(response_text, num_texts):
        """
        Parse sentiment scores from the API response.

        Args:
            response_text (str): The text response from the OpenAI API.
            num_texts (int): The number of texts analyzed.

        Returns:
            list of float: Sentiment scores for each text.
        """
        try:
            scores = []
            for line in response_text.split("\n"):
                if line.strip() and len(scores) < num_texts:
                    score = float(line.split(":")[-1].strip())
                    scores.append(score)
            return scores
        except ValueError:
            print("Error parsing sentiment scores. Returning neutral scores.")
            return [0.0] * num_texts  # Default to neutral sentiment if parsing fails
