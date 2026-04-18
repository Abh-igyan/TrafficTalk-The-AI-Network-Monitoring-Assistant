import redis

r=redis.Redis(host='localhost',port=6379,decode_responses=True)

def get_counters():
    keys=r.keys("COUNTERS:*")
    data={}
    for x in keys:
        val=r.hgetall(x)
        rx=int(val.get("RX_BYTES",0))
        tx=int(val.get("TX_BYTES",0))
        data[x]=rx+tx
    return data
