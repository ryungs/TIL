### 개념

- list, dict에서 인자 추가, 인자삭제, 인제 뽑아내기 개념 알기
- class 상속은 안나옴
- 명세랑 예시출력값 제대로 읽기!

```python
import keyword
print('예약어--------------------------------------')
print(keyword.kwlist)
print()
print('내장함수-------------------------------------')
print(dir(__builtins__))
print()
print('str--------------------------------------')
print(dir(str))
print()
print('list--------------------------------------')
print(dir(list))
print()
print('dict--------------------------------------')
print(dir(dict))
print()
print('set--------------------------------------')
print(dir(set))
print()
print('tuple--------------------------------------')
print(dir(tuple))
```



```python
# 
a = {'유림': '배고파', '동령': '핵추워'}
del a['유림']
print(a)

ap = ['유림', '동령']
del ap[0]
print(ap)

d = {'a' : '1', 'b': '2' }
print(d.get('c'))

b = {'유림': '새치약', '동령': '안돼 더써'}
b['상택']='저는 문과에오'
print(b)

c = {'도건': '아스날'}
c.update(동령='SK')
print(c)
```



# Problem set

###### 1. 정수 3개가 들어온다, 이때 2번째로 큰 정수를 출력해라

```python
def pick(a, b, c):
    if a <= b <= c or c<= b <=a:
        return b
    elif b <= a <= c or c<= a <=b:
        return a
    else:
        return c
    
print(pick(2,0,-1))
```

###### 2. 사용자가 띄어쓰기를 기준으로, (Volume unit) 로 입력한다. 원화로 계산해서 print 해주자.

```python

```





###### 3. 반복문과 조건문만을 활영하여 1~30까지 숫자 중 홀수만 담긴 리스트를 만들어라

```python
[1 2, ]
def num(a):
result = []
for x in range(1, 31):
    if x % 2:
        result.append(x)
        
print(result)
```

 ###### 4. 반복문과 조건문만 활용하여 1~100 까지 자연수 중 5의 배수들의 총합을 구하세요

```python
# 1
y = 0
for x in range(1, 101):
    if x % 5 == 0:
        y += x
print(y)
# 2
y = 0
for x in range(0, 101, 5):
    y += x
print(y)
```

###### 5. 정수 n 이 들어오면, 1 ~ n 까지의 합을 출력하는데(함수)

```python
def my_sum(n):
    x = 0
    for n in range(1, n+1):
        x += n
    return x
my_sum(10)
        
```

###### 6. 'for' 와 ' range' 로 구구단 출력하기

```python
def gugudan():
    
    for x in range(2, 10):
        my_list = []
        for y in range(1, 10):
            my_list += [x * y]
   		print(gugidan)
```

###### 7. 입력으로 높이가 들어옵니다. 높이만큼 산 모양으로 출력하세요.(함수인데 print로 끝. no out.)

```
예시 출력)
높이 = 5 일 때
   ☆
   *
  ***
 *****
*******
```

```python

```

###### 8. dict를 for 문에 활용하기 한번 직접 4가지 반복문을 활용해보고 출력되는 결과를 확인해보세요.

```python
classroom = {"teacher": "Kim", "student1": "Hong", "student2": "Kang"}

for x in classroom :
    print (x) # key값 
    
for y in classroom.keys():
    print(y) # key값 
    
for z in classroom.vlaues():
    print(z) # vlaue값 
    
for q in classroom.items():
    print(q) # key vlaue값  
```



###### 9. 조건문과 반복문, break를 통해서 아래의 코드와 동일한 코드를 작성하세요. (3이 있을 경우 True를 print하고, 아닐 경우 False를 print 합니다.)

```python
numbers = [1, 5, 10]
print(3 in numbers)
예시 출력)
False

result = False
for x in number:
    if x == 3:
        result = True
    	break
print(result)
```

###### 10. colors = [ 'red', 'green', 'blue', 'white', 'black', 'gold' ] 다음 리스트에서 0, 4, 5 index에 있는 요소들을 삭제한 새로운 리스트를 만드세요.

```python
remain = []
for x in colors:
    if colors.index(x) not in (0, 4, 5):
        remain.append(x) #remain += x 왜 안되지?
print(remain)


```

###### 11. 직사각형의 둘레와 면적을 구하는 코드를 작성해주세요.

```markdown
height = 30
width = 20
예시 출력)
직사각형 둘레: 100, 면적: 600입니다.
```

```python
def rec(a, b):
    dul = 2 * (a + b)
    m = a * b
    return f'직사각형 둘레: {dul}, 면적: {m}입니다.'
```

