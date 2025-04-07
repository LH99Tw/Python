import numpy as np
import pandas as pd
# 파이썬 데이터 분석 라이브러리

#DataFrame : 데이터 테이블 전체 객체
#Series : 데이터 테이블의 각 열 데이터 객체
    # 피쳐 벡터 (feature vector) 와 같은 개념. data/index/dtype 속성 존재
    
from pandas import Series, DataFrame

list_data = [1, 2, 3, 4, 5]
list_name = ["a", "b", "c", "d", "e"]
example_obj = Series(data=list_data, index=list_name)
print(example_obj)

print(example_obj.index)
print(example_obj.values)
print(example_obj.dtype)

# 시리즈 객체는 이름을 변경할 수 있다.
example_obj.name = "시리즈 예제"
example_obj.index.name = "인덱스"
print(example_obj)

# 시리즈 객체 생성
dict_data = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5
}
example_obj2 = Series(dict_data, dtype=np.float32, name="시리즈 예제2")
print(example_obj2)


dict_data_1 = {"a":1, "b":2, "c":3, "d":4, "e":5}
indexes = ["a","b","c","d","e","f","g","h"]
series_obj_1 = Series(dict_data_1, index=indexes)
print(series_obj_1)

# 데이터 프레임 생성
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data' 
# 데이터 URL을 변수 data_url에 넣기
df_data = pd.read_csv(data_url, sep='\s+', header = None) # csv 데이터 로드
df = pd.DataFrame(df_data)
print(df)

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
'age': [42, 52, 36, 24, 73], 
'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
print(df)

# 그룹 별 집계

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings','kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)

print(df.groupby("Team")["Points"].sum())


# 멀티 인덱스 그룹별 집계
multi_groupby = df.groupby(["Team", "Year"])["Points"].sum()
print(multi_groupby)


print(multi_groupby["Devils":"Kings"])
print(multi_groupby.unstack())

grouped = df.groupby("Team")
print(grouped.get_group("Riders")) # 키 값을 기준으로 분할된 DF 객체 
print(grouped.agg(np.mean)) # 집계 함수 적용

print(grouped.transform(max)) # 정보 변환

score = lambda x: (x - x.mean()) / x.std()
print(grouped.transform(score))

# 병합과 연결

raw_data = {
'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
'test_score': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

df_left = pd.DataFrame(raw_data, columns = ['subject_id', 'test_score'])

raw_data = {
            'subject_id': ['4', '5', '6', '7', '8'],
            'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
            'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

df_right = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

print(pd.merge(left=df_left, right=df_right, how="inner", on='subject_id'))
