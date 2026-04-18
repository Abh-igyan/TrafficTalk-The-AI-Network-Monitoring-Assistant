import redis
import time
import random

# Initializing Redis connection
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

INTERFACES = [f"eth{i}" for i in range(50)]

def initialize():
    """Wipes old data and sets a clean baseline."""
    print("Initializing baselines...")
    pipe = r.pipeline()
    for iface in INTERFACES:
        key = f"COUNTERS:{iface}"
        pipe.hset(key, mapping={
            "RX_BYTES": random.randint(1000, 5000),
            "TX_BYTES": random.randint(1000, 5000)
        })
    pipe.execute()

def simulate_traffic():
    """Uses atomic increments and pipelines for high performance."""
    while True:
        
        pipe = r.pipeline()
        
        for iface in INTERFACES:
            key = f"COUNTERS:{iface}"
            
            is_spike = random.random() > 0.90
            multiplier = 10 if is_spike else 1
            
            rx_increase = random.randint(50, 500) * multiplier
            tx_increase = random.randint(50, 500) * multiplier

            pipe.hincrby(key, "RX_BYTES", rx_increase)
            pipe.hincrby(key, "TX_BYTES", tx_increase)

        pipe.execute()
        print(f"Updated {len(INTERFACES)} interfaces...")
        time.sleep(1)

if __name__ == "__main__":
    try:
        initialize()
        print("Traffic simulation started. Press Ctrl+C to stop.")
        simulate_traffic()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")