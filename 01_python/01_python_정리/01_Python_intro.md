# 01_Python_intro

- 정식명칭에 대한 단어에 대한 개념을 정확하게 알아라



![container](C:\Users\Ryung\TIL\images\container.png)



## 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

- 식별자의 이름은 영문 알파벳, _, 숫자로 구성된다

- 첫글자에 숫자가 올 수 없다 ex) 12day 못씀

- 대문자를 구별한다

- 아래의 예약어는 쓸 수 없다

  ```python
  # 예약어 리스트 부르는 방법
  import keyword
  print(keword.kwlist)
  ```

  ~~~python
  None, False, True, and, or, not as, raise, assert, break, class, continue, def, del, if, elif, else, try, except, finally, for, while, pass, return, yield, global, nonlocal, from, import, in, is, lambda, with
  ~~~

- 내장함수나 모듈 등의 이름으로도 만들면 안된다.

  - 내장 함수나 모듈등을 식별자로 정하면 원래 함수가 호출되지 않는다

    

## 기초문법

### 인코딩 선언

- 인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어있다

- 만약, 인코딩 설정하려면 코드 상단에 아래와 같이 선언한다

  ``` python
  # -*- coding: utf-8 -*-
  ```

- 주석으로 보이지만, python parser에 의해 읽혀진다



### 주석(Comment)

- ★ 주석은 `#` 

- ★ `docstring`은 `"""`

  ```python
  def ss3(a, b):
  """ 행복한 ssafy 3반 """
  	return a + b
  
  ss3(1, 2) # 답 : 3
  print(ss3.__doc__) # 답 : 행복한 ssafy 3반
  ```




### 코드라인

- 기본적으로 파이썬에서는 ; 을 작성하지 않는다

- 한줄로 표기하고 싶을 때 ; 을 작성하여 표기할 수 있다.

  ```python
  print('ss3')
  print('ss3')
  
  print('ss3') ; print('ss3')
  ```

  

- 줄을 여러줄 작성할 때는 역슬래시 `\`를 사용하여 표기할 수 있다.

  ```python
  a = 'long word'
  if a \ 
  == 'long word':
      print(a)
  ```

- 단 `[], {}, ()`은 역슬래시 `\` 없이도 여러 줄로 표기할 수 있다.

  ```
  ['a'
  'b'
  'c']
  ```

  

## 변수(variable) 및 자료형

- dust = 60 이면 dust에 60을 저장한다

- 변수는 `=`을 통해 할당(assignment)된다

- 해당 자료형을 확인하기 위해서는 `type()`

- 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`

  - `id()`를 찍어보는 것만틈 정확한 것은 없다

    

- 이제 본질을 깨닫자!

- `int` 와 `string`은 진짜 박스에 담는 거였지만

- `[], {}, ()` list, set, dictionary, tuple 은 위치를 가져오는 것이다

  - ''소화기는 문에서 가장 오른쪽에 있어요'' 라는 위치를 담고 있는 것이지 소화기를 진짜 담아서 들고 다니는 것이 아니다.

  - 05_data_structure 에 자세하게 나옴
  - copy, deep_copy 확인해보기

- 같은 값을 동시에 할당 가능

  ```python
  a = b = 100
  print(a) # 100
  print(b) # 100
  ```

- 다른 값을 동시에 할당 가능

  ``` python
  a = 1
  b = 2
  
  a = tmp
  a = b
  b = tmp
  
  print(a) # 2
  print(b) # 1
  
  x , y = 1, 2
  x , y = y , x
  
  print(x) # 2
  print(y) # 1
  ```

- ★ 이건 안돼요 (쪽수 안 맞으면 불가능)

  ``` python
  x, y = 1
  x, y = 1, 2, 3
  ```



### ★모눈종이 = 메모리/램★

- 메모리라고 하는 큰 모눈종이 위에 정수, 리스트, 딕셔너리 등등 모~든~ 데이터가 있다
- 컴퓨터의 머리가 얼마나 좋은지는 cpu로 판단
- 컴퓨터가 얼만큼 많은 일을 벌려 놓을 수 있느냐는 메모리로 판단

