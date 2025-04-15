import seaborn as sns
import numpy as np              # numpy 모듈 호출
import pandas as pd             # pandas 모듈 호출
import matplotlib.pyplot as plt # matplotlib 모듈 호출
import seaborn as sns           # (1)seaborn 모듈 호출


tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips, x_ci=95)
plt.show()

tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", hue="time", data=tips)
plt.show()

sns.swarmplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted")
plt.show()


