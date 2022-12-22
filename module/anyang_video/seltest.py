import requests

url='http://anyang-anyang.ktcdn.co.kr/%EA%B5%90%EC%9C%A1%EC%97%AD%EB%9F%89%EA%B0%95%ED%99%94%EC%84%BC%ED%84%B0/2022-1%ED%95%99%EA%B8%B0/2022%20%EC%A0%95%EA%B8%B0%ED%95%99%EC%8A%B5%EB%B2%95/%EC%A0%95%EA%B8%B0%ED%95%99%EC%8A%B5%EB%B2%95%ED%8A%B9%EA%B0%951%EC%B0%A8_%EC%8B%A0%EA%B3%B5%EC%9E%AC%EC%A0%841.mp4'
response = requests.get(url)
with open('video.mp4', 'wb') as f:
    f.write(response.content)