![수의개념](C:\Users\Ryung\TIL\images\수의개념.PNG)

### 수치형(Numbers)

`int`(정수)

- 모든 정수는 `int`로 표현한다

- ★ 정수 자료형에 오버플로우가 없다

  - system의 가장 큰 수를 가져와서 곱해도 그 수를 print 해주기 때문에 파이썬은 모든 정수를 담을 수 있다.

  ```python
  import sys
  max_int = sys.maxsize
  print(max_int) # 9223372036854775807
  max_int = sys.maxsize * sys.maxsize
  print(max_int) # 85070591730234615847396907784232501249
  ```

- ★ n 진수 표기법 (2, 8, 10, 16)

  ```python
  # 10진수를 n진수로 표현하는 함수
  bin(10진수) # 2진수로 표현
  oct(10진수) # 8진수로 표현
  hex(10진수) # 16진수로 표현
  
  # n진수를 10진수로 표현하는 함수
  int('2진수', 2) #10진수로 표현
  print(0b100) #10진수로 표현
  int('8진수', 8) #10진수로 표현
  print(0o777) #10진수로 표현
  int('16진수', 16) #10진수로 표현
  print(0xfff) #10진수로 표현
  ```

  ```python
  binary_number = 0b100 # 4
  octal_number = 0o777 # 511
  decimal_number = 2019 # 2019
  hexadecimal_number = 0xfff # 9 다음 숫자는 알파벳으로 표기 4095
  ```



### `float`(부동소수점, 실수)

- 실수는 float로 표현된다

- 다만 실수를 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않아서 오류가 발생한다 (floating point rounding error)

- ★ error 나는 상황을 기억해라

  ```python
  3.5 - 3.12 == 0.38 # Flase
  #3.5 - 3.12 는 0.3799999999999999 로 표현되기 때문
  round(3.5 - 3.12 , 2) == == 0.38 # True
  
  0.1 * 3 == 0.3 # Flase
  # 0.1 * 3 이 0.30000000000000004 로 표현되기 때문
  round(0.1 * 3, 2) == 0.3 # True
  ```

- ★ 3가지 방법으로 처리할 수 있다

  ```python
  # 1. 절대값 비교
  a = 0.1 * 3
  b = 0.3
  
  abs(a-b) <= 1e-10 # abs는 절대값함수, 1e-10 = 0.0000000001 # True
  
  # 2. 절대값 비교를 내장된 float epsilon값과 비교
  import sys
  sys.float_info.epsilon
  abs(a-b) <= sys.float_info.epsilon # True
  
  # 3. math 모듈을 통해 근사한 값인지 비교
  import math
  math.isclose(a, b) # True
  ```



 ### `complex`(복소수)

- 복소수는 허수부를 j로 표현한다
- 제곱했을 때 음수가 나오는 수 복소수 (실수부 + 허수부)
- 1j  *  1j = -1 + 0j

```python
★
a = 3 + 4j
type(a) # complex
print(a.imag) # 허수 # ()가 없는데도 값이 나오는 이유는 class complex의 인스턴스라서
print(a.real) # 실수
print(a.conjugate()) # 켤레 복소수
print(a.conjugate() * a)
```



### Bool

- 파이썬에는 `True` 와 `False`로 이루어진 `Bool`타입이 있다

  ```python
  type(True) # Bool
  type(False) # Bool
  ```

- 비교/ 논리 연산 수행 등에서 활용된다

- ★ 무조건 `False`로 변환되는 7가지 기억하기

  ``` python
  0, 0.0 None, [], {}, (), ''
  ```



### None

- 파이썬에서는 값이 없음을 표현하기 위해 	`None`타입이 존재한다

- `None`는 진짜 아무것도 없는 공허한 상태를 뜻한다

- 따라서 `return` 문이 없는 함수에서 `None`이 나온다.

  ```
  type(None) # NoneType
  ```



### 문자형(String)

