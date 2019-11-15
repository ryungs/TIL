# 02_Control_of_flow

## 제어문 Control of flow

- 제어문은 크게 반복문`for문` `while문` 과 조건문 `if문` 으로 나눌 수 있다.



## 조건문

- if 문 뒤에 오는 것이 Ture 냐 False 냐를 묻는 것이다
- `if`문은 반드시 참/ 거짓을 판단할 수 있는 `조건식`과 함께 사용이 되어야 한다.

- `조건식`이 `True`인 경우 `:` 이후의 문장을 수행한다

- `조선식`이 `False`인 경우 `else:` 이후의 문장을 수행한다

  

#### 실습문제 1

> 조건문을 통해 변수 num 값과 홀수/짝수 여부를 출력하세요.

예시 출력)

3

홀수입니다.

``` python
num = int(input('값을 입력하세요:'))
print(num)
if num % 2 == 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')
```

#### 실습문제 2

> 아래의 코드의 출력 결과를 예상해보세요

~~~python
if True:
    if False:	# 진입 안함
        print(1)
        print(2)
    else:		# 진입
        print(3)
else:		# 진입 안함
    print(4)
print(5)
# 3
# 5
~~~

#### 실습문제 3

> 택시를 타려면 주머니에 4,000원 이상 혹은 카드가 있어야 한다. 이때 택시를 탈 수 있는지를 확인하는 코드를 짜보자

~~~python
ride = int(input('얼마있는지?'))
if ride >= 4000:
    print('택시를 탈 수 있습니다')

elif ride == '카드':
    print('택시를 탈 수 있습니다')

else:
    print('걸어가세요ㅜㅜ')
~~~



## 복수조건문

- 2개 이상의 조건문을 활용할 경우 `elif<조건식>:` 활용한다

#### 실습문제 1

> 조건문을 통해 변수 score에 따른 평점을 출력하세요

| 점수      | 등급 |
| --------- | ---- |
| 90점 이상 | A    |
| 80점 이상 | B    |
| 70점 이상 | C    |
| 60점 이상 | D    |
| 60점 미만 | F    |

예시 출력)

B

```python
score = int(input('점수를 입력하세요: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```



#### 실습문제2 - 중첩 조건문 활용

> 위의 실습문제 1 코드를 활용하여  95점 이상이면, "참잘했어요"를 함께 출력해주세요

예시 출력)
A
참잘했어요

```python
score = int(input('점수를 입력하세요: '))

if score >= 90:
    print('A')
    if score >= 95:
        print('참잘했어요')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```



#### 실습문제 3

> 3의 배수면, Fizz출력
>
> 5의 배수면, Buzz 출력
>
> 3, 5 의 공배수면 FizzBuzz 출력
>
> 나머지는 숫자 출력

```python
n = int(input('숫자를 입력하세요: '))
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)
```



#### 실습문제 5 환율계산

> 사용자가 띄어쓰기를 기준으로, (Volume 단위) 로 입력한다. 원화로 계산해서 print 해주자.

``` python
user_input = input('volume & unit를 입력해주세요').split()
volume = int(user_input[0])
unit = user_input[1]

def urrency_calculator_2(volume, unit):
    currency = {'USD': 1167,
    'JPY': 10.96,
    'EUR': 1168,
    'CNY': 171
    }
    unit_currency = {
        '달러': 'USD',
        '엔':'JPY',
        '유로': 'EUR',
        '위안': 'CNY'
    }
    
    symbol = unit_currency[unit]
    return round(volume * currency[symbol], 2)

print(f'{currency_calculator_2(volume, unit)}입니다')
```



## 조건표현식 = 삼항연산자

- 한줄에 if와 else가 들어 있는 것이 조건표현식이라고 한다 
- ★ elif는 못쓴다!! 기억하기

-  **ture일 때 출력값 + `if`조건식 + `else` + fasle 일때 출력값**

- print(result) 하고 싶으면

  **result = ture일 때 출력값 + `if`조건식 + `else` + fasle 일때 출력값 **



## 반복문

### `while`문

- `while`문은 조건식이 True인 경우 반복적으로 코드를 실행합니다
- 따라서 **while문은 반드시 종료조건을 설정해줘야 합니다**
- `break`로 멈출 수 있습니다
- 한 없이 반복할 수 있기 때문에 조심하기!!



### `for` 문

- `for`문은 정해진 시퀀스와 set, dictionary 내에서 순차적으로 코드를 실행합니다.
- 정해진 시퀀스와 set, dictionary 내에서 순차적으로 돌며 **가지고 있는 모든 것을 꺼내준다.**
- 따라서 종료 조건을 신경 쓰지 않아도 된다.



#### 실습문제 1

> 반복문과 조건문만 활용하여 1 ~ 30까지 숫자 중에 홀수만 담긴 리스트는 만드세요

```python
odds = []
for i in range(1, 31):
    if i % 2:
        odds += [i]
        
print(odds) 
```



#### 실습문제 2

> 반복문과 조건문만 활용하여 1~100 까지 자연수 중 5의 배수들의 총합을 구하세요

