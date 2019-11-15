# 03_function

- 특정 코드가 반복 된다면 함수로 만들어라!
- ★ 함수는 `print문`이 아닌 `return 문`으로 끝나야 한다
- `return` 값이 없으면 `None`를 반환한다
- 내장 함수가 있다 `dir(__bulitins__)` 으로 볼 수 있다.

```python
# 내장함수들 엄청 많음
bool(), complex(), int(), float(), type(), id()

divmod(), sum(), max(), min(), round(), len()

dict(), set(), list(), tuple(), str(), range()

print()

```

```python
# 직사각형 둘레, 면적 구하기
height = 30
width = 20

d = height * 2 + width * 2
m = height * width

print(f'직사각형 둘레: {d}, 면적: {m}입니다.')
```

```python
# 함수로 만들기
def rectangle(height, width):
    d = height * 2 + width * 2
	m = height * width
    return f'직사각형 둘레: {d}, 면적: {m}입니다.'

rectangle(30, 20)
```



## 함수의 return

- 어떠한 종류의 객체여도 상관없지만 **오직 한개의 객체만이 반환됩니다**
- 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.
- ★ return 문에는 쉼표를 못 쓴다 ex) return x, y 안 돼!!!

```python
# 두 수 중 큰 수 출력하기
def my_max(x, y):
    if x > y:
        return x
    else:
        return y
my_max(1,3)
```

- 함수는 input과 output이 있어도 없어도 된다

```python
def yes_in_yes_out(x):
    return x

def yes_in_no_out(x):
    print(x)
    
def no_in_yes_out(x):
    return x

def no_in_no_out(x):
    print(x)
```



## 함수의 인수

- 함수는 인자(parameter)를 넘겨줄 수 있다.



### 위치 인수

- 함수는 기본적으로 인수를 위치로 판단한다.



### 기본값(Default Argument Values)

- 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정 할 수 있다.

- 기본 값이 지정된 인자는 항상 마지막에 와야한다!

- 기본 값 설정이 안 되어있다면 반드시 인자를 넣어줘야 한다.

  ```python
  def greeting(age, name = 'ssafy'):
      return f'안녕 나는 {age}살 이고 이름은 {name}이야'
  
  greeting(1)
  
  # error
  def greeting_error(name = 'ssafy', age):
      return f'안녕 나는 {age}살 이고 이름은 {name}이야'
  
  ```



### ★ 키워드 인자(Keyword Argument)

- 키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달 할 수 있다.
- ★  키워드 인자는 순서를 바꿔도 알아서 찾아간다!
- 키워드 인자와 위치 인자를 복합해서 사용 할 수 없다.

```python
def greeting_keyword(age, name = 'ssafy'):
    return f'{name} 은(는) {age} 살 입니다.'

# 기본값 설정 + 키워드 인자 가능
print(greeting_keyword(age = 1))

# 키워드 인자 + 위치 인자 불가능
print(greeting_keyword(age = 2, '내년의 ssafy')) #error

# 위치 인자는 순서에 맞게 적어준다
print(greeting_keyword(30, 서른즈음에))

# 키워드 인자는 순서에 상관없이 알아서 찾아간다
print(greeting_keyword(name = '아홉살 인생', age = '9'))
```



### 가변 인자 리스트

- 앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용한다
- ★ 가변인자는 `*` 로 표현하고 `tupel`의 형태로 출력한다. `list` 아님!!!!

~~~python
print(1, 2, 3, 4, 5, 6, end = ' ^^!', sep = ' <<<< ')
# 1 <<<< 2 <<<< 3 <<<< 4 <<<< 5 <<<< 6 ^^!

def unknown_args(*args):
    print(args, type(args))
    
unknown_args(1, 2, 3, 4, ['a', 'b'], 2, 5,)
# (1, 2, 3, 4, ['a', 'b'], 2, 5) <class 'tuple'>
~~~



#### 실습문제

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 my_max()을 만들어주세요.

```python
def my_max(*nums):
    num = list(nums)
    sorted(num)
    return num[-1]
my_max(-1, 2, 9, 10)
```



### 정의되지 않은 인자 처리하기

- ★ 정의되지 않은 인자는 `**`로 표현하고 `dict` 형태로 출력한다

```python
dict(한국어='안녕', 영어='hi')
# {'한국어': '안녕', '영어': 'hi'}

def unknown_things(**kwargs):
    return kwargs

unknown_things(a='apple', b='banana', c='car', d='disco')
# {'a': 'apple', 'b': 'banana', 'c': 'car', 'd': 'disco'}
```



### dictionary를 인자로 넘기기(unpacking arguments list)

```python
def signup(username, password, password_confirmation):
    if password == password_confirmation:
        return True
    else:
        return False
    
info = {
    'username': 'ryungs',
    'password': '12345r',
    'password_confirmation': '12345r'
}

signup(**info)
# True
```





## ★ 이름공간(namespace) 및 스코프(Scope) 개념이해!

- 파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있다
- LEGB Rule 을 가지고 있다
- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
- 함수 안에서 선언한 변수와 함수 밖에서 선언한 변수는 이름이 같다고 해도 천혀 상관이 없다
- 집에서 유재석은 장남이지만 밖에서 유재석은 국민 mc 이다

- 전역변수는 global로 바꿀 수 있지만 사용하지 않는다



## Lambda 표현식

- def 를 지운다
- 함수 이름과 인자 사이에 = 를 넣는다
- 그 뒤에 lambda를 적는다
- ()를 지운다
- \n 을 없앤다
- return도 지운다

