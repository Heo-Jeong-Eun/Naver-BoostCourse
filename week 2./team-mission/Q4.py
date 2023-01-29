# Q4. 3번에서 진행한 함수를 포함한 클래스를 구현한다. 
# merge list를 이용해 리스트 내 데이터의 합을 출력한다. 
# 데이터를 합치기 전 데이터의 자료형을 변경한다. 
# output : csv 내부 데이터 

# A. 
#   1. file_path에 csv 파일 경로를 지정, open으로 파일을 열고, csv.reader로 파일을 읽어 reader에 저장한다. 
#   2. merge_list에는 col을 기준으로 변수를 더한 값을 리스트에 저장 후 출력한다. 

import csv # 내장 모듈인 cvs를 import
import pandas as pd # 내장 모듈인 pandas를 import
from pprint import pprint # 각 요소를 한줄씩 출력, 리스트와 딕셔너리에 요소가 많을 경우 사용한다. 

class ReadCSV():
  def __init__ (self, file_path):
    self.file_path = file_path

  def read_file(self):
    file_path = open(self.file_path, "r")
    # open()을 사용해 .csv 파일을 연다. 
    # 경로 뒤에 "r", "w", ... 등 옵션을 지정할 수 있다. 
    reader = csv.reader(file_path) 
    # csv.reader를 사용해 csv 파일 읽기
    # 파일 전체를 하나의 변수에 저장하는 것, 데이터를 다룰 때마다 파일을 불러오지 않아도 되기 때문에 편리하다.
    return reader

  def merge_list(self): 
    df = pd.read_csv(self.file_path, header = None) 
    # pandas 모듈의 read_csv로 csv 파일을 읽어온다. 
    # 이때 csv 파일의 header에 값이 바로 주어지므로 header는 주어지지 않았다고 설정한다. 
    # header를 None으로 지정하지 않으면 index 0번째에 들어가야할 값이 header로 자동 지정되기 때문에 
    # 첫번째 출력값이 누락된다. 
    return list(df.sum(axis='columns')) # col을 기준으로 sum, axis는 축을 의미한다. 

file_path = '/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv'
read_csv = ReadCSV(file_path) 
pprint(list(read_csv.read_file())) # pprint로 각 요소마다 출력
print() # 공백 출력
print(read_csv.merge_list())