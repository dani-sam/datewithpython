# Lab 03 — Observability: Fundamentals

## Overview
This lab sets up an observability stack (Prometheus, Grafana, and later
Loki/Promtail) for monitoring the Containerlab FRR environment built in
Lab 01. Goal: move from manual `health_check.py` runs to continuous
metrics, dashboards, and log aggregation.

## Stack
- **Prometheus** — metrics collection and storage
- **Grafana** — dashboards and visualization
- **Loki** (planned) — log aggregation
- **Promtail** (planned) — log shipping to Loki

## Structure
```
fundamentals/
├── docker-compose.yml
├── prometheus/
│   └── prometheus.yml
├── grafana/
│   ├── dashboards/
│   └── provisioning/
├── NOTES.md
└── README.md
```
## How to run
```bash
cd observability/fundamentals
docker compose up -d
```

Then visit:
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (default login: admin / admin)

## Phases
1. Metrics foundation — Prometheus scraping self + lab hosts
2. Visualization — Grafana dashboard for router/host stats
3. Log aggregation — Loki + Promtail
4. Alerting — Alertmanager on a meaningful rule
5. Wrap-up — docs, notes, commit history

## Status
Phase 1 in progress.
