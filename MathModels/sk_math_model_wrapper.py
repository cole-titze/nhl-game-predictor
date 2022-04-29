from sklearn.metrics import accuracy_score

class MathModel:
    prediction = None

    def __init__(self, x_training, y_training, x_testing, y_testing, modelAndName):
        self.math_model = model.model
        self.name = model.name
        self.x_train = x_training
        self.y_train = y_training
        self.x_test = x_testing
        self.y_test = y_testing

    def train(self):
        self.math_model.fit(self.x_train, self.y_train)

    def predict_results(self):
        y_prediction = self.math_model.predict(self.x_test)
        self.prediction = accuracy_score(self.y_test, y_prediction)
    
    def print_result(self):
        print(self.name)
        print(self.prediction)