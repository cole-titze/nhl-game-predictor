import pickle

filename = './SavedModel/finalized_model.sav'

def save(model):
    pickle.dump(model, open(filename, 'wb'))

def load():
    return pickle.load(open(filename, 'rb'))
