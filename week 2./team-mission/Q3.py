# Q3. 파일 입출력을 이용해 파일 데이터를 리스트로 출력한다. 
# 파일 입출력에 사용하는 open 함수를 이용해 csv 파일 내부의 데이터를 읽는다. 
# output : csv 내부 데이터 

# A. 
#   1. open()을 사용해 파일을 연 뒤, csv.reader()로 파일을 읽어온다.
#   2. print로 파일 출력, 이때 list로 한번 더 감싸주어야 하고, 각 행마다 출력한다. 

# 방법 1. 
# error -> 바깥 부분을 한번 더 list로 감싸야한다. 
import csv 
# 내장 모듈인 cvs를 import

with open('/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv') as csvfile:
# open()을 사용해 .csv 파일을 연다. 
# 경로 뒤에 "r", "w", ... 등 옵션을 지정할 수 있다. 
  reader = csv.reader(csvfile)
  # csv.reader를 사용해 csv 파일 읽기
  for row in reader: 
    # for문을 활용해 각 행마다 읽어오기
    # 구분자를 따로 두지 않아도 for문을 사용하기 때문에 한줄씩 출력이 된다. 
    # 이때 return 되는 각 row의 col들은 리스트이다. 
    print(row)

'''
# 방법 2. 
# error -> [] 밖 ,을 기준으로 \n or for문으로 한줄씩 출력을 해야한다. 
import csv

csvfile = open('/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv', "r")
reader = csv.reader(csvfile)

data = list(reader) 
# reader를 리스트로 변환 
# 파일 전체를 하나의 변수에 저장하는 것, 데이터를 다룰 때마다 파일을 불러오지 않아도 되기 때문에 편리하다.
print(data)
'''