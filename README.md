# 🚀 Real-Time Data Streaming Pipeline

## 📌 Overview

This project demonstrates a simple real-time data streaming pipeline built using:

- Python (Producer & Consumer)
- Apache Kafka (Message Broker)
- PostgreSQL (Database)
- Docker & Docker Compose (Infrastructure)

The pipeline simulates streaming data, processes it in real-time, and stores it in a relational database.

---

## 🏗 Architecture

Producer → Kafka → Consumer → PostgreSQL

---

## 🧩 Components

| Component    | Role |
|-------------|------|
| Producer    | Generates and sends streaming data to Kafka |
| Kafka       | Message broker that buffers and distributes data |
| Consumer    | Reads data from Kafka and processes it |
| PostgreSQL  | Stores processed data |
| Docker      | Runs services in isolated containers |

---

## 🔄 Data Flow

1. Producer generates JSON messages  
2. Messages are sent to a Kafka topic  
3. Consumer subscribes to the topic  
4. Consumer writes data into PostgreSQL  

---

## 🐳 Infrastructure Setup (Docker)

Start all services:

```bash
docker compose up -d


