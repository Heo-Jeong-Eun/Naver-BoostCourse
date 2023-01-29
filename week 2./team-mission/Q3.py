# Q3. 파일 입출력을 이용해 파일 데이터를 리스트로 출력한다. 
# 파일 입출력에 사용하는 open 함수를 이용해 csv 파일 내부의 데이터를 읽는다. 
# output : csv 내부 데이터 

# A. 
#   1. open()을 사용해 파일을 연 뒤, csv.reader()로 파일을 읽어온다.
#   2. print로 파일 출력, 이때 list로 한번 더 감싸주어야 하고, 각 행마다 출력한다. 

import csv # 내장 모듈인 cvs를 import
from pprint import pprint # 각 요소를 한줄씩 출력, 리스트와 딕셔너리에 요소가 많을 경우 사용한다. 

def read_file(file_path):
  file_path = open(file_path, "r")
  # open()을 사용해 .csv 파일을 연다. 
  # 경로 뒤에 "r", "w", ... 등 옵션을 지정할 수 있다. 
  reader = csv.reader(file_path) 
  # csv.reader를 사용해 csv 파일 읽기
  # 파일 전체를 하나의 변수에 저장하는 것, 데이터를 다룰 때마다 파일을 불러오지 않아도 되기 때문에 편리하다.
  return reader

file_path = '/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv'
pprint(list(read_file(file_path)))