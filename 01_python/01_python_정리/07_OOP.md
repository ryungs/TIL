# 07_OOP

## OOP with Python

## ★ 용어 정리 ★

```python
class Person:                      #=> 클래스 정의(선언) : 클래스 객체 생성
    name = '홍길동'                  #=> 멤버 변수(데이터 어트리뷰트)
    def greeting(self):            #=> 멤버 메서드(메서드)
        print(f'{self.name}')
        
iu = Person()       # 인스턴스 객체 생성
daniel = Person()   # 인스턴스 객체 생성
iu.name             # 데이터 어트리뷰트 호출
iu.greeting()       # 메서드 호출
```

```python
# Person을 만들어봅시다.
class Person:
    name = 'ssafy kim'
    def greeting(self):
        return f'Hi! {self.name}'

p = Person()

print(p.name) # ssafy kim
p.name = 'kim gildong'
print(p.greeting()) # Hi! kim gildong
print(p.name) # kim gildong

# 클래스와 인스턴스 간의 관계를 확인해 봅시다
isinstance(p, Person) # p 는 Person 이야? True
isinstance(1, int) # 1은 int야? True
```



### `self` :  인스턴스 객체 자기자신

- C++ 혹은 자바에서의 this 키워드와 동일함
- 특별한 상황을 제외하고는 무조건 메소드에서 self를 첫번째 인자로 설정한다.
- 메소드는 인스턴스 객체가 함수의 첫번째 인자로 전달되도록 되어 있다

```python
# p를 인사시키는 방법
p.name = '홍길동'
print(p.greeting()) # Hi! 홍길동

# 사람 중 홍길동을 인사시키자
Person.greeting(p)  # Hi! 홍길동
```

- 클래스 선언 부 내부에서도 반드시 self 를 통해 어트리뷰트에 접근해야 한다.



### ★ 클래스-인스턴스 간의 이름공간 ★

- **클래스를 정의**하면, **클래스 객체가 생성**되고 해당되는 이름 공간이 생성된다
- **인스턴스를 만들게 되면**, **인스턴스 객체가 생성**되고 해당되는 이름 공간이 생성된다
- **인스턴스의 어트리뷰트가 변경**되면, 변경된 데이터를 **인스턴스 객체 이름 공간**에 저장한다.
- 즉, **인스턴스의 특정한 어트리뷰트에 접근**하게 되면 **인스턴스 → 클래스 순**으로 탐색한다



### 생성자/ 소멸자

- **생성자**는 **인스턴스 객체가 생성될 때** 호출되는 함수이며
- **소멸자**는 **객체가 소멸되는 과정**에서 호출되는 함수이다

#####  양쪽에 언더스코어가 있는 메서드를 = 스페셜 메소드, 매직 메소드라고 부른다

```python
def __init__(self): # 생성자
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    
def __del__(self): # 소멸자
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

```python
# 생성자와 소멸자를 만들어 봅시다
class Person:
    def __init__(self):
        print('응애!')
    def __del__(self):
        print('빠잉~')
        
p1 = Person() # 응애!
del p1 # 빠잉~
p1 = 1 # 빠잉~ p1이 Person()에 손가락을 가르키고 있다가 1로 손가락 방향을 변경하니까 빠잉이 나옴!
```

- 아래와 같이 모두 사용 가능
- 생성자 값을 초기화 하는 과정에서 자주 활용

```python
def __init__(self, parameter1, parameter2):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
    print(parameter1)

def __init__(self, *args):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __init__(self, **kwagrs):
    print('생성될 때 자동으로 호출되는 메서드입니다.')
```



### 클래스 변수/ 인스턴스 변수

```python
class Person:
    population = 0              # 클래스 변수 : 모든 인스턴스가 공유함.
    
    def __init__(self, name):   
        self.name = name        # 인스턴스 변수 : 인스턴스별로 각각 가지는 변수
```

```python
# 위의 생성자와 인사하는 메소드를 만들어봅시다. 
class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1

# 본인의 이름을 가진 인스턴스를 만들어봅시다.
p1 = Person('나다')
p1.name # 나다

# 옆자리 친구의 이름을 가진 인스턴스를 만들어봅시다.
p2 = Person('너다')
p2.name # 너다

# population을 출력해봅시다.
Person.population # 출력한 만큼 올라감

# 물론, 인스턴스도 접근 가능합니다. 왜일까요?!
p1.population # 출력한 만큼 올라감
```



### 정적 메소드(static method)/ 클래스 메소드(classmethod)

- 메소드 호출은 인스턴스가 아닌 클래스가 할 수 있도록 구성할 수 있다
- 이때 활용되는게 ★정적 메소드 혹은 클래스 메소드★ 이다
- **정적 메소드**는 객체가 전달되지 않은 형태이며
- **클래스 메소드**는 인자로 클래스를 넘겨준다

#### staticmethod는 다음과 같이 정의됩니다.

```python
@staticmethod
def methodname():
    codeblock
