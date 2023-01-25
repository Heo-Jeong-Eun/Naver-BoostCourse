# Q1. 중간고사, 기말고사 점수를 따로 받아 저장하는 클래스 구현
# 생성자의 인스턴스는 private으로 선언되어야하며, 데코레이터를 이용해 데이터를 저장한다.
# output : 62.5

# A. 
#   1. 인스턴스를 private, 즉 __mid, __final과 같은 형태로 선언 하고
#   2. @property 데코레이터를 활용 -> getter, setter를 구현해 데이터를 저장한다. 

#   접근 제어자 : 객체의 프로퍼티 접근을 제한하는 명령어
#   @property : 객체의 프로퍼티를 보호해주는 함수이다.
#   getter : 값을 가져오는 method, setter : 값을 저장하는 method
class Score:
    def __init__(self, __mid, __final):
        self.__mid = __mid
        self.__final = __final
        # __mid = 0 # private variable, 외부에서 접근이 불가능하다. 
        # __final = 0

    @property # 데코레이터 @property를 사용, 값을 읽을 때마다 getter/function을 따로 호출 X, property 이름으로 접근 O
    def mid(self): # self : 인스턴스 그 자체, 객체 자기 자신을 참조하는 매개변수
        return self.__mid
    @mid.setter # setter 선언 방법 : method 이름 + .setter
    def mid(self, value):
        self.__mid = value # self.__mid에 value 값 저장
    @property
    def final(self):
        return self.__final
    @final.setter
    def final(self, value):
        self.__final = value

score = Score(50, 75) 
print((score.mid + score.final) / 2) # 인스턴스.속성 형식으로 값을 가져온다. 