# 05 data structure

|           | string    | range     | tuple     | list     | set       | dictionary |
| --------- | --------- | --------- | --------- | -------- | --------- | ---------- |
| ordered   | ordered   | ordered   | ordered   | ordered  |           |            |
| unordered |           |           |           |          | unordered | unordered  |
| mutable   |           |           |           | mutable  | mutable   | mutable    |
| immutable | immutable | immutable | immutable |          |           |            |
| iterable  | iterable  | iterable  | iterable  | iterable | iterable  | iterable   |

- mutable : 값이 변하는지?
- iterable : list, dict, set, str, tuple, range, bytes > for문을 돌릴 수 있는가



## 문자열 메소드 활용하기

### 변형 (원본은 그대로인 애들)

string = ' '

iterable = ()tuple [] list { : }dict

##### `string.capitalize()` : 문장의 제일 첫 글자만 대문자로 만들고, 나머지는 다 소문자로 반환

##### `string.title()` :  어포스트로피나 공백을 이후의 첫 글자를 대문자로 만들어 반환

##### `string.upper()` : 모든 글자를 대문자로 만들어 반환

##### `string.lower()` :  모든 글자를 소문자로 만들어 반환

##### `string.swapcase()` : 대문자 ↔ 소문자 를 바꾸어 반환

```python
text =  'HI! EveryOne, I\'m ssafy'
text.capitalize() # 'Hi! everyone, i'm ssafy'
text.title() # 'Hi! Everyone, I'M Ssafy'
text.upper() # 'HI! EVERYONE, I'M SSAFY'
text.lower() # hi! everyone i'm ssafy'
text.swapcase() # hi! eVERYONE, i'M SSAFY'
```



##### `붙이고싶은값.join(iterable)` : iterable(str, tuple, list)의 사이사이에 string 값을 붙여 특정한 **문자열**로 반환

```python
exam = '시험잘치자'
'!'.join(exam) #시!험!잘!치!자

exam = ['시험', '잘치자']
'!^^ '.join(exam) # '시험!^^ 잘치자'
```



##### `string.replace(old, new, count])` : 바꿀 대상의 글자를 새로운 글자로 바꿔서 반환

count를 지정하면 해당 갯수만큼만 시행합니다.

```python
'aaaaaaaaaa'.replce('a', 'b') # bbbbbbbbbb
'aaaaaaaaaa'.replce('a', 'b', 3) # bbbaaaaaaa
```



##### `string.strip()` : 양쪽 공백 제거 \n, \t도 공백으로 처리

##### `string.lstrip()` : 왼쪽 공백 제거

##### `string.rstrip()` : 오른쪽 공백 제거

```python
'     양쪽없어져라\n    '.strip() # 얘만 \n, \t도 공백으로 처리
# '양쪽없어져라'

'     왼쪽만없어져라\n    '.lstrip()
# '왼쪽만없어져라\n    '

'     오른쪽만없어져라\n    '.rstrip()
# '     오른쪽만없어져라\n'
```





### 탐색 및 검증 (원본은 그대로인 애들)

##### `string.find('x')` : x의 첫번째 위치를 반환, **없으면 -1을 반환**

 ```python
'apple'.find('p') # 1
'apple'.find('c') # -1
 ```

`string.index('x')` : x의 첫번째 위치를 반환, **없으면 error가 뜬다**

```python
'apple'.index('p') # 1
'apple'.index('c') # error
```



### 참 거짓 반환 (원본은 그대로인 애들)

##### `string.isaplha()` : 스트링이 모두 알파벳이면 True 아니면 False 반환

##### `string.issuper()` :  스트링이 모두 대문자이면 True 아니면 False 반환

##### `string.islower()` :  스트링이 모두 소문자이면 True 아니면 False 반환

##### `string.istitle() `:  스트링이 모두 title이면 True 아니면 False 반환



##### `string.isdecimal()` : 스트링이 모두 10진수이면 True 아니면 False 반환

##### `string.isdigit()` :  스트링이 모두 10진수이면 True 아니면 False 반환

##### `string.isnumeric()` : 스트링이 모두 숫자이면 True 아니면 False 반환



##### `string.isspace() `:  스트링이 모두 공백이면 True 아니면 False 반환



##### `string.split('특정단위')` : 문자열을 특정한 단위로 잘라서 **리스트로 반환**

- 괄호 안에 아무것도 안 적으면 띄워쓰기 기준으로 잘라서 리스트로 반환

  ```python
  'apple'.split()
  # ['a', 'p', 'p', 'l', 'e']
  
  'a_b_c'.split('_')
  # ['a', 'b', 'c']
  
  '1 : 2 : 3'split(':')
  # ['1 ', ' 2 ', ' 3']
  ```

  

## 리스트 메소드 활용하기

### 값 추가 및 삭제 (원본 수정)

