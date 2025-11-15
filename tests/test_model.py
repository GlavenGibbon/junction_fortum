from src.models.predict import predict


def test_predict_placeholder():
    model = {'model': 'placeholder'}
    # Should return list of zeros for placeholder
    preds = predict(model, [])
    assert isinstance(preds, list)
