def sumfunc(n):
    return sum(range(1, n + 1))


number = int(input("1 이상의 정수를 입력하시오: "))
if number > 1:
    result = sumfunc(number)
    print(f"1부터 {number}까지의 합은 {result}입니다.")
    
else:
    
    print("1 이상의 정수를 입력해야 합니다.")