###### 12. 아래의 코드와 동일한 `my_max`함수를 만들어주세요. 정수를 두개 받아서, 큰 값을 반환합니다.

```markdown
max(1, 5)
예상 출력)
5
```

```python
def my_max(a, b):
    if a >= b:
        return a
    else:
        return b
```

###### 13. 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 `my_max()`을 만들어주세요.

```markdown
my_max(10, 20, 30, 50)
예시출력)
50
```

```python
def my_max2(*num):
    num = list(num)
    sorted(num)
    return num[-1]
```

###### 14. 앞선 fake_dict는 단순히 dictionary 형태로 print를 합니다. my_dict() 함수를 만들어 실제로 dictionary를 반환하는 함수를 만들어보세요.

```python
def my_dict(**dictionary):
    return dictionary
```

###### 15. url 패턴을 만들어 문자열을 반환하는 my_url 함수를 만들어 봅시다. 영진위에서 제공하는 일별 박스오피스 API 서비스는 다음과 같은 방식으로 요청을 받습니다.

기본요청 URL : <http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?>

- key : 발급받은 키값(abc)
- targetDt : yyyymmdd
- itemPerPage : 1~10 기본10

예시) 호출 1) my_url(key='abc', targetDt='yyyymmdd')

호출 2) api = { 'key': 'abc', 'targetDt': 'yyyymmdd' } my_url(**api)

예시 출력) '<http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage=10key=abc&targetDt=yyyymmdd&>'

###### 16. URL 검증하기

> 이제 우리는 만들어진 요청을 보내기 전에 URL을 검증해야 합니다. 앞선 설명을 참고하여 검증 로직을 구현하고 문자열을 반환하세요

```
> 아래의 두가지 상황만 만들도록 하겠습니다 <
key, targetDt 가 없으면 '필수 요청변수가 누락되었습니다.'
itemPerPage의 범위가 1~10을 넘어가면 '1~10까지 값을 넣어주세요.'
```

```python
word_list = ['apple', 'apple', 'banana', 'coconut', 'banana', 'kiwi']
# result = {'apple': 2, 'banana': 2, 'coconut': 1, 'kiwi': 1}

def fruits(bamama):
	result = {}
	for x in bamama:
    	result[x] = bamama.count(x)
	return result

fruits(word_list)

```

###### 17.  `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성해봅시다. n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

```python
def fact(n):
    y = 1
    for x in range(1, n+1):
        y *= x
    return y
```



###### 18. 재귀를 이용한 팩토리얼 계산

```

```



###### 19. 피보나치 수열

> 피보나치 수열은 다음과 같은 점화식이 있다.
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해보자.

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

예시 입력)
fib(10)

예시 호출)
89

```python

```



###### 20. chicken coupon

> ex) 치킨쿠폰 3장을 모으면 한마리를 줍니다. 한마리를 시키면 한장을 줍니다. n장이 있을 때, 몇 마리까지 먹을 수 있을까요? ex) 10장 => 7장 + 1장 => 5 + 1 => 3 + 1 => 1 + 1

```python

```



###### 21. 개미수열 (Look & Say)

> 숫자를 세어서 몇개인지 말해요

n = 0 [1]

n = 1 [1, 1]

n = 2 [1, 2]

n = 3 [1, 1, 2, 1]

n = 4 [1, 2, 2, 1, 1, 1]

n = 5 [1, 1, 2, 2, 1, 3]

n = 6 [1, 2, 2, 2, 1, 1, 3, 1]

n = 7 [1, 1, 2, 3, 1, 2, 3, 1, 1, 1]

```python

```



###### 22. 사전 준비

> 다음의 리스트를 만들어보세요.

1. 1~10까지의 숫자 중 짝수만 담긴 리스트 `even_list`
2. 1~10까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`

```python
even_list = [x for x in range(2, 12, 2)]
cubic_list = [x ** 3 for x in range(1,11)]
```



###### 23. 짝짓기 - 곱집합

> 주어진 두 list의 가능한 모든 조합을 담은 `pair` 리스트를 만들어주세요.

1. 반복문 활용

2. list comprehension 활용

   girls = ['jane', 'iu', 'mary']
   boys = ['justin', 'david', 'kim']

   예시 출력)

   [('justin', 'jane'), ('justin', 'iu'), ('justin', 'mary'), ('david', 'jane'), ('david', 'iu'), ('david', 'mary'), ('kim', 'jane'), ('kim', 'iu'), ('kim', 'mary')]

``` python
l = []
for x in boys:
    for y in girls:
        l.append((x,y))
