import GamePredictionTrigger.trigger as trigger
import time
import json
import os

def set_local_environment():
    try:
        with open("local.settings.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        os.environ["SQL_DATABASE"] = jsonObject["Values"]["SQL_DATABASE"]
        os.environ["SQL_USERNAME"] = jsonObject["Values"]["SQL_USERNAME"]
        os.environ["SQL_PASSWORD"] = jsonObject["Values"]["SQL_PASSWORD"]
    except Exception:
        pass

t0 = time.time()
set_local_environment()
trigger.tune()
t1 = time.time()
total = t1-t0
print(total)