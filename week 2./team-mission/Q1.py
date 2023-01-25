# Q1. 중간고사, 기말고사 점수를 따로 받아 저장하는 클래스 구현
# 생성자의 인스턴스는 private으로 선언되어야하며, 데코레이터를 이용해 데이터를 저장한다.
# output : 62.5

# A. 
#   1. 

class Score():
    # __mid = 0 # private variable, 외부에서 접근이 불가능하다. 
    # __final = 0

    def mid(self):
        return self.__mid

    def final(self):
        return self.__final

score = Score(50, 75)
print((score.mid + score.final) / 2)