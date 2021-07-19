import pandas as pd

city=['서울','부산','인천','대구','대전','광주','수원']
population=[12524,31252,253523,3532523,52332,124314,4124412,41241,142124,4142]

data=pd.DataFrame()#빈 데이터 프레임 생성
data

data=pd.DataFrame(columns=['도시','인구수'],index=range(10))#행과 열 만들기
data

data_dict={'도시':city, '인구수':population}
data_dict
data=pd.DataFrame(data_dict)
data

data.to_csv("/content/drive/MyDrive/pandas/data02.csv",index=False)#index요소 안보
pd.read_csv("/content/drive/MyDrive/pandas/data02.csv")