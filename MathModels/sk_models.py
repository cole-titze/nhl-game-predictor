from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

class Model:
    def __init__(self, name, model):
        self.name = name,
        self.model = model

class MathModels:
    def __init__(self):
        self.models = []
        knn = KNeighborsClassifier(n_neighbors=150, n_jobs=-1)
        mlp_test = MLPClassifier(solver='adam', max_iter=600, activation='logistic', alpha=1e-5,
                                 hidden_layer_sizes=(64, 32, 16, 8))
        rf = RandomForestClassifier(n_estimators=600, criterion='entropy', n_jobs=-1)
        mlp = MLPClassifier(solver='adam', max_iter=600, activation='logistic', alpha=1e-5, hidden_layer_sizes=(40, 32, 16, 8))
        svm_clf = svm.SVC(probability=True)
        nb = GaussianNB()

        ensemble = VotingClassifier(estimators=[
            ("MLP", mlp), ("knn", knn)], voting='soft', n_jobs=-1)

        # Add weights based on log loss or cross-val
        voting_all = VotingClassifier(estimators=[
            ("MLP Test", mlp_test), ("Naive Bayes", nb)], voting='soft', n_jobs=-1)

        pca_stacking = StackingClassifier(estimators=[
            ("MLP Testing", mlp_test), ("Naive Bayes", nb)], n_jobs=-1)

        #self.models.append(Model("KNN", knn))
        #self.models.append(Model("SVM", svm_clf))
        #self.models.append(Model("RF", rf))
        #self.models.append(Model("MLP", mlp))
        self.models.append(Model("MLP Testing", mlp_test))
        #self.models.append(Model("Naive Bayes", nb))
        #self.models.append(Model("Ensemble", ensemble))
        #self.models.append(Model("Voting All", voting_all))
        #self.models.append(Model("Stacking PCA", pca_stacking))
