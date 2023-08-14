import time
from random import *
from RR import Tank, MegaTank
t1=Tank('T-34', 50, 50, 500, 1500)
t2=Tank('TIGER', 50, 50, 600, 1600)
t1.print()
t3=MegaTank('ffff', 50, 50, 1000, 1700)
t3.print()
while t1.health>0 and t2.health>0:
    ch=randint(1, 2)
    if ch==1:
        t1.shot(t3)
    if ch ==2:
        t3.shot(t1)
    time.sleep(2)
