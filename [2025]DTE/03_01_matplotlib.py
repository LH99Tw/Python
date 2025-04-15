import matplotlib.pyplot as plt
X = range(100)
Y = range(100)
plt.plot(X, Y)

import numpy as np # numpy 모듈 호출
X_1 = range(100)
Y_1 = [np.cos(value) for value in X]
X_2 = range(100)
Y_2 = [np.sin(value) for value in X]
plt.plot(X_1, Y_1)
plt.plot(X_2, Y_2)
plt.show()

fig, ax = plt.subplots() # (1) figure와 axes 객체 할당

X_1 = range(100)
Y_1 = [np.cos(value) 
       for value in X]

ax.plot(X_1, Y_1) # (2) plot 함수를 사용하여 그래프 생성
ax.set(title='cos graph', # (3)그래프 제목,X축 라벨,Y축 라벨 설정
     xlabel='X', 
     ylabel='Y');

plt.show() # (4) 그래프 출력

fig = plt.figure()         # (1) figure 반환
fig.set_size_inches(10,10) # (2) figure의 크기 지정

ax_1 = fig.add_subplot(1,2,1) # (3) 첫 번째 그래프 생성
ax_2 = fig.add_subplot(1,2,2) # (4) 두 번째 그래프 생성

ax_1.plot(X_1, Y_1, c="b") # (5) 첫 번째 그래프 설정
ax_2.plot(X_2, Y_2, c="g") # (6) 두 번째 그래프 설정
plt.show()                 # (7) 그래프 출력

X_1 = range(100)
Y_1 = [value for value in X]

X_2 = range(100)
Y_2 = [value + 100 for value in X]

plt.plot(X_1, Y_1, color="#000000") 
plt.plot(X_2, Y_2, c="c")

plt.show()

plt.plot(X_1, Y_1, 
         color="b", 
         linestyle="dashed", 
         label='line_1')
plt.plot(X_2, Y_2, 
         color="r", 
         linestyle="dotted", 
         label='line_2')
plt.legend(
  shadow=True, 
  fancybox=False, 
  loc="upper right")

plt.title('$y = ax+b$')
plt.xlabel('$x_line$')
plt.ylabel('y_line')
plt.show()

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * ( 
       15 * np.random.rand(N))**2

plt.scatter(x, y, 
            s=area, c=colors, 
            alpha=0.5)
plt.show()
