
# dict에서 원하는 key 없애기
a = {'유림': '배고파', '동령': '핵추워'}
del a['유림']
print(a)

# list에서 원하는 인자 없애기
ap = ['유림', '동령']
del ap[0]
print(ap)

# dict에서 없는 key 갑 불러내면 None값 나옴
d = {'a' : '1', 'b': '2' }
print(d.get('c'))

# dict에서 원하는 key, vlaue 추가하기
b = {'유림': '새치약', '동령': '안돼 더써'}
b['상택']='저는 문과에오'
print(b)

# dict에서 원하는 key, vlaue 추가하기
c = {'도건': '아스날'}
c.update(동령='SK')
print(c)

# dict에서 key, value 추출하기
mates = {'1': '유림', '2':'상택', '3':'도건', '4':'재영'}
for key, value in mates.items():
    print(key, value)

# 문제
word_list = ['apple', 'apple', 'banana', 'coconut', 'banana', 'kiwi']
# result = {'apple': 2, 'banana': 2, 'coconut': 1, 'kiwi': 1}

def some(x):
    a_set = {}
    for x in word_list:
        a_set[x] = word_list.count(x) # dict에서 원하는 key, vlaue 추가하기
    return a_set

print(some(word_list))