```

#### classmethod는 다음과 같이 정의됩니다.

```python
@classmethod
def methodname(cls):
    codeblock
```



#### ★ 실습문제 ★

> 사실 이전에 작성한 Mylist는 완벽하지 않았습니다
>
> 한번 제대로 된 자료구조를 만들어 봅시다
>
> `Stack` 클래스를 간략하게 구현해봅시다
>
> `Stack` : 스택은 LIFO(Last in First Out)으로 구조화된 자료구조를 뜻합니다

- `empty()` : 스택이 비었다면 참을 주고 그렇지 않으면 거짓
- `top()` : 스택의 가장 마지막 데이터를 넘겨준다 **스택이 비었다면 None을 리턴**
- `pop()` : 스택의 가장 마지막 데이터 값을 넘겨주고 해당 데이터 삭제,  **스택이 비었다면 None을 리턴**
- `push()` : 스택의 가장 마지막 데이터 뒤에 값을 추가한다 **리턴값 없음**

```python
# 여기에 코드를 작성해주세요.
class Stack:
    def __init__(self):
        self.items = []
        
    def empty(self):
        return not bool(self.items)
    
    def push(self, e):
        self.items.append(e)
    
    def pop(self): 
        if not self.empty():
            return self.items.pop()
    
    def top(self): 
        if self.items:
            return self.items[-1]
           
    # 객체 자체가 리턴하는 값
    def __repr__(self):
        return '\n'.join(self.items)
    
    # 객체를 print 하면 나오는 값
    def __str__(self):
        return'|'.join(self.items)
    
# 인스턴스를 하나 만들고 메소드 조작을 해봅시다.
s = Stack()
print(s.empty()) # True
print(s.push(1)) # None
print(s.push(2)) # None
print(s.empty()) # False
print(s.top()) # 맨 위에 있는 2을 그냥 읽고
print(s.empty()) # False
print(s.pop()) # 맨 위에 있는 2을 꺼내서 읽고
print(s.empty()) # False
print(s.top()) # 맨 위에 있는 1을 그냥 읽고
print(s.pop()) # 맨 위에 있는 1을 꺼내서 읽고
print(s.pop()) # None
print(s.empty()) # True
print(s.push('a')) # None
print(s.push('b')) # None
print(s.push('c')) # None

print(s) # a|b|c
s # a b c
```



### 연산자 오버라이딩(중복 정의) 덮어쓰기

- 파이썬에 기본적으로 정의된 연산자를 직접적으로 정의하여  활용할 수 있다

  ```python
  + __add__
  - __sub__
  * __mul__
  < __lt__
  <= __le__
  == __eq__
  !+ __ne__
  >= __ge
  > __gt__
  ```

  

## 상속

- 클래스에서 가장 큰 특징은 상속
- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높다
- 이처럼 상속은 공통된 속성이나 메서드를 부모 클래스에 정의하고, 이를 상속받아 다양한 형태의 사람들을 만들 수 있다

#### `issubclass(x, y)` : x가 y의 자식 클래스냐?

- True, false 형태로 나옴



#### `super()`

- 자식 클래스에 메소드를 추가 구현할 수 있다

- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있다

  ```python
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email 
          
      def greeting(self):
          print(f'안녕, {self.name}')
          
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          super().__init__(name, age, number, email) # 내 상위 클래스를 그대로 가져온다는 뜻  Person()과 같은 말
          self.student_id = student_id
          
  p1 = Person('홍길동', 200, '0101231234', 'hong@gildong')
  s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
  s1.greeting()
  ```



### 메소드 오버라이딩

- 메서드를 재정할 수도 있다.

  ```python
  # 군인은 다른 인사를 합니다.
  class Soldier(Person):
      def __init__(self, name, age, number, email, army):
          super().__init__(name, age, number, email)
          self.army = army
          
      def greeting(self):
          print(f'충성! {self.army} {self.name}')
  s = Soldier('권택건', '25', '0101234568', 'Hermes@hermes.com', '준위')
  s.greeting() 
  ```

  

### 상속관계에서 이름공간

- 기존의 인스턴스 → 클래스 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장된다
- 인스턴스 → 자식클래스 → 부모 클래스 → 전역



### 다중상속

- 두개 이상의 클래스를 상속받는 경우, 다중상속이 됩니다.

  ```python
  # 아래에 코드를 작성해주세요.
  class Person:
      def __init__(self, name):
          self.name = name
      
      def breath(self):
          return '날숨'
      
      def greeting(self):
          return 'hi' + self.name
      
  class Mom(Person):
      gene = 'XX'
      
      def swim(self):
          return '첨벙첨벙'
      
  class Dad(Person):
      gene = 'XY'
      
      def kick(self):
          return '슛'
      
  class Child(Dad, Mom):
      def cry(self):
          return '응애'
      
  c = Child('애')
  c.swim() # 첨벙첨벙
  ```

  