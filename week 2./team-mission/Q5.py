# Q5. 이전에 구현한 클래스에서 merge_list의 함수 동작을 합계가 아닌 평균을 구하는 함수로 변경한다. 
# output : csv 내부 데이터 

# A. 
#   1. pandas 라이브러리의 mean()으로 평균값을 구하고 sorted로 오름차순 정렬 

import csv # 내장 모듈인 cvs를 import
import pandas as pd # 내장 모듈인 pandas를 import
from pprint import pprint # 각 요소를 한줄씩 출력, 리스트와 딕셔너리에 요소가 많을 경우 사용한다. 

class ReadCSV():
  def __init__ (self, file_path):
    self.file_path = file_path

  def merge_list(self): 
    df = pd.read_csv(self.file_path, header = None) 
    # pandas 모듈의 read_csv로 csv 파일을 읽어온다. 
    # 이때 csv 파일의 header에 값이 바로 주어지므로 header는 주어지지 않았다고 설정한다. 
    # header를 None으로 지정하지 않으면 index 0번째에 들어가야할 값이 header로 자동 지정되기 때문에 
    # 첫번째 출력값이 누락된다. 
    # return list(df.sum(axis='columns')) # col을 기준으로 sum, axis는 축을 의미한다. 
    return list(sorted(df.mean(axis='columns'))) 
    # col을 기준으로 mean, pandas에서 mean() 함수를 이용하면 평균값을 쉽게 구할 수 있다.
    # 평균값을 구하고 sorted로 오름차순 정렬, 이때 axis는 축을 의미한다. 

file_path = '/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv'
read_csv = ReadCSV(file_path) 
print(read_csv.merge_list())