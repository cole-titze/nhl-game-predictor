from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import StackingClassifier


class Model:
    def __init__(self, Name, Model):
        self.name = Name,
        self.model = Model

class MathModels:
    def __init__(self):
        self.models = []
        knn = KNeighborsClassifier(n_neighbors=150)
        mlp = MLPClassifier(solver='adam', max_iter=600, activation='relu', alpha=1e-5, hidden_layer_sizes=(8,))
        rf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        mlp_ai_final = MLPClassifier(solver='adam', max_iter=600, activation='logistic', alpha=1e-5, hidden_layer_sizes=(8,))

        # Look into estimators_ with already fitted models (pick best models)
        ensemble = VotingClassifier(estimators=[
            ("Random Forrest", rf), ("Best MLP Input Layer Match Attributes", mlp_ai_final)],
            voting='soft')

        # Add weights based on log loss or cross-val
        pca_ensemble_soft = VotingClassifier(estimators=[
            ("Knn", knn), ("MLP", mlp), ("MLPFinal", mlp_ai_final)],
            voting='soft')

        pca_stacking = StackingClassifier(estimators=[
            ("Knn", knn), ("MLP", mlp), ("MLPFinal", mlp_ai_final)])



        self.models.append(Model("Knn", knn))
        self.models.append(Model("MLP testing", mlp))
        self.models.append(Model("Random Forrest", rf))
        self.models.append(Model("Best MLP Input Layer Match Attributes", mlp_ai_final))
        self.models.append(Model("Ensemble", ensemble))
        self.models.append(Model("Ensemble PCA Soft", pca_ensemble_soft))
        self.models.append(Model("Stacking PCA", pca_stacking))
