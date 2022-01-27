import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'jan_feb': 50, 'mar_may': 300, 'jun_sep': 2500, 'oct_dec': 500, 'annual_rainfall': 3000})

print(r.json())