- 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.

- 하지만 **하나의 문장부호를 선택**하여 유지하도록 한다.

- ★ 다만 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 이스케이프 문자인 백슬래시(`\`)를 사용하는 것 대신 활용 가능 합니다.

  ```python
  print('스티브잡스가 말하길, \'Real Artist Ship\'') # \ 사용 
  ```

- 여러 줄에 걸쳐있는 문장의 경우 `PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용

  - 이 아이가 주석의 역할과 스트링 역할을 다 한다.

  ``` python
  print("""
  말하는대로,
  쓰는대로,
  다 써져요!
  """)
  # 말하는대로,
  # 쓰는대로,
  # 다 써져요!
  ```



### ★  이스케이프 문자열

- 문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다

| 예약문자 | 내용(의미)   |
| -------- | ------------ |
| \n       | 줄바꿈       |
| \t       | 탭           |
| \r       | 캐리지턴     |
| \0       | 널(Null)     |
| \\\      | \            |
| ' '      | 단일인용부호 |
| " "      | 이중인용부호 |

```python
print('이 다음에 새 줄이 시작됨 \n 그리고 나온다 탭 \t 태태탭)
# 이 다음에 새 줄이 시작됨!
# 그리고 나온다 탭 	 태태태탭
```

- print 문 마지막의 기본값은 enter이다.

  ```python
  print('뒤에 문자열과 떨어지기 싫어', end='\t')
  print('앞에 문자열과 너무 가깝기 싫어')
  # 뒤에 문자열과 떨어지기 싫어	나는 앞에 문자열과 너무 가깝기 싫어
  
  print('아 배고파', end='!!!\n')
  # 아 배고파!!!
  ```



### String interpolation

- 3가지 문법이 존재

- 1. %-formatting : 진짜 옛날꺼
  2. str.format() : 알고는 있기
  3. f-strings : 많이 씀, 파이썬 3.6 버전 이후로 지원되는 사항

  ```python
  name = 'Gwak'
  year = 2019
  
  # 1 'Hello Gwak'
  'Hello %s' %name
  
  # 2 'Hello Gwak, It is 2019'
  'Hello {}, It is {}'.format(name, year)
  
  # 3 'Hello Gwak, It is 2019'
  f'Hello {name}, It is {year}'
  ```

- f-strint은 형식을 지정할 수 있으며 연산도 가능하다.

  ```python
  # 형식 지정
  import datetime
  today = datetime.datetime.now()
  print(today)
  # '오늘은 2019년 01월 16일 Wednesday'
  f'오늘은 {today:%Y}년 {today:%m}월 {today:%d}일 {today:%A}'
  
  # 연산도 가능
  pi = 3.1415926535
  r = 2
  f'원주율은 {pi:0.3} 반지름 {r}인 원의 넓이는 {(r **2 * pi):0.2}'
  # {pi:0.3}은 0은 출력되는 숫자의 칸수를 뜻하고 3은 입력된 값을 3자리까지 읽고 뒤에서 반올림 해라 라는 뜻
  # {pi:0.3f}은 0은 출력되는 숫자의 칸수를 뜻하고 3f은 소수점만 3자리 읽고 뒤에서 반올림 해라 라는 뜻
  ```



## 연산자 (산술, 비교, 논리, 복합, 기타)



### 산술연산자 7개

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| *      | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| **     | 거듭제곱       |

-  divmod(a, b) : a를 b로 나눈 몫과 나머지를 내주는 함수

  ```python
  음수도 표현 가능
  positive_num = 4
  print(-positive_num) # -4
  print(--positive_num) # 4
  ```

  

### 비교 연산자 6개

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |

```python
3.0 == 3 #True
type(3.0) == type(3) # False
```



### 논리연산자 3개

| 연산자  | 내용                                                   |
| ------- | ------------------------------------------------------ |
| a and b | a 와 b 모두 True 시에만 True (하나라도 False면 False)  |
| a  or b | a 와 b 모두 False 시에만 False (하나라도 True 면 True) |
| not a   | True → False,  False → True                            |

- 파이썬에서 and는 a값이 거짓이면 a를 리턴하고, 참이면 b를 리턴한다
- 파이썬에서 or은 a값이 참이면 a를 리턴하고 , 거짓이면 b를 리턴한다

```python
# and는 틀린게 나오는 순간 값 도출
print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 5) # 0

# or 은 맞는게 나오는 순간 값 도출
print(3 or 5) # 3
print(0 or 3) # 3
print(3 or 5) # 3
```



### 복합연산자 7개

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -=b   | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |



### 기타연산자 5개

| 연산자          | 내용                                                         |
| --------------- | ------------------------------------------------------------ |
| Concatemation   | 숫자가 아닌 str, list, tuple 자료형은 `+`연산자를 통해 합칠 수 있다 (dict, set ,range제외)<br />★ `+`가 왜 기타 연산자에 있는지 알기 |
| Containmet Test | `in` 연산자를 통해 속해있는지 여부를 확인 할 수 있다 (모든 자료형 가능) |
| Identity        | `is` 연산자를 통해 동일한 object인지 확인할 수 있다.<br />- int, string 만 비교 가능<br />- tuple, dict, set, list, range는 내용이 같더라도 다른 위치에 저장되기 때문에 id값이 달라서 항상 False |
| Indexing        | `[]`를 통한 값 접근이 가능하다<br />- string, tuple, list, range 가능<br />- set 불가능 <br />- dict는 key 값 입력 하면 value 값 나옴 |
| Slicing         | `[ : ]`를 통해 슬라이싱이 가능하다                           |

- Identity

  ```python
  # 파이썬에서 256 까지는 id 값을 저장하고 있어서 is 했을 때 True가 나오지만 그 이상은 False이다
  a = 10
  b = 10
  print(a == b) # True
  print(type(a) ==  type(b)) # True
  print(id(a) == id(b)) # True
  print(a is b) # True
  
  a = 1004
  b = 1004
  print(a == b) # True
  print(type(a) ==  type(b)) # True
  print(id(a) == id(b)) # False
  print(a is b) # False
  ```

- indexing

  ```python
  # string, tuple, list, range 가능
  print('apple'[4]) # e
  print((1, 2, 3)[2]) # 3
  print(['a', 'b', 'c'][0]) # a
  print(range(1, 10)[2]) # 3
  # set은 순서 개념이 없기 때문에 인덱스 값 호출 안 됨!
  print({1, 2, 3}[1]) 
  
  # dict은 []안에 key 값만 넣을 수 있고 value 값이 호출된다
  print({'1': 'a', '2': 'b'}['1']) # a
  ```

- slicing

  ```
  흐어어어헝
  ```



### 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +,-(음수/양수부호)
6. 산술연산자 *, / ,%
7. 산술 연산사 +, -
8. not
9. and
10. or



### 기초 형변환 2가지

### 암시적 형변환 2개 밖에 없음

- True == 1로 False == 0으로

  ```python
  True + 2 # 3
  False + 2 # 2
  ```

- Numbers(float > complex > int)

  ```python
  int_number = 3
  float_number = 5.5
  complex_number = 3 + 5j
  print(int_number + float_number) # 8.5
  print(float_number + complex_number) # 8.5+5j
  print(int_number + complex_number) # 6+5j
  ```

### 명시적 형변환

- 위의 두 가지 상황을 제외하고는 모두 명시적으로 형변환을 해주어야 한다.
- int → str : 모두 가능
- str → int : str이 소수점 없는 숫자로 이루져있을 때만
- int() : str(**소수점 없는숫자로만** 이루져있을 때), float(모두) 가능
- float() : str(숫자로만 이루져 있을 때), int(모두) 가능
- str() :  int, float, list, tuple, set, dictionary를 문자열로 변환



## ★ 시퀀스(sequence) 자료형 자세히보기 ★ ordered

- 시퀀스는 데이터의 순서대로 나열된 형식을 나타낸다. 인덱스 값을 뽑아 낼 수 있다

- 졍렬 되었다는 뜻은 아니다

- 1. 리스트 [list]

  2. 튜플 (tuple)

  3. 레인지 range() 

  4. 문자열 'string' : 모눈종이라는 메모리/램 위에 한글자씩 입력되어 있음

     ​			이것이 인덱스 값 도출, 슬라이싱이 가능한 이유이다.

  5. 바이너리(binary) : 따로 다루지 않음

     

### 리스트[list]

- 수정 가능(mmutable)
- 인덱스 값으로 호출 가능

```python
my_list= [] # 빈 리스트 생성 가능

locations = ['서울', '대전', '구미','광주']
print(locations) # ['서울', '대전', '구미','광주']

# list[인덱스값] 으로 접근 가능
print(locations[0]) # 서울
```



### 튜플(tuple)

- 수정이 불가능(immutable) 
- 추가나 수정은 불가능하고 덮어쓰기만 가능
- 직접 사용하는 것 보다 파이썬 내부에서 사용한다

```python
# swap 하는 경우 사용
a = 5
b = 11
a , b = b, a
print(a, b) # 11, 5
```



### 레인지 range()

- 기본형 `range(n)` : 0 ~ n-1까지

- 범위 지정 `range(n, m)` : n ~ m-1까지

- 범위 및 스텝 지정 `range(n, m, s)` : n ~ m-1 까지 +s만큼 증가

- [list]와 {set} 에 담을 수 있다.

  ```python
  print(list(range(1, 5))) # [1, 2, 3, 4]
  print(list(range(-3, 3))) # [-3, -2, -1, 0, 1, 2]
  print(list(range(-5, -10))) # []
  print(list(range(5, 1, -1))) # [5, 4, 3, 2, 1]
  
  # 특정 
  범위 안에서 배수 숫자 찾기 가능
  print(set(range(0, 20, 5))) # {0, 5, 10, 15}
  ```

### ★ 시퀀스에서 활용할 수 있는 연산자/ 함수 외우기!

| operation  | 설명                          |
| ---------- | ----------------------------- |
| x in s     | x가 s 안에 있니?              |
| x not in s | x가 s 안에 없니?              |
| s1 + s2    | s1과 s2 합쳐줘                |
| s * n      | s를 n번 반복해서 더해줘       |
| s[i]       | s의 i 번째 인덱스 값을 보여줘 |
| s[i:j]     | slicing                       |
| s[i:j:k]   | k 간격으로 slicing            |
| len(s)     | s 의 길이값                   |
| min(s)     | s의 최솟값                    |
| max(s)     | s의 최댓값                    |
| s.count(x) | s 안의 x의 갯수               |



## ★ set, dictionary 자세히 보기★ Unordered

- set, dictionary는 기본적으로 순서가 없다.

### `set` {}

- 수학에서의 집합과 동일하게 처리

- 순서가 없고, 중복된 값이 없다

  | 연산자/함수       | 설명   |
  | ----------------- | ------ |
  | a - b             | 차집합 |
  | a \| b            | 합집합 |
  | a & b             | 교집합 |
  | a.union(b)        | 교집합 |
  | a.intersection(b) | 교집합 |

- set을 활용하면 list의 중복 값을 손쉽게 제거할 수 있다

### `dictionary` { 'key1' : 'value1', 'key2' : 'vlaue2' }

- key는 immutable한 모든 것이 가능한다. (int, bool, string, range, tuple, float)

- 중복된 key 값은 존재할 수 없다

- value는 list, dictionary를 표함한 모든 것이 가능하다.

- 딕셔너리 메소드를 활용하여 key, value를 확인해 볼 수 있다.

  ```python
  ss3 = {'leader': '황은석', 'CA': '강진우' }
  ss3 = ['leader'] # '황은석'
  ss3.keys() # ['leader','CA']
  ss3.value() # ['황은석', '강진우']
  ss3.itenms() # [('leader', '황은석'), ('CA', '강진우')]
  ```

  





