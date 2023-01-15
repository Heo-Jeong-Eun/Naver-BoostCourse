# Q4. 중복되는 물품은 합쳐서 표기한다. 딕셔너리 데이터의 키 값을 이용해 중복을 확인한다. 
# ouput : {'감': 35, '귤': 25, '배': 30, '사과': 35, '포도': 10}

# A. 
#   key가 겹치는 두 개의 딕셔너리의 요소를 합치고 key를 기준으로 딕셔너리를 정렬한 뒤 출력해준다. 

from collections import Counter # Counter 객체를 사용하기 위해 collections 모듈을 import 

dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first, dict_second):
    dict_third = {} # 합친 딕셔너리를 출력해주기 위한 새 딕셔너리 선언 
    dict_third = (Counter(dict_first) + Counter(dict_second)) # Counter 객체를 사용해 딕셔너리를 합해준다.
    return (dict(sorted(dict_third.items())))
    # sorted()로 정렬, 이때 sorted()만 사용하면 key만 빠진 채 리스트가 된다. 
    # items()를 사용해 key와 value를 딕셔너리의 형태로 출력한다. 
    # 가장 바깥을 dict()으로 감싸 딕셔너리 형태로 반환 받는다. -> Counter 때문에 리스트로 자꾸 출력되기 때문에 추가

print(merge_dict(dict_first, dict_second))

"""
# error code ! 

from collections import Counter

dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first, dict_second):
    return dict(sorted(Counter(dict_first) + Counter(dict_second)))

print(merge_dict(dict_first, dict_second))
"""
