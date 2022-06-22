class Result:
    f_score = None
    log_loss = 1  # Worst possible
    model = None
    accuracy = None

    def print(self):
        print("log_loss: " + str(self.log_loss))
        print("f1_score: " + str(self.f_score))
        print("model: " + str(self.model.name))
        print("accuracy: " + str(self.accuracy))
