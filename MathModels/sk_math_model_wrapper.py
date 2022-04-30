from sklearn.metrics import accuracy_score

class MathModel:
    prediction = None
    odds = None
    winner = None

    def __init__(self, x_training, y_training, x_testing, y_testing, modelAndName):
        self.math_model = modelAndName.model
        self.name = modelAndName.name
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
        print(self.name)
        print(self.prediction)
    
    def predict_single_game(test_game):
        self.odds = self.math_model.predict_proba(test_game)
        self.winner = self.math_model.predict(test_game)

    def print_single_game_odds():
        print(self.odds)
        print(self.winner)