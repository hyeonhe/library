# 사용자로부터 두 숫자를 입력받습니다.
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 덧셈 연산을 수행하고 결과를 출력합니다.
addition = num1 + num2
print(f"덧셈 결과: {addition}")

# 뺄셈 연산을 수행하고 결과를 출력합니다.
subtraction = num1 - num2
print(f"뺄셈 결과: {subtraction}")

# 곱셈 연산을 수행하고 결과를 출력합니다.
multiplication = num1 * num2
print(f"곱셈 결과: {multiplication}")

# 나눗셈 연산을 수행하고 결과를 출력합니다.
# 나눗셈 시 두 번째 숫자가 0인 경우 예외 처리를 해야 합니다.

if num2 != 0:
    division = num1 / num2
    print(f"나눗셈 결과: {division}")
else:
    print("0으로 나눌 수 없습니다.")
