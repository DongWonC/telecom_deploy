import os
import requests

# 환경 변수에서 토큰 가져오기 (옵션)
token = os.environ.get("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")
headers = {'Authorization': f'token {token}'}

# GitHub API에 요청 보내기
response = requests.get('https://api.github.com/DongWonC', headers=headers)

# 응답 확인
print(response.status_code)
print(response.json())