import pandas as pd

#파일과 데이터 프레임

data=pd.read_csv("/content/drive/MyDrive/pandas/대한민국_주요_도시_인구수.csv")
data

data.shape

data.info()#데이터 프레임의 요약 정보

data['도시']#특정 칼럼

data.도시