##### `[list].append('string')` : 리스트에 값을 추가할 수 있다, 수행하는 만큼 리스트에 값이 쌓인다

##### `[list].extend(iterable)` : 리스트에 iterable(list, range, tuple, string유의) 값을 추가 가능, 수행하는 만큼 리스트에 값이 쌓인다 

- **append와 extend비교**

  ```python
  caffes = ['starbucks', 'tom&toms', 'coffeebean', 'hollys']
  caffes.append(['the venti']) 
  print(caffes) 
  # ['starbucks', 'tom&toms', 'coffeebean', 'hollys', ['the venti']]
  # 리스트를 그대로 넣음
  
  caffes.extend(['쥬씨']) # caffes.extend({'쥬씨'}) set도 이하 동문
  print(caffes)
  # ['starbucks', 'tom&toms', 'coffeebean', 'hollys', '쥬씨']
  # 리스트 안에 문자열만 넣음
  ```

- **extend에 string 넣을 때는 조심하기**

  ```python
  caffes.extend('ediya') # caffes.extend(('ediya')) 튜플도 이하 동문
  print(caffes)
  # ['starbucks', 'tom&toms', 'coffeebean', 'hollys', '쥬씨','e', 'd', 'i', 'y', 'a']
  # 문자열을 하나하나씩 넣음
  ```



##### `[list].insert(index값,'string')` : 인덱스 값 위치에 string를 추가

- `[list].insert(index값,['string'])`: ['string']  그대로 추가
- `[list].insert(index값,{'string'})`:  {'string'} 그대로 추가
- `[list].insert(index값,('string')`: 'string' 추가

```python
fast_foods = ['McDonald', 'burgerking', 'KFC']

fast_foods.insert(1, 'Moms touch')
# ['McDonald', 'Moms touch', 'burgerking', 'KFC']

fast_foods.insert(3, 'Lotteria')
# ['McDonald', 'Moms touch', 'burgerking', 'KFC', 'Lotteria']
```



##### `[list].remove(인자그대로)` :  리시트에서 입력한 인자를 삭제 합니다.

- 처음 만나는 애 한번만 지움

- 원본이 파괴되기 때문에 하나번 지워지면 끝!

  ```python
  numbers = [1, 2, 3, 1, 2]
  print(numbers) # [1, 2, 3, 1, 2]
  
  numbers.remove(1)
  print(numbers) # [2, 3, 1, 2]
  
  numbers.remove(1)
  print(numbers) # [2, 3, 2]
  
  numbers.remove(1)
  print(numbers) # error
  ```

  

##### `[list].pop(index값)` : 정해진 index에 위치한 값을 원본에서삭제하고 그 항목을 반환한다

index 값이 지정되지 않으면 리스트의 마지막 항목을 원본에서 삭제하고 반환한다

```python
bag = ['카드', '명찰', '휴대폰', '보조배터리']
bag.pop() # '보조배터리'
print(bag) # ['카드', '명찰', '휴대폰']
bag.pop(1) # '명찰'
```



### 탐색 및 정렬

##### `[list].index(x)` : 리스트 안의 x 값의 index 위치를 반환

```python
wishlist = ['여행', '먹방투어', '스카이다이빙']
wishlist.index('여행') # 0
wishlist.index('잠') # error
```



##### `[list].count(x)` : x 값의 갯수를 확인 할 수 있다

```python
alph = ['a', 'b', 'c', 'd', 'b', 'b']
alph.count('b') # 3

target = 'b'
for i in range(alph.count('b')):
    alph.remove(target)
print(alph) # ['a', 'c', 'd']      

# count와 remove 메소드를 활용해서 원하는 함수를 만들 수 있다
def my_list(l, target):
    for i in range(l.count(target)):
        l.remove(target)
    return l
my_list([1, 2, 2, 3, 4, 2, 2], 2) # [1, 3, 4]
```



##### `[list].sort()` : 순서대로 정렬해준다. 함수이자 메소드, 원본 수정, None 값 return 

##### `sorted(list)` : 순서대로 정렬해준다. 원본 유지 , 정렬해준다

- ###### `.sort()` 와 `sorted()` 비교

  ```python
  # .sort() 원본 파괴
  my_list = [4, 3, 2, 1]
  sorted_list = my_list.sort()
  print(my_list, sorted_list)
  # [1, 2, 3, 4] None
  
  # sorted() 원본 유지
  my_list = [4, 3, 2, 1]
  sorted_list = sorted(my_list)
  print(my_list, sorted_list)
  # [4, 3, 2, 1] [1, 2, 3, 4]
  ```



##### `[list].reverse()` : 리스트를 반대로 뒤집음, 정렬은 아님!! 원본 수정 None 값 return 

