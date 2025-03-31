import numpy as np
import sys



'''
test_array = np.array([1, 4, 5, 8], float)
test_list = [[1, 4, 5, 8], [1, 4, 5]]
np.array(test_list, float) #Value Error
동적 타이핑을 지원하지 않음 ( 하나의 데이터 타입만 지원 )
각 값 메모리 크기가 동일, 검색/연산 속도가 리스트에 비해 빠름
텐서 구조에 따라 배열 생성 : 모든 구성요소에 값이 존재해야 함

float32 데이터 타입인 numpy 배열의 값을 저장하는 메모리 블록은 4바이트 씩 차지

'''
test_array = np.array([1, 4, 5, 8], float)
print(type(test_array[3])) # 개별 값 타입도 float64, 8바이트의 실수형 데이터
print(test_array.dtype) # 배열 전체의 데이터 타입 float64
print(test_array.shape) # 배열의 크기 (4,) 타입은 튜플

matrix = [[1,2,5,8], [1,2,5,8], [1,2,5,8]]
print(np.array(matrix, int).shape) # 3행 4열의 행렬 형태

tensor_rank3 = [
    [[1,2,5,8], [1,2,5,8], [1,2,5,8]],
    [[1,2,5,8], [1,2,5,8], [1,2,5,8]],
    [[1,2,5,8], [1,2,5,8], [1,2,5,8]],
    [[1,2,5,8], [1,2,5,8], [1,2,5,8]]
]
print(np.array(tensor_rank3, int).shape) # 3차원 텐서 형태 ( 4, 3, 4 )
print(np.array(tensor_rank3, int).ndim) # 차원 수 3
print(np.array(tensor_rank3, int).size) # 원소 수 48

# dtype
print(np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype = int)) # 명시적으로 데이터 타입 지정
print(np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype = float))
print(np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype = np.float64).itemsize) # 데이터 타입 크기 확인

x = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(x.shape)
print(x.reshape(-1, )) # 1차원 배열로 변환 = ( 8, )
print(x.reshape(4, 2)) # but, 반드시 전체 요소의 개수는 통일


#배열 생성
# 1. arange(시작, 마지막, 증가값) 실수형도 가능
# 2. ones, zeros, empty
print(np.ones(shape = (5,2), dtype = np.int8))
# 3. ones_like, zeros_like, empty_like
# 4. identity 단위행렬, eye 시작점과 행렬 크기를 지정한 단위행렬, diag 대각행렬 추출

# 통계 분석 함수
# 1. uniform 균일 분포 데이터 생성
print(np.random.uniform(0, 5, 10))
# 2. normal 정규 분포 데이터 생성
print(np.random.normal(0, 2, 10)) #평균값, 분산, 데이터 개수 

# 넘파이 배열 연산
# 1. 연산 함수(operating function) : 배열 내부의 연산을 지원하는 함수
    # axis : 축, 배열의 랭크가 증가할 때마다 새로운 축이 되어 차원 증가
test_array = np.arange(1, 11)
print(test_array.sum())
test_array = np.arange(1, 13).reshape(3, 4)
print(test_array.sum(axis = 0)) # 열 방향 합계 ( axis = 0 은 열 방향 합, 1은 행 방향 합)
thrid_order_tensor = np.array([
    [test_array], [test_array], [test_array]
])
print(thrid_order_tensor.sum(axis = 0)) # 3차원 텐서 연산
print(thrid_order_tensor.sum(axis = 1))
print(thrid_order_tensor.sum(axis = 2))

print(test_array.mean(axis = 1)) # 축을 기준으로 평균 계산

# 2. 연결 함수(concatenation function) : 배열 간 결합 지원
    # vstack 과 hstack
    # concatenate((배열1, 배열2), axis)

# 3. 사칙연산 함수
    # 1) 같은 구조일 때 사칙연산 가능
    # 2) 배열 간의 곱셈에서는 요소별 연산과 벡터의 내적(dot product) 연산 지원
        # m x n 행렬과 n x l 행렬을 내적하면 m x l 행렬 생성
x_1 = np.arange(1, 7).reshape(2, 3)
x_2 = np.arange(1, 7).reshape(3, 2)
print(x_1.dot(x_2)) # 벡터의 내적 연산
    # 3) 브로드캐스팅 연산(broadcasting operation) : 크기가 다른 배열 간 연산 지원
        # 방송국의 전파가 퍼지듯 스칼라 값을 모든 요소에 퍼트리듯 연산
x = np.arange(1, 10).reshape(3, 3)
print(x + 10)

# 4. 비교 연산과 데이터 추출
    # 연산 결과는 항상 boolean type을 가진 배열
x = np.array([4, 3, 2, 6, 8, 5])
print(x > 3)

x = np.array([1, 3, 0])
y = np.array([4, 3, -1])
print(x > y)
    # 1. all 과 any 함수
        # all : 모든 요소가 조건을 만족하는지 확인
        # any : 하나 이상의 요소가 조건을 만족하는지 확인
x = np.array([1, 4, 0])
print((x>3).all())
print((x>3).any())
    # 2. where 함수
        # 배열이 boolean type일 때 참인 값들의 인덱스 반환
x = np.array([4,6,7,3,2])
print(np.where(x > 3))
    # 3. argsort, argmax, argmin 함수
        # argsort : 정렬된 배열의 인덱스 반환
        # argmax : 최대값의 인덱스 반환
        # argmin : 최소값의 인덱스 반환
x = np.array([4,6,7,3,2])
print(np.argsort(x))
print(np.argmax(x))
print(np.argmin(x))
    # 4. 인덱스를 활용한 데이터 추출
        # boolean index : 특정 조건을 불린형의 배열에 넣어서 추출. ( 구조는 같아야 함 )
x = np.array([4,6,7,3,2])
cond = x > 3
print(x[cond])
        # fancy index : 인덱스를 배열로 지정하여 추출
cond = np.array([1, 2, 0 ,2, 2, 2, ], int)
print(x[cond])
        
