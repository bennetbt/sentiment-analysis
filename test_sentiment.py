import pytest
from sentimentanalysis import analyze_sentence

def test_positive_sentence():
    text = "I love this product!"
    expected_output = '{"text": "I love this product!", "sentiment": "Positive", "value": 0.781}'
    assert analyze_sentence(text) == expected_output

def test_negative_sentence():
    text = "This product is terrible!"
    expected_output = '{"text": "This product is terrible!", "sentiment": "Negative", "value": 0.595}'
    assert analyze_sentence(text) == expected_output

def test_neutral_sentence():
    text = "This product is okay."
    expected_output = '{"text": "This product is okay.", "sentiment": "Neutral", "value": 0.475}'
    assert analyze_sentence(text) == expected_output