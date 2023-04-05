import sentimentanalysis


def test_positive_sentence():
    text = "I love this product!"
    expected_output = '{"text": "I love this product!", "sentiment": "Positive", "value": 0.692}'
    assert sentimentanalysis.analyze_sentence(text) == expected_output


def test_negative_sentence():
    text = "This product is terrible!"
    expected_output = '{"text": "This product is terrible!", "sentiment": "Negative", "value": 0.531}'
    assert sentimentanalysis.analyze_sentence(text) == expected_output


def test_neutral_sentence():
    text = "This product is okay."
    expected_output = '{"text": "This product is okay.", "sentiment": "Neutral", "value": 0.612}'
    assert sentimentanalysis.analyze_sentence(text) == expected_output
