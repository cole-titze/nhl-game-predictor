from sklearn.metrics import accuracy_score

class MathModel:
    prediction = None
    odds = None
    winner = None

    def __init__(self, x_training, y_training, x_testing, y_testing, model_and_name):
        self.math_model = model_and_name.model
        self.name = model_and_name.name
        self.x_train = x_training
        self.y_train = y_training
        self.x_test = x_testing
        self.y_test = y_testing

    def train(self):
        self.math_model.fit(self.x_train, self.y_train)

    def predict_results(self):
        y_prediction = self.math_model.predict(self.x_test)
        self.prediction = accuracy_score(self.y_test, y_prediction)
    
    def print_model_result(self):
        print(self.prediction)
    
    def predict_single_game(self, test_game):
        self.odds = self.math_model.predict_proba(test_game)
        self.winner = self.math_model.predict(test_game)

    def partial_fit(self, X, y):
        self.math_model.partial_fit(X, y)

    def print_single_game_odds(self):
        print(self.odds)
        print(self.winner)

    def get_accuracy(self):
        return self.prediction
