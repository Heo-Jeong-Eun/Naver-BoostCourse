# Q5.
# ouput : 
"""
inputs = "cat32dog16cow5" 

string_list = find_string(inputs)
print(find_string)
>>> ['cat', 'dog', 'cow']
"""

# A. 
#   문자열에서 알파벳만 추출 후 리스트에 저장, 출력한다. 

import re # 정규 표현식, findall을 사용하기 위해 regex 모듈을 import 

inputs = "cat32dog16cow5" 

def find_string(inputs):
    alphas = re.findall('[a-zA-Z]+', inputs) 
    # findall은 문자열을 리스트로 반환한다. 
    # [a-zA-Z] == 문자 클래스를 사용해 알파벳 모두를 선택
    # 뒤에 +를 붙여 앞의 문자가 최소 한 개 이상 존재하는지 확인한다. 
    # 즉 문자가 연속으로 저장되다가 [] 범위 안에 있는 값이 아니면, (이 문제의 경우 문자) 현재 값까지 리스트에 저장한다. 

    return alphas

print(find_string(inputs))