return l

l = [(x,y) for x in boys for y in girls]
```



###### 24. 피타고라스 정리

> 주어진 조건(x < y < z < 50) 내에서 피타고라스 방정식의 해를 찾아보세요.

1. 반복문 활용

2. list comprehension 활용

   예시 출력)
   [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45)]

```python
for x in range(1, 50)
```



###### 25. 모음 제거하기

> 다음의 문장에서 모음(a, e, i, o, u)를 모두 제거하시오.

1. list comprehension만 사용해보세요.

   words = 'Life is too short, you need python!'

   예시출력)
   Lf s t shrt, y nd pythn!

```python

```


 ###### 26. 아래에서 미세먼지 농도가 80 초과인 지역만 뽑자!

dusts = {'seoul': 103, 'kyungi': 79, 'dajeon': 36, 'beijing': 500 }

예상 답 : {'seoul': 103, 'beijing': 500}

```python

```

###### 27. key는 key를 쓰고, value 를 80 초과면 나쁨/ 아니면 안나쁨
dusts = {'seoul': 103, 'kyungi': 79, 'dajeon': 36, 'beijing': 500 }

예상 답 : {'seoul': 'bad', 'kyungi': 'not bad', 'dajeon': 'not bad', 'beijing': 'bad'}

```python

```



28. 지금까지 배운 것을 통해서 Person 클래스를 만들고, 친구와 나를 표현해봅시다.

주머니와 정보를 가지고 있고 (멤버 변수)

인사(`greeting()`)와 주머니에 내용을 추가(`in_my_pocket()`)할 수 있습니다. (메서드)

추가적으로 `get_my_pocket()`으로 지갑에 담긴 정보를 가져와 봅시다.

그리고 사람을 출력하면, 지갑을 제외한 정보를 보여줘보세요.

```

```



###### 29. 이제 배운 것을 활용하여 나만의 리스트 객체를 만들 수 있습니다.

> ```
> class MyList:
> ```

```markdown
* 변수
data : 비어 있는 리스트

* 메서드 
append : 값을 받아 추가합니다.
pop : 마지막에 있는 값을 없애고, 해당 값을 리턴합니다.
reverse : 제자리에서 뒤집고 리턴 값은 없습니다.
count(x) : x의 갯수를 반환합니다.
clear : 값을 모두 삭제합니다.

__repr__ : ex) '리스트 내용 1, 2, 3'
```

###### 30. Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.

```python
def palindrome(word):
    if word == ''.join(reversed(word)):
        return True
    else:
        return False
```

###### 31. 양의 정수 x 를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요

```python
def ok(n):
    min_n = 1
    max_n = n
    
    while min_n ** 2 < n < max_n **2:
        num = (min_n + max_n) / 2
        
        if n < num ** 2:
            max_n = num
        elif n > num **2:
            min_n = num
        elif round(min_n, 4) == round(max_n, 4):
            return round(min_n, 4)
            
```



```python
from collections import Counter
dict(Counter(word_list))
-------------------------------------
customer_arrival_times = [('tony', 1), ('sam', 2), ('tony', 14)]

from collections import defaultdict
example_default_dict = defaultdict(list)

for customer, time in customer_arrival_times:
    example_default_dict[customer].append(time)

dict(example_default_dict)
# {'tony': [1, 14], 'sam': [2]}
```



```python
nums = [1, -7, 2, 15, -11, 2]

maximum_sub_sum(nums)
# 17
# The sum of sub-list nums[2:4]
```

```python
# num 안에 두 쌍의 합이 target이 되는 첫번째 Index 쌍을 반환해주세요
nums = [4, 2, 8, 9, 6]

target = 8
pair_sum(nums, target)
# nums[1] + nums[4] == 8
# [1, 4]

target = 17
pair_sum(nums, target)
# nums[2] + nums[3] == 17
# [2, 3]

target = 99
pair_sum(nums, target)
# no pair sum exists...
# None


```

List에서 기억해야 할 것은
1. slice
2. swap
3. for 문
   3-1. for 문의 index와 다르게 증가(감소)하는 변수(기준)
   3-2. 인접한 element 끼리의 비교입니다. (edited) 
   아마... 이 안에서 시험이 나올 거 같아요.
   더 어려우면
4. 선형구조인 list를 원형구조로 바꾸어서 생각하던가
5. 하나의 link를 node로 보고 연결된 link 구성 등등인데
   그리고 만약 list가 class 관련 문제로 나온다면... stack이 가능성있지 않을까요? 
