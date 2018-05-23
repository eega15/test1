### test1_now.py ###
### 10523

###
import datetime

###
def _nowString():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
###
print( _nowString() )
print( _nowString()[:17] )
