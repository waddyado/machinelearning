from sklearn import tree

clf = tree.DecisionTreeClassifier()


#favoritenumber=x, type of roll=y

X = [[5], [3], [2], [2], [6],
     [1], [5],
     [7], [9], [4], [4]]

Y = ['california', 'volcano', 'saki', 'mexican', 'avocado', 'salmon', 'cucumber', 'dancing',
    'fire', 'krab', 'lobster']









clf = clf.fit(X, Y)


inp = input('Whats your favorite number? :>')

str(inp)

float(inp)

prediction = clf.predict(inp)



print('here is your recommended roll', prediction)
