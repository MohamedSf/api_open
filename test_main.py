
from fastapi.testclient import TestClient
from fastapi import status
import requests
from main import app

url = 'http://127.0.0.1:8000/'

client = TestClient(app=app)

def test_index_returns_correct():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
                                "message": "Hello, World"
                                }
    

# def test_return_prediction():
#     response = client.get('/predict', params = {"id_client":100001})
#     assert response.status_code == status.HTTP_200_OK
#     assert sorted(list(response.json().keys())) == ['prediction', 'proba']

# def test_predict():
#     params = {'id_client': 100001}
#     url_predict = 'http://127.0.0.1:8000/predict' 
#     response = requests.get(url = url_predict, params = params)
#     assert response.status_code == status.HTTP_200_OK
#     assert sorted(list(response.json().keys())) == ['prediction', 'proba']
    
