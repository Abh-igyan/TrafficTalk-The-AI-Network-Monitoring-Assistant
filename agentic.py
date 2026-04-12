from db import get_counters
from processor import compute_rates, get_top_n
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")
if not key:
    print("❌ Error: GROQ_API_KEY not found in .env file!")
else:
    print(f"✅ Key loaded successfully: {key[:6]}...")

def format_dat(data):
    fd = "\n".join([f"{iface}: {rate:.2f} bytes/sec" for iface, rate in data])
    return fd

def agent(query, interval=5, top_n=5):
    query = query.lower()

    rates = compute_rates(get_counters, interval)
    top = get_top_n(rates, top_n)
    # Simple queries → no LLM
    if "top" in query:
        return f"Here are the top interfaces:\n{format_dat(top)}"

    # Complex queries → LLM
    return agent_with_llm(query, top)

client = Groq(api_key=key)


def agent_with_llm(query, data):
    fd = format_dat(data)
    prompt = f"""
    You are a network monitoring assistant.

    User query: {query}

    Here is the network traffic data (interface, bytes/sec):
    {fd}

    Tasks:
    1. Identify the most heavily loaded interface
    2. Compare it with others (relative difference)
    3. Mention if any interface looks significantly higher (possible hotspot)
    4. Give 1 practical suggestion (e.g., monitoring, load balancing)

    Keep the explanation clear and concise.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
