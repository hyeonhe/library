from datetime import datetime

# 현재 날짜를 가져옵니다.
current_date = datetime.now()

# 사용자로부터 생년월일을 입력받습니다.
birth_date = input("생년월일을 YYYY-MM-DD 형식으로 입력하세요: ")

# 입력된 생년월일을 날짜 형식으로 변환합니다.
try:
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
except ValueError:
    print("올바른 날짜 형식이 아닙니다. YYYY-MM-DD 형식으로 입력하세요.")
    exit()

# 현재 날짜와 생년월일을 비교하여 나이를 계산합니다.
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

# 결과를 출력합니다.
print(f"당신의 만 나이는 {age}세 입니다.")
