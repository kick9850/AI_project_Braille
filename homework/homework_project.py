from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


##데이터 불러오기
iris = load_iris()
print(iris.DESCR)

##데이터 정보 확인1
print(iris.data)
print(iris.feature_names)

##데이터 정보확인2
print(iris.target)
print(iris.target_names)

##feature_names 와 target을 레코드 닺는 데이터 프레임 생성
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

df['target'] = df['target'].map({0:"srtosa", 1:"versicolor", 2:"viginica"})
print(df)

#슬라이싱을 통해 feature와 label 분리
x_data = df.iloc[:, :-1]
y_data = df.iloc[:, [-1]]

#데이터 시각화1
sns.pairplot(df, hue="target", height=3)
plt.show()

#데이터 시각화2
sns.pairplot(df, x_vars=["sepal length (cm)"], y_vars=["sepal width (cm)"], hue="target", height=5)
plt.show()

#미세조정
x_train, x_test,y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=7)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)

score=model.score(x_test,y_test)
print(score)

#모델링 Decision Tree 사용하기
desision_tree = DecisionTreeClassifier(random_state=32)
print(desision_tree._estimator_type)

desision_tree.fit(x_train, y_train)
y_pred = desision_tree.predict(x_test)

print(classification_report(y_test, y_pred))

#모델링 random forest 사용하기
random_forest = RandomForestClassifier(random_state=32)
random_forest.fit(x_train,y_train)
y_pred = random_forest.predict(x_test)

print(classification_report(y_test,y_pred))

#모델링 svc 사용하기
svm_model = svm.SVC()
svm_model.fit(x_train, y_train)
y_pred = svm_model.predict(x_test)

print(classification_report(y_test, y_pred))