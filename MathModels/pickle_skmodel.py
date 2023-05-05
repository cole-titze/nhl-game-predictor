import pickle

filename = './SavedModel/finalized_model.sav'

def save(model):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

def load():
    with open(filename, 'rb') as file:
        return pickle.load(file)
