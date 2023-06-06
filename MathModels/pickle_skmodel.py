import codecs
import pickle
import DataAccess.data_access as da

def save_model(model):
    model_data = codecs.encode(pickle.dumps(model), "base64").decode()
    da.store_model(model_data)


def load_model():
    data = da.get_model()
    return pickle.loads(codecs.decode(data.encode(), "base64"))
