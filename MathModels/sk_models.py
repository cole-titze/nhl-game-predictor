from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import StackingClassifier
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

class Model:
    def __init__(self, Name, Model):
        self.name = Name,
        self.model = Model

class MathModels:
    def __init__(self):
        self.models = []
        knn = KNeighborsClassifier(n_neighbors=150)
        mlp_test = MLPClassifier(solver='adam', max_iter=600, activation='relu', alpha=1e-5, hidden_layer_sizes=(32, 8))
        rf = RandomForestClassifier(n_estimators=200, criterion='entropy')
        mlp = MLPClassifier(solver='adam', max_iter=600, activation='logistic', alpha=1e-5, hidden_layer_sizes=(40,))
        svm_clf = svm.SVC(probability=True)
        kernel = 1.0 * RBF(1.0)
        guass = GaussianProcessClassifier(kernel=kernel)

        ensemble = VotingClassifier(estimators=[
            ("MLP", mlp_test), ("Best MLP", mlp)], voting='soft')

        # Add weights based on log loss or cross-val
        voting_all = VotingClassifier(estimators=[
            ("Knn", knn), ("MLP", mlp), ("rf", rf), ("svm", svm_clf), ("guass", guass)], voting='soft')

        pca_stacking = StackingClassifier(estimators=[
            ("Knn", knn), ("MLP", mlp), ("rf", rf), ("svm", svm_clf), ("guass", guass)])

        #self.models.append(Model("KNN", knn))
        #self.models.append(Model("SVM", svm_clf))
        #self.models.append(Model("RF", rf))
        #self.models.append(Model("MLP", mlp))
        #self.models.append(Model("MLP Testing", mlp_test))
        self.models.append(Model("Gaussian", guass))
        #self.models.append(Model("Ensemble", ensemble))
        #self.models.append(Model("Voting All", voting_all))
        #self.models.append(Model("Stacking PCA", pca_stacking))
