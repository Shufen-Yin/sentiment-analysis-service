import requests

def test_predict():
    url = "http://localhost:5000/predict"
    text = input("Enterext to analyze: ")
    try:
        response = requests.post(url, json={"text": text})
        print(f"sentiment analyiss result: {response.json()}")
    except Exception as e:
        print(f"fail connection: {e}")

if __name__ == "__main__":
    test_predict()