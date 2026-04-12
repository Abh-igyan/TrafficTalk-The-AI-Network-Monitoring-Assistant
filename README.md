# 🚀 AI Network Traffic Analyzer

> Real-time network interface monitoring powered by Redis and LLM-based insights.  
> Inspired by SONiC's COUNTERS_DB architecture used in production at Microsoft, Google, and Meta.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Redis](https://img.shields.io/badge/Redis-7.0+-red)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA3-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📸 Demo

[![Demo GIF](Untitled%20design.gif)]

---

## 📌 Features

| Feature | Description |
|---|---|
| 🔍 Top-N Interfaces | Identifies highest-traffic interfaces by RX + TX |
| ⏱️ Configurable Interval | Custom sampling window for rate computation |
| 📊 Delta-based Rates | Real-time throughput using counter deltas |
| 🤖 Hybrid Agent | Rule-based for speed, LLM for deep insights |
| 🧩 Modular Design | Clean separation of concerns, easy to extend |
| 🧪 Traffic Simulation | Built-in generator for local testing |

---

## 🧠 How It Works

```
Redis COUNTERS_DB
       │
       ▼
Sample counters at T₁
       │
    wait Δt
       │
       ▼
Sample counters at T₂
       │
       ▼
Rate = (Counter₂ - Counter₁) / Δt
       │
       ▼
Sort by total throughput
       │
       ▼
Top-N Results → Agent Layer → CLI Output
```

---

## 🏗️ Architecture

```
User Query
    │
    ▼
Agent Layer (agentic.py)
    │
    ├── Simple query → Rule-based response ⚡
    │
    └── Complex query → Groq LLaMA 3.3-70B 🧠
                              │
                              ▼
               Traffic Processor (processor.py)
                              │
                              ▼
                   Redis COUNTERS_DB (db.py)
```

---

## 📂 Project Structure

```
.
├── db.py               # Redis connection & counter retrieval
├── processor.py        # Delta computation & top-N sorting
├── agentic.py          # Hybrid agent (rule-based + LLM)
├── main.py             # CLI entry point
├── data_generator.py   # Simulates real-time network traffic
├── .env                # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Abh-igyan/ai-network-analyzer.git
cd ai-network-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Redis
```bash
docker run -d -p 6379:6379 redis
```

### 4. Configure environment
```bash
# Create .env file
echo "GROQ_API_KEY=your_api_key_here" > .env
```

> ⚠️ Make sure `.env` is listed in `.gitignore` — never commit API keys.

### 5. Simulate traffic (optional)
```bash
python data_generator.py
```

---

## ▶️ Usage

```bash
# Top interfaces (default: top 5, interval 1s)
python main.py --query "top interfaces"

# Natural language queries
python main.py --query "which interfaces are overloaded?"
python main.py --query "analyze traffic pattern"

# Custom parameters
python main.py --interval 5 --top 3
```

---

## 📊 Sample Output

### CLI Output
```
Top interfaces by traffic:
─────────────────────────────────────────────────
  #   Interface      RX rate        TX rate        Total
─────────────────────────────────────────────────
  1   eth27          1544.00 B/s    1333.00 B/s    2877.00 B/s
  2   eth12          1200.00 B/s    1200.00 B/s    2400.00 B/s
  3   eth32          1100.00 B/s    1000.00 B/s    2100.00 B/s
─────────────────────────────────────────────────
```

### LLM Insight
```
eth27 is the most heavily utilized interface, with throughput significantly
above others. This indicates a potential traffic hotspot — monitoring or
load balancing may be required.
```

---

## 🤖 Agent Design

```
Query received
     │
     ├── Matches known pattern? → Rule-based response  ⚡ (fast, no API call)
     │
     └── Complex / ambiguous?  → Groq LLaMA 3.3-70B   🧠 (deep reasoning)
```

**Supported queries:**
- `"top interfaces"`
- `"which interfaces are overloaded?"`
- `"analyze traffic pattern"`

---

## 🧠 Tech Stack

- **Python 3.8+**
- **Redis** — counter storage (mirrors SONiC COUNTERS_DB)
- **Docker** — containerized Redis setup
- **Groq API** — LLaMA 3.3-70B for natural language insights
- **python-dotenv** — secure API key management

---

## 🚀 Roadmap

- [ ] JSON output for automation pipelines
- [ ] REST API via FastAPI
- [ ] Web dashboard with live graphs
- [ ] Anomaly detection on traffic spikes
- [ ] Direct integration with real SONiC COUNTERS_DB

---

## 🎯 Key Highlights

- **Delta-based computation** — accurate real-time rates, not stale snapshots
- **Hybrid AI design** — LLM used only when needed, keeping latency low
- **SONiC-inspired** — mirrors production-grade network OS architecture
- **Clean modularity** — each layer independently testable and replaceable

---

## 👨‍💻 Author

**Abhigyan Tiwari**  
B.Tech CSE, NIT Silchar  
[![GitHub](https://img.shields.io/badge/GitHub-Abh--igyan-black)](https://github.com/Abh-igyan)

---

## ⭐ Contributing

Contributions welcome — fork the repo, open issues, or submit pull requests!
