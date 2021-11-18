import graphviz
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing, tree


if __name__ == '__main__':
    titanic_train = pd.read_csv(
        filepath_or_buffer='./data/train.csv',
        dtype={
            'Sex': 'category',
            'Survived': 'category',
            'Embarked': 'category'
        }
    )
    sns.relplot(
        kind='scatter',
        data=titanic_train,
        x='Age',
        y='Fare',
        hue='Survived'
    )
    plt.title('Scatter')
    plt.show()

    titanic_train.dropna(inplace=True)
    y = titanic_train['Survived']
    sex_encoder = preprocessing.LabelEncoder()
    embarked_encoder = preprocessing.LabelEncoder()
    x = titanic_train[['Pclass','Age', 'Fare']]
    x['Sex'] = sex_encoder.fit_transform(titanic_train['Sex'])
    x['Embarked'] = embarked_encoder.fit_transform(titanic_train['Embarked'])

    classifier = tree.DecisionTreeClassifier(max_depth=3)
    classifier.fit(x,y)
    # tree.plot_tree(classifier)
    # plt.show()
    dot_data = tree.export_graphviz(classifier)
    graph = graphviz.Source(dot_data)
    graph.render("Classifier")
