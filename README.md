# 🚀 AI Network Traffic Analyzer

A modular system to monitor and analyze network interface traffic using Redis-based counters and delta-based rate computation. Inspired by SONiC's COUNTERS_DB architecture.

---

## 📌 Features

- 🔍 Identify **Top-N interfaces** by traffic (RX + TX)
- ⏱️ Configurable **sampling interval**
- 📊 Delta-based **real-time traffic rate computation**
- 🤖 Agent-like query interface (natural language queries)
- 🧩 Modular architecture (easy to extend)
- 🧪 Traffic simulation support for testing

---

## 🧠 How It Works

1. Interface counters (RX/TX bytes) are stored in Redis
2. System samples counters at two time intervals
3. Computes traffic rate using:
 Rate = (Counter₂ - Counter₁) / Δt
4. Sorts interfaces by throughput
5. Returns top-N results or answers user queries

---

## 🏗️ Project Structure

├── db.py # Redis connection & counter retrieval
├── processor.py # Rate computation & sorting logic
├── agentic.py # Query handling (agent layer)
├── main.py # CLI entry point
├── data_generator.py # Simulates traffic (optional)
├── requirements.txt
└── README.md
