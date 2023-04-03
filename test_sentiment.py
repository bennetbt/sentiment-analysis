import unittest
from sentiment-analysis import analyze_sentence

class TestSentimentAnalyzer(unittest.TestCase):

    def test_positive_sentence(self):
        text = "I love this product!"
        result = analyze_sentence(text)
        expected_output = '{"text": "I love this product!", "sentiment": "Positive", "value": 0.781}'
        self.assertEqual(result, expected_output)

    def test_negative_sentence(self):
        text = "This product is terrible!"
        result = analyze_sentence(text)
        expected_output = '{"text": "This product is terrible!", "sentiment": "Negative", "value": 0.595}'
        self.assertEqual(result, expected_output)

    def test_neutral_sentence(self):
        text = "This product is okay."
        result = analyze_sentence(text)
        expected_output = '{"text": "This product is okay.", "sentiment": "Neutral", "value": 0.475}'
        self.assertEqual(result, expected_output)