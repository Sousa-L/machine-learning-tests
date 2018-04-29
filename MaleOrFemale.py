from sklearn import tree
#[Altura, Peso, Tamanho do sapato]
X = [[180, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37],
    [171, 75, 42], [181, 85, 43], [154, 43, 35], [175, 73, 42]]

Y = ['Homem', 'Mulher', 'Mulher', 'Mulher', 'Homem', 'Homem',
    'Homem', 'Mulher', 'Homem', 'Mulher', 'Homem', 'Mulher', 'Homem']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

height = raw_input("Qual sua altura? ")
weight = raw_input("Qual seu peso? ")
shoes = raw_input("Qual tamanho do seu sapato? ")

prediction = clf.predict([[height, weight, shoes]])

print prediction
