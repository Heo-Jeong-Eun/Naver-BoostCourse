# Q4. 3번에서 진행한 함수를 포함한 클래스를 구현한다. 
# merge list를 이용해 리스트 내 데이터의 합을 출력한다. 
# 데이터를 합치기 전 데이터의 자료형을 변경한다. 
# output : csv 내부 데이터 

'''
import csv
import pandas as pd
import numpy as np

class ReadCSV():
  def __init__ (self, file):
    self.file = file
    self.data = pd.read_csv(file)

  def read_file(self, ):

  def merge_list(self, csvfile):

read_csv = ReadCSV('/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv')
print(read_csv.read_file())
print(read_csv.merge_list())
'''

# row merge
# error -> 0번째 행이 row title로 들어가서 sum X
import csv
import pandas as pd
import numpy as np

df = pd.read_csv('/content/drive/MyDrive/NaverBoostCourse/JeongEun/week 2/data-01-test-score.csv')
list(df.sum(axis='columns'))