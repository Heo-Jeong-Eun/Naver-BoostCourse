# Q2. string 문장을 받아 단어를 역순으로 출력하는 함수를 작성
# ouput : Where there is a will there is a way

# A. 
#   1. 공백 기준으로 나눠서 리스트에 저장 한 뒤 
#   2. 역순으로 정렬
#   3. 공백을 구분자로 다시 합친 뒤 출력한다. 

sentence = "way a is there will a is there Where"

def reverse_sentence(sentence): 
    rev_sentence = list(sentence.split(' ')) 
    # rev_sentence 변수에 list() 함수를 이용해 sentence 문자열을 리스트에 저장하는데, 
    # 이때 split()을 사용해 리스트에 저장할 때 기준, 즉 구분자를 추가한다.
    # 구분자를 공백으로 주어서 way, a, is, there, will, a, is, there, Where 
    # 다음과 같이 rev_sentence 리스트에 삽입 되도록 한다. 
    # return (rev_sentence) -> 이 부분 주석을 지우고 출력해보면 확인이 가능하다. 

    return ' '.join(reversed(rev_sentence))
    # 나누어진 문자열을 역순으로 정렬하는 reversed()함수로 rev_sentence를 감싸주고
    # join()을 통해 문자열을 결합한다. 
    # 이때 나누었던 결과를 바탕으로 결합이 가능하고, join의 . 앞에 공백으로 구분자를 추가해주면
    # 구분자를 기준으로 결합을 한다. 
    # join은 리스트, 튜플, 딕셔너리에서 사용이 가능하다. 

print(reverse_sentence(sentence)) 