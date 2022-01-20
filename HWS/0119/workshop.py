# # 1번 문제

# # 함수 정의
# # 인자는 리스트 하나
# def list_sum(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result

# print(list_sum([1, 2, 3, 4, 5]))        # => 15

# # 2번 문제
# def dict_list_sum(infos):
#     # 모든 age들을 더할 변수
#     result = 0
#     # 순회
#     for info in infos:
#         result += info['age']     # dict -> {'name': 'kim', 'age':12}
#     return result

# print(dict_list_sum([{'name': 'kim', 'age':12}, {'name': 'lee', 'age':4}]))

# 3번 문제
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