```python
classmates = ['친구1', '친구2', '친구3']
mates = classmates.reverse()
print(classmates, mates)
# ['친구3', '친구2', '친구1'] None
```



## ★ 복사 ★

- 복사하고 나면 immutable 한 string, int, range, tuple 은 결과 값이 다르고 
- 어딘가 위치를 찍고 있는 mmutable한 리스트, 셋, 딕셔너리는 결과값이 같다.

```python
# 문자열 복사
origin = 'A'
copy = origin
print(origin, copy) # A A

origin = 'B'
print(origin, copy) # A B

print(origin == copy) # False
print(id(origin) == id(copy)) # False

# 리스트 복사
o_list = ['a']
c_list = o_list
print(o_list, c_list) # ['a'] ['a']

o_list.append('b')
print(o_list, c_list) # ['b'] ['b']

print(o_list == c_list) # True
print(id(o_list) == id(c_list) # True

# 딕셔너리 복사
lunch = {'최애1': '치킨', '최애2': '아이스크림', '최애3': '떡볶이'}
dinner = lunch
dinner['최애3'] = '초콜릿'
print(lunch, dinner) 
# {'최애1': '치킨', '최애2': '아이스크림', '최애3': '초콜릿'} {'최애1': '치킨', '최애2': '아이스크림', '최애3': '떡볶이'}
```



### 리스트를 진짜 복사하고 싶다면

```python
# 첫 번째
a = [1, 2, 3]
b = a[:] # 이렇게 복사해야 함
a[0] = 5
print(a, b) # [5, 2, 3] [1, 2, 3]

# 두 번째
a = [1, 2, 3]
b = list(a) # 이걸 리스트 캐스팅이라고 부르는데 이렇게 치면 위치값을 받는게 아니라 진짜 값을 받는다.
a[0] = 5

print(a, b) # [5, 2, 3] [1, 2, 3]
```



### 얕은 복사(shallow copy) 

### 깊은 복사(deep copy) : import copy → copy.deepcopy(x)

- 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)를 해야합니다. 그래야 내부에 있는 모든 객체까지 새롭게 값이 변경됩니다.

```python
# 리스트 안에 리스트가 있을 때

# 얕은 복사
o = [1, 2, [3, 4]]
c = o[:] #이게 얕은 카피
o[0] = 100
o[2][0] = 100
print(o) # [100, 2, [100, 4]]
print(c) # [1, 2, [100, 4]]

# 깊은 복사
import copy
o = [1, 2, [3, 4]]
c = copy.deepcopy(o)
o[0] = 100
o[2][0] = 100
print(o) # [100, 2, [100, 4]]
print(c) # [1, 2, [3, 4]]


# 딕셔너리 안에 딕셔터리가 있을 때

# 얕은 복사
ss3 = {
    'teacher': 'neo',
    'gamtoo' : {
        'leader': 'Hwang',
        'CA' : 'Kang'
    }
}

new_ss3 = dict(ss3)
ss3['gamtoo']['CA'] = 'KANGJW'

print(ss3) # {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'KANGJW'}}
print(new_ss3) # {'teacher': 'neo', 'gamtoo': {'leader': 'Hwang', 'CA': 'KANGJW'}}

# 깊은 복사
import copy
ss3 = {
    'teacher': 'neo',
    'gamtoo' : {
        'leader': 'Hwang',
        'CA' : 'Kang'
    }
}

# Deep copy
new_ss3 = copy.deepcopy(ss3)
ss3['gamtoo']['CA'] = 'KANGJW'

print(ss3)
print(new_ss3)
```



##### `[list].clear()` : 리스트의 모든 항목을 삭제합니다. 원본파괴

```python
numbers = list(range(1, 10))
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.clear()
print(numbers) # []
```



## ★ List Comprehension : 리스트를 만드는 간단한 방법

> 다음 리스트를 만들어보세요.

- 1 ~ 10까지의 숫자 중 짝수만 담긴 even_list

- 1~ 10까지의 숫자로 만든 세제곱 담긴 cubic_list

- 여러개의 for 문 혹은 if 문을 중첩적으로 사용가능

```python
even_list = [x * 2 for x in range(1, 6)]
print(even_list) # [2, 4, 6, 8, 10]

cubic_list = [x ** 3 for x in range(1, 11)]
print(cubic_list) # [1, 8, 27, 64, 125, 216, 343,512, 729, 1000] 
```



#### 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 full_name 리스트를 만들어주세요

- 반복문 활용

- list comprehension 활용

  ```python
  # 반복문 활용
  first_name = ['수지', '지은', '수정']
  last_name = ['배', '이', '정']
  
  full_name = []
  for x in last_name:
      for y in first_name:
          full_name += [(x,y)]
  print(full_name)
  
  # list comprehension 활용
  first_name = ['수지', '지은', '수정']
  last_name = ['배', '이', '정']
  full_name = [(x, y) for x in last_name for y in first_name]
  print(full_name)
  ```

