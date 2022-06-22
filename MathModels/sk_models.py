from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

class Model:
    def __init__(self, Name, Model):
        self.name = Name,
        self.model = Model

# best is MLPClassifier(solver='adam', max_iter=300, activation='relu', alpha=1e-5, hidden_layer_sizes=(40,)) with .628
class MathModels:
    def __init__(self):
        self.models = []
        knn = KNeighborsClassifier(n_neighbors=15)
        # kmeans = KMeans(n_clusters=2, random_state=42)
        mlp = MLPClassifier(solver='adam', max_iter=300, activation='relu', alpha=1e-5, hidden_layer_sizes=(40,))
        rf = RandomForestClassifier(n_estimators=100, criterion='entropy')
        mlp_ai_final = MLPClassifier(solver='adam', max_iter=300, activation='logistic', alpha=1e-4, hidden_layer_sizes=(40,))

        self.models.append(Model("Knn", knn))
        # self.models.append(Model("Kmeans", kmeans))
        self.models.append(Model("MLP testing", mlp))
        self.models.append(Model("Random Forrest", rf))
        self.models.append(Model("Best MLP Input Layer Match Attributes", mlp_ai_final))
