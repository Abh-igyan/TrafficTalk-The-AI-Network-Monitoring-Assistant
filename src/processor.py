import time


def compute_rates(get_data, interval=10):
    t1=get_data()
    time.sleep(interval)
    t2=get_data()

    rates={}
    for x in t1:
        delta=max(0,t2[x]-t1[x])
        rates[x]=delta/interval
    return rates

def get_top_n(rate_dict, n=5):
    return sorted(rate_dict.items(),key=lambda x :x[1],reverse=True)[:n]
