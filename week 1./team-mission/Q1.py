# Q1. num_list에서 홀수 데이터만 출력하는 함수를 작성
# output : [1, 5, 7, 15, 29]

# A. 
#   1. 홀수만 저장할 리스트를 선언, 
#   2. num_list를 for문으로 반복했을 때 
#   3. i == num_list의 원소 값을 2로 나누었을 때 나머지가 1인 경우
#   4. 리스트에 요소를 추가하는 함수인 append()를 사용하여 해당 i값을 result 리스트에 추가한다.  


num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    result = [] # 빈 리스트 선언
    for i in num_list: # num_list까지 반복, 리스트 모든 요소를 반복문으로 훑고 싶을 때는 in 뒤에 리스트를 지정하면 된다.
        if i % 2 == 1: # 홀수 판별식, 2로 나누었을 때 나머지가 1인 경우 
            result.append(i) # result라는 리스트에 append() 명령어로 i를 추가해준다. 
    return result

print(get_odd_num(num_list))


# error code !
# output : [1, 5, 7, 15, 16, 22, 28, 29]
"""
# A. 
#   짝수인 경우 del을 이용해 삭제하고 num_list를 출력하려고 했으나 
#   del, clear, remove, pop을 사용해도 삭제되지 않아서 실패했다. 
#   인덱스를 보고 요소를 삭제하는 명령어라서 에러가 발생하는 것인지 어떤 이유인지 아직 찾지 못했다. 

def get_odd_num(num_list):
    result = []
    for i in num_list:
        if i % 2 == 0:
            result.remove(i)
            result.clear(i)
            result.pop(i)
            del i 
    return num_list 

print(get_odd_num(num_list))
"""