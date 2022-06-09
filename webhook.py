import requests
import json

with open("2022-06-07_statistics.json", "r") as f:
    st = json.load(f)

keyword_kor = {
            "blazer": "블레이져",
            "Half-shortpants": "반바지",
            "blouse": "블라우스",
            "cardigan": "가디건",
            "coat": "코트",
            "denim": "청바지",
            "hoodi": "후드티",
            "jumper": "점퍼",
            "leggings": "레깅스",
            "mustang": "무스탕",
            "onepiece": "원피스",
            "pkshirts": "폴로티",
            "riders": "라이더자켓",
            "shirts": "셔츠",
            "skirt": "스커트",
            "slacks": "슬랙스",
            "sweater": "스웨터",
            "sweatpants": "추리닝",
            "sweatshirts": "맨투맨",
            "t-shirts": "티셔츠"
} 

data_object = ('{"type":"mrkdwn", "text": "오늘의 키워드는 :star:*%s*:star: 입니다!"}'%(keyword_kor[st["top1"][0]])).encode('utf-8')
slack_url = ""

freq_second = ('{"type":"mrkdwn", "text": "2. %s, %s"}'%(keyword_kor[st["top2"][0]], st["top2"][1])).encode('utf-8')
freq_third = ('{"type":"mrkdwn", "text": "3. %s, %s"}'%(keyword_kor[st["top3"][0]], st["top3"][1])).encode('utf-8')

output = requests.post(slack_url, data_object)
print(output)
output = requests.post(slack_url, freq_second)
print(output)
output = requests.post(slack_url, freq_third)
print(output)
