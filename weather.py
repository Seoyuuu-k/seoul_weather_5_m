import requests                       # url: get요청
import csv                            # csv로 저장
import os                             # 폴더 생성
from datetime import datetime         # 시간 변환

WEATHER_API_KEY= os.getenv("WEATHER_API_KEY") # 키는 무조건 지워줘야함
city_name = "Seoul"
url =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
response = requests.get(url)
result = response.json()
result
# 깃허브에 배포


# 현재 기온
temp = result["main"]["temp"]
# 습도
humidity = result["main"]["humidity"]
# 날씨 상태
weather = result["weather"][0]["main"]
# 현재 시각
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#CSV
# 헤더생성
header = ["current_time","weather","temp","humidity"]

# 만약 , seoul_weather.csv 없으면 만들고, 있으면 덮어쓰기
# csv 생성 -> 헤더추가 -> 데이터 값

csv_exist = os.path.exists("seoul_weather.csv")

# mode / w:wirte, r:read, wb:write byte, a:write(있다면 덮어쓰기)
with open("seoul_weather.csv", "a") as file:
    writer = csv.writer(file)

    # CSV 한번도 안 만들어 졌다면, 헤더 추가!
    if not csv_exist:
        writer.writerow(header)

    writer.writerow([current_time, weather, temp, humidity])
    print("서울 기온 저장 완료")
    
                      