#### 피타고라스 정리

>  주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

- 반복문 활용

- list comprehension 활용

  ```python
  # 반복문 활용
  pita = []
  
  for x in range(1, 50):
      for y in range(1, 50):
          for z in range(1, 50):
              if x < y < z:
                  if x ** 2 + y ** 2 == z ** 2:
                      pita += [(x, y, z)]
  print(pita)
  
  # list comprehension 활용
  pita = [(x, y, z) for x in range(1, 50) for y in range(1, 50) for z in range(1, 50) if x < y < z if x ** 2 + y ** 2 == z ** 2]
  print(pita)
  ```

  

#### 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

```python
words = 'Life is too short, you need python!'
vowels =  'aeiouAEIOU'
result = [x for x in words for x not in vowels]
print(result)
print(''.join(result))
```



## 딕셔너리 메소드 활용

### 추가 및 삭제 (원본 수정되는 애들)

##### `dict.pop(key, default)` : key가 딕셔너리에 있으면 원본에서 제거하고 제거한 value 값을 반환 그렇지 않으면 default 값을 반환

- default가 없는 상태에서  딕셔너리에 없으면 keyerror 발생

```python
fruits = {'apple': '사과', 'banana': '바나나'}
fruits.pop('apple') # 사과
print(fruits) # {'banana': '바나나'} 원본 수정!!!

# 없는거 꺼내보기
fruits.pop('melon') #  keyerror

# default 지정해서 없는거 꺼내보기
fruits.pop('melon', '없어유') # 없어유
```



##### `dict.update(key = value)` : 원하는 것으로 key  value 값 변경

```python
fruits = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
fruits.update(banana = '버내너') #딕셔너리로 넘겨주는거 아니다
print(fruits) # {'apple': '사과', 'banana': '버내너', 'melon': '멜론'}
```



##### `dict.get(key, default = None)` : key를 입력하면 value를 보여준다

- 절대로 key error가 발생하지 않는다 
- default 값이 None 이다

```python
# 그냥 key 값 넣는거랑 .get 메소드 차이
fruits = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

fruits['apple']  # 사과
fruits['pineapple'] # error

fruits.get('apple') # 사과
print(fruits.get('pineapple')) # None

fruits.get('strawberry', False) # 없어유
```



## dictionary comprehension

- dictionary도 comprehension을 활용하여 만들 수 있습니다.

```python
cubic_dict = { x: x ** 3 for x in range(1, 5) }
print(cubic_dict) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 아래에서 미세먼지 농도가 80 초과인 지역만 뽑자!
dusts = {'seoul': 103, 'kyungi': 79, 'dajeon': 36, 'beijing': 500 }

bad = { city: dust for city. dust in dusts.items() if dust > 80 }
print(bad) # {'seoul': 103, 'beijing': 500 }

# key는 key를 쓰고, value 가 80 초과면 bad/ 아니면 not bad
# 삼항연산자 쓸 때는 if 문 쓰고 for 문
how_bad = { city: 'bad' if dust > 80 else 'not bad' for city. dust in dusts.items()}
print(how_bad) # {'seoul': 'bad', 'kyungi': 'not bad', 'dajeon': 'not bad', 'beijing': 'bad'}
```



## set 메서드 활용 set은 중복 x

### 추가 및 삭제 (원본 수정)

##### `set.add(element)` : string, int element를 추가

```python
a = {1, 2, 3, 4}
a.add(5) # {1, 2, 3, 4, 5}
a.add(5) # {1, 2, 3, 4, 5} 두번 추가해도 중복이라서 한번만
print(a) # {1, 2, 3, 4, 5} 원본 수정
```



##### `set.update(*other)` :  여러가지 값을 순차적으로 추가, 반드시 iterable 한 값을 넣어야함

- 튜플, 셋, 리스트, 스트링 추가 가능

```python
b = {3, 4, 5}
b.update({6, 6, 7, 8},{1, 2})
print(b) # {3, 4, 5, 6, 7, 8, 1, 2}
```



##### `set.remove(element)` : element를 set에서 삭제하고 없으면 **error 를 발생**

##### `set.discard(element)` : element를 set에서 삭제하고 없어도 error 발생 x 

##### `set.pop()` : 임의의 원소를 set에서 제거하고 반환

- set은 순서가 없기 때문에 입력 값 없이 임의의 원소를 제거하고 반환하다, 얼핏보면 가장 작은 원소를 제거하는 것 같지만 아닐 때도 있기 때문에 쓰지 않는 것을 추천!!



## 내장함수

##### `map(function, iterable)` :  iterable 원소들을 function에 적용한 후, 그 결과를 돌려줌

##### `zip()` : 

##### `filter()` : 

