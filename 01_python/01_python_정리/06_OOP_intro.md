# 06_OOP_intro

#### OOP : Object Oriented Programming 객체 지향 프로그램

>  컴퓨터 프로그래밍의 패러다임의 하나이다. 객체지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립적인 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고 받고, 데이터를 처리할 수 있다.

> 명령형 프로그래밍인 절차지향 프로그래밍에서 발전된 형태를 나타내며, 기본 구성요소는 다음과 같다.

- 클래스(Class) 
  * 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것으로 
  * 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있다. 
  * 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인하여야 한다.
- 인스턴스 
  * 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다.
  * 객체는 자신의 고유한 속성(attribute)을 가지며 클래스에 정의한 행위(behavior)를 수행할 수 있다.
  * 객체의 행위는 클래스에서 정의한 행위를 공유함으로써 메모리는 경제적으로 사용한다.
- 메서드(Method)
  * 클래스로부터 생성된 객체를 사용하는 방법으로 
  * 객체에 명령을 것이라고 할 수 있다.
  * 메서드는 한 **객체의 속성**을 조작하는데 사용된다.

  

| class | 사람   | list      | dict         | int     | set          | str            |
| ----- | ------ | --------- | ------------ | ------- | ------------ | -------------- |
|       | 곽동령 | [1, 2]    | {a:1}        | 49      | {1, 2}       | 'hi'           |
|       | 이유림 | [1]       | {}           | 0       | 0            | ''             |
|       | 이상택 | [2, 3, 4] | {b: 2, c: 3} | 1000000 | {2, 3, 4, 5} | 'happyhacking' |

- class 안에 있는 함수를 메서드라고 부른다
- hi는  str 이라는 class의 instance이다. 결국 instance는 관계를 뜻한다
- 존재하는 모든 것은 object



```python
# list class의 object가 할 수 있는 것들을 알아봅시다.
print(dir(list)) # list가 할 수 있는 명령어 불러오는 거
'__add__', '__class__', '__contains__', '__delattr__', '__delitem__' '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getiem__','__gt__','__hash__','__iadd__','__imul__','__init__','__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
```



## 클래스 및 인스턴스

### 클래스 객체 

- 이름 지을 때 첫 글자 대문자 (Upper Camel Case로 구분)

- 선언과 동시에 클래스 객체가 생성됨

- 선언시 self는 반드시 작성해라!

- 선언된 공간은 지역 스코프로 사용된다

- 정의된 어트리뷰트 중 변수는 멤버 변수로 불린다

- 정의된 함수 (def)은 메소드로 불린다

  ```python
  # Person 클래스를 만들어 보자
  class Person:
      name = '홍길동'
      
      def say_hi(self):
          print('Hello!')
          
      def intro(self):
          print(f'I am {self.name}') # 그냥 name 적으면 안돼!
          
  p = Person()
  p.say_hi() # HELLO!
  p.intro() # I am 홍길동
  ```

  

### 인스턴스 객체

- 인스턴스 객체는 `ClassName()`을 호출함으로써 선언된다
- 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 가지고 있다
- 인스턴스 → 클래스  → 전역 순으로 탐색한다

```python
# 클래스 Person의 인스턴스 'iu'를 만들어 봅시다
iu = Person()

iu.say_hi() # HELLO!
iu.name # 홍길동

# iu 이름 바꿔주기
iu.name = '이지은'
print(iu.name) # 이지은
iu.intro # I am 이지은

# iu와 Person이 같은지 확인 isinstance()
print(isinstance(iu, Person)) # True
print(isinstance([], list)) # True

print(type(iu) == Person) # True
print(type('a') == str) # True
```



#### 파이썬 출력의 비밀

- *Object.__ repr__(self)*  : `파이썬 인터프리터`가 해당 객체를 인식 할 수 있는 공식적인 문자열을 나타낼 때 사용
- *Object.__ str__(self)*  : `적당히` 사용자가 보기 쉬운 형태로 출력 할 때 사용

