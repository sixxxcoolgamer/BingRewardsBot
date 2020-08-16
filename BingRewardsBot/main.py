import time
from firefox import ffdriver
from edge import edgedriver
from mobile import mobiledriver
from config import disable_pc, disable_edge, disable_mobile

print("\n>>> Program Start")
start_time = time.time()

if not disable_pc:
    ffdriver()
if not disable_mobile:
    mobiledriver()
if not disable_edge:
    edgedriver()


print(">>> Program Finished in " + str(round((time.time() - start_time),3)) + "s")
