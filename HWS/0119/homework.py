# 2번 문제

# 정중앙 문자를 반환 하는 함수
# 만약 문자열의 깅이가 짝수라면 중앙의 2개를 반환
# 함수를 정의
# 전달인자를 받을 매개변수
# def get_middle_char(word):
#     length = 0
#     # 단어 전부 순회
#     for i in word:
#         # 한개씩 개수를 세어보자.
#         length += 1
#     # 정 중앙값
#     center = length // 2

#     # 만약 홀수라면
#     if length % 2:
#         result = word[center]
#     # 짝수라면
#     else:
#         # result = word[center-1] + word[center]
#         result = word[center-1:center+1]
#     return result


# print(get_middle_char('ssafy'))       # => a
# print(get_middle_char('coding'))       # => di

# 3번 문제
# 4번 문제
# def my_func(a, b):
#     c = a + b
#     print(c)
#     return c

# result = my_func(3, 7)
# print(result)

# 5번 문제

# 함수 정의
# 가변 인자 리스트 -> 다수의 인자들을 한번에 받아 보자.
# def my_avg(*numbers):
#     # 평균값을 구하기
#     length = 0
#     count = 0
#     for i in numbers:   # (77, 83, ....)
#         length += 1
#         count += i
#     return count / length

# print(my_avg(77, 83, 95, 80, 70))    # => 81.0

