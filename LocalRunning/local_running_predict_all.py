import GamePredictionTrigger.trigger as trigger
import json
import os

# Locally set secrets, when in azure these will already be set
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

set_local_environment()
trigger.predict_all_games()
