from db import get_counters
from processor import compute_rates, get_top_n

def agent(query, interval=5, top_n=5):
    query = query.lower()

    rates = compute_rates(get_counters, interval)
    top = get_top_n(rates, top_n)
    return agent_with_llm(query,top)


from openai import OpenAI
client = OpenAI(api_key="your-api-key")

def agent_with_llm(query, data):
    prompt = f"""
    NETWORK DATA (Top {len(data)} active interfaces):
    User query: {query}
    Data: {data}
    Explain insights in simple terms.
    """
    response = client.chat.completions.create(
        model="gpt-4-turbo", # or gemini-1.5-pro
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content