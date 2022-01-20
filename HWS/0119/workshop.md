## 1. List의 합 구하기

정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
list_sum([1, 2, 3, 4, 5])                                                  # => 15
```

```python
def list_sum(list):
    total = 0
    for i in list:
        total += i
    return total

a = list_sum([1, 2, 3, 4, 5])
print(a)

# 교수님 풀이
# 함수 정의
# 인자는 리스트 하나
def list_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(list_sum([1, 2, 3, 4, 5]))        # => 15
```



## 2. Dictionary로 이루어진 List의 합 구하기

Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])     # => 16
```

```python
def dict_list_sum(list):
    age_total = 0
    for dict in list:            # 딕셔너리 분리
        for key in dict:         # 키 분리
            if key == 'age':
                age_total = age_total + dict[key]
    return age_total   
          
a = dict_list_sum([{'name': 'kim', 'age':12}, {'name': 'lee', 'age':4}])
print(a)

# 교수님 풀이
def dict_list_sum(infos):
    # 모든 age들을 더할 변수
    result = 0
    # 순회
    for info in infos:
        result += info['age']     # dict -> {'name': 'kim', 'age':12}
    return result

print(dict_list_sum([{'name': 'kim', 'age':12}, {'name': 'lee', 'age':4}]))
```



## 3. 2차원 List의 전체 합 구하기

정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])                       # => 55
```

```python
def all_list_sum(alllist):
    total = 0
    for list in alllist:
        for i in list:
            total += i
    return total

a = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(a)

# 교수님 풀이
# 2차원 리스트 = 리스트 안에 또 리스트
# numbers = [ [0,1,2],
#             [3,4,5],
#             [6,7,8],]

# for x in range(3):
#     for y in range(3):
#         print(numbers[y][x])

def all_list_sum(numbers):
    result = 0
    for number in numbers:                 # number -> [1] [2, 3] [4, 5, 6] [7, 8, 9, 10]
        for num in number:                 # num -> 1, 2, 3 ...
            result += num
    return result

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
# print(sum(sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]], [])))
```

