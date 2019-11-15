# 04_recursive_function

## 재귀함수 (recursive function)

- 재귀 함수는 함수 내부에서 자기 자신을 호출하는 함수를 뜻한다.

- 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 된다.

- 재귀함수는 작성시에는 반드시, basecase가 존재해야 한다

- 멈추는 곳이 존재해야 한다.

- 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용한다

- 코드가 직관적이고 이해하기는 쉽지만 직접 만들기는 어렵다

- python tutor를 보면 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다

- 이 경우 메모리 스택이 넘치거나 프로그램 실행속도가 느려지는 단점이 생긴다

- 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더 이상 함수를 호출하지 않고 종료한다.

  

## 팩토리얼 → 치킨쿠폰 → 피보나치 → up & down  → 스퀘어 루트 순으로 이해하기



#### 실습문제 - 팩토리얼 계산

> 팩토리얼(factorial)을 계산한느 함수 fact(n)를 작성해봅시다
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산하는 값을 반환합니다

예시 출력) 120

```python
# 그냥 함수
def fact(n):
    result = 1
    while n > 1:
        result = result * n 
        n -= 1
    return result

# 재귀함수 이용하기
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
```



#### 실습문제 - 피보나치 수열

> 피보나치 수열은 다음과 같은 점화식이 있다
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해보자

1) fib(n) : 재귀함수

2) fib_loop(n): 반복문을 활용한 함수

예시 입력)

fib(10)

예시 호출)

89

````python
# 재귀함수 이용하기
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n - 1) + fib(n - 2)
    
# 반복문 이용하기
def fib_loop(n):
    result = [1, 1]
    for i in range(1, i):
        result.append(result[-1] + result[-2])
    return result

fib_loop(5)[-1]
    
        
````



#### 실습문제 - chicken coupon

>ex) 치킨쿠폰 3장을 모으면 한마리를 줍니다. 한마리를 시키면 한장을 줍니다. n장이 있을 때, 몇 마리까지 먹을 수 있을까요? ex) 10장 => 7장 + 1장 => 5 + 1 => 3 + 1 => 1 + 1

```python
def free_chicken(coupon, n = 3, chicken = 0):
    if coupon < n:
        return chicken
    else:
        coupon -= 3
        chicken += 1
        coupon += 1
        return free_chicken(coupon, n, chicken)
      
        
    

```



#### 실습문제 - up&down

> 우리가 `range(1, 101)` 중 하나를 생각한다. 컴퓨터가 절반에 위치한 숫자를 물어보고, 그 숫자가 생각한 수보다 크면1 , 작으면 -1, 맞으면 0을 입력한다. 이때 몇번 만에 컴퓨터가 맞췄는지 출력하고 프로그램을 끝낸다.

예시)

50

→ -1

25

→ -1

13

→ -1

7

→ 1

10

→ 1

12 

→ 0

6번 만에 맞췄습니다!

```python
def updown(n):
    print('1~100사이 숫자를 생각하세요')
    max_num = 101
    min_num = 0
    count = 0
    while max_num and min_num != n:
        print((max_num + min_num) // 2)
        feedback = int(input('제시된 숫자가 생각한 숫자보다 작으면 -1 크면 1 맞으면 0을 입력하세요'))
    	if feedback == -1:
            max_num = (max_num + min_num) // 2
        elif feedback == 1:
            min_num = (max_num + min_num) // 2
        elif feedback == 0:
            count += 1
            break
        count += 1
        
    return f'{count} 번 만에 맞춤!'
        
updown(25)   
```



