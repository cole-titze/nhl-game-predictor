from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

class Model:
    def __init__(self, Name, Model):
        self.name = Name,
        self.model = Model

# best is (38,) with .62576
class MathModels:
    def __init__(self):
        self.models = []
        #knn = KNeighborsClassifier(n_neighbors=15)
        #kmeans = KMeans(n_clusters=2, random_state=42)
        #mlp = MLPClassifier(max_iter=1000, solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
        #rf = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
        mlpAiFinal = MLPClassifier(solver='adam', max_iter=300, activation='logistic', alpha=1e-4, hidden_layer_sizes=(44,))

        #self.models.append(Model("Knn", knn))
        #self.models.append(Model("Kmeans", kmeans))
        #self.models.append(Model("MLP", mlp))
        #self.models.append(Model("Random Forrest", rf))
        self.models.append(Model("MLP AI Final", mlpAiFinal))