```python
# list에 쌓아서 sum 활용하는 방법
penta = []
for numbers in range(1, 101):
    if numbers % 5 == 0:
        penta += [numbers]
        
print(sum(penta))

# 변수를 정수로 잡아서 더하는 방법
penta_1 = 0
for numbers in range(1, 101):
    if numbers % 5 == 0:
        penta_1 += numbers
        
print(penta_1)
```



#### 실습문제 3 - sigma

> 정수 n 이 들어오면, 1 ~ n 까지의 합을 출력하는데(함수)

```python
n = int(input('숫자를 입력하세요: '))

def sigma(n):
    numbers = 0
    for i in range(1, n + 1):
            numbers += i
    return numbers

print(sigma(n))
```



#### 실습문제 4 - 구구단

>'for' 와 ' range' 로 구구단 출력하기

```python
n = 4
gugu = []
for i in range(1,10):
    gugu += [i * n]

print(gugu)
```



#### 실습문제 5 - 삼각형
> 입력으로 높이가 들어옵니다. 높이만큼 산 모양으로 출력하세요.(함수인데 print로 끝. no out.)

```python
h = int(input('Tree의 높이를 입력하세요(3~30)'))
for i in range (1):
    print((' ' * ((h * 2 - 1 - i) // 2 )) + '☆')
for i in range(1, h * 2, 2):
    print((' ' * ((h * 2 - 1 - i) // 2 )) + '*' * i)
```



### enumerate() 사용하여 index와 함께 `for`문 활용하기

- `enumerate()`를 활용하면 추가적인 변수를 활용할 수 있다

- `enumerate(iterable, start=0)`은 내장 함수로 (객체의 순서, 객체값)을 튜플로 보여준다

- index 접근이 가능한 애들만 쓴다

- 셋과 딕셔너리에 어거지로 쓰면 나오긴 하지만 원칙상 안 쓰는 것이 맞다

  ```python
  mates = ['친구1', '친구2', '친구3', '나']
  list(enumerate(mates)) 
  # [(0,'친구1'), (1,'친구2'), (2,'친구3'), (3, '나')]
  
  numbers = {1, 2, 3}
  list(enumerate(numbers)) 
  # [(0, 1), (1, 2), (2, 3)]
  ```

  

- start 값은 0이 기본값이고 지정할 수 있다

  ```python
  mates = ['친구1', '친구2', '친구3', '나']
  list(enumerate(mates, start = 1)) 
  # [(1,'친구1'), (2,'친구2'), (3,'친구3'), (4, '나')]
  ```

  

### dictionary 반복문 활용하기

- dictionary에 `for`문을 실행시키면 key 값이 도출된다

  ```python
  classroom = {'teacher': '교수님', 
               'leader': '친구1', 
               'mate': '친구2'
              }
  for role in classroom:
      print(role)
  # teacher
  # leader
  # mate
  
  for role in classroom:
      print(classroom[role])
  # 교수님
  # 친구1
  # 친구2
  ```



#### dictionary에서 `for`문 활용하는 방법 4가지

```python
# key 반복
for key in dict:
    print(key)
# key 반복
for key in dict.keys():
    print(key)
# value 반복
for value in dict.values():
    print(value)
# key, value 반복
for key, value in dict.items():
    print(key, value)
```



## `break`, `continue`, `else`

### `break`

- break는 만나는 즉시 반복문을 종료하는 표현
- while, for 문에 둘 다 쓸 수 있다
- 언제 써요? 더 이상 볼 필요 없을 떄!



#### 실습문제

> 조건문과 반복문, break를 통해서 아래의 코드와 동일한 코드를 작성하세요
>
> (3이 있을 경우 True를 print하고, 아닐 경우 False를 print합니다.)

numbers = [1, 5, 10]

print( 3 in numbers)

예시 출력)

False

```python
numbers = [1, 5, 10]
result = False
for i in numbers:
    if i == 3:
        result = True
        break
print(result)
```



### `continue`

- `continue`를 만나면 그 이후 코드를 무시하고 바로 다음 요소가서 반복 수행한다.

  ```python
  for i in range(6):
      if i % 2 == 0:
          continue
      print(f'{i}는 홀수입니다.')
  # 짝수는 if 문 안으로 들어가서 continue를 만나서 print문까지 갈 수가 없고
  # 홀수만 print문을 만나서 출력 된다
  # 1 는 홀수입니다.
  # 3 는 홀수입니다.
  # 5 는 홀수입니다.
  ```



### `else`

- `else` 문은 반복문을 끝까지 다 돌고 마지막 딱 1번만 실행된다.

- 반복문을 도는 중간에 break 만나면 `else`는 무시

  ```python
  for i in range(3):
      if i == 6:
          print(f'{i}에서 break 실행됨')
          break
  else:
      print('break 안걸림')
  # break 안걸림
  
  for i in range(3):
      if i == 1:
          print(f'{i}에서 break 실행됨')
          break
  else:
      print('break 안걸림')
  # 1에서 break 실행됨 
  ```