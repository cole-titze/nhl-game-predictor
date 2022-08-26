import GamePredictionTrigger.trigger as trigger
import time

t0 = time.time()
trigger.test()
t1 = time.time()
total = t1-t0
print(total)