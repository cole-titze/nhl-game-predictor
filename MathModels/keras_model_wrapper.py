import numpy as np


class MathModel:
    prediction_titles = None
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

    # Best is 61.1%
    def predict_results(self):
        self.prediction_titles = self.math_model.metrics_names
        self.prediction = self.math_model.evaluate(self.x_test, self.y_test)

    def print_model_result(self):
        print(self.name)
        print(self.prediction_titles)
        print(self.prediction)

    def predict_single_game(self, test_game):
        self.odds = self.math_model.predict_proba(test_game)
        self.winner = self.math_model.predict(test_game)

    def print_single_game_odds(self):
        print(self.odds)
        print(self.winner)
