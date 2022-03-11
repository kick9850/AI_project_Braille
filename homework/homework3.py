from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

x_train, x_test,y_train, y_test = train_test_split(iris.data, iris.target)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)

score=model.score(x_test,y_test)
print(score)