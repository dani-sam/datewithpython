# Lab 03 — Observability: Fundamentals

## Overview
A complete observability stack built on Docker Compose, monitoring host-level
metrics and container logs, with alerting on failure conditions. Built as a
progression from Lab 02 (Docker fundamentals), applying the same
containerization skills to a real monitoring pipeline.

Demonstrates the full observability loop: **metrics → visualization → logs →
alerting**.

## Stack

| Component     | Role                                      |
|----------------|-------------------------------------------|
| Prometheus     | Metrics collection, storage, alert rules  |
| Grafana        | Dashboards and log/metric visualization   |
| node_exporter  | Host-level metrics (CPU, memory, disk)    |
| Loki           | Log aggregation and storage               |
| Promtail       | Log shipping from Docker containers       |
| Alertmanager   | Alert routing on rule triggers            |

## Structure
```
fundamentals/
├── docker-compose.yml
├── prometheus/
│   ├── prometheus.yml
│   └── alert_rules.yml
├── grafana/
│   └── dashboards/
│       └── host-metrics.json
├── loki/
├── promtail/
│   └── promtail-config.yml
├── alertmanager/
│   └── alertmanager.yml
├── NOTES.md
└── README.md
```

## How to run
```bash
cd observability/fundamentals
docker compose up -d
```

Then visit:
- **Prometheus** — http://localhost:9090 (metrics + alert rule status)
- **Grafana** — http://localhost:3000 (default login: admin / admin)
- **Alertmanager** — http://localhost:9093 (fired alerts)
- **Loki** — queried via Grafana Explore, not a standalone UI

## What each phase demonstrates

**Phase 1 — Metrics foundation**
Prometheus scraping itself and node_exporter for real host metrics (CPU,
memory, disk). Confirmed via Prometheus's `/targets` page showing both jobs UP.

**Phase 2 — Visualization**
Grafana connected to Prometheus as a data source. Dashboard `Host Metrics —
node_exporter` with 3 panels: CPU idle rate, memory available, disk usage.
Exported to `grafana/dashboards/host-metrics.json` for version control.

**Phase 3 — Log aggregation**
Promtail auto-discovers all running Docker containers and ships their logs
to Loki. Logs queried and filtered per-container via Grafana Explore
(e.g. `{service_name="/prometheus"}`).

**Phase 4 — Alerting**
A `NodeExporterDown` alert rule fires if node_exporter becomes unreachable
for 30+ seconds. Full lifecycle manually verified:
`INACTIVE → PENDING → FIRING → INACTIVE`, confirmed in both Prometheus's
Alerts page and Alertmanager's UI.

## Key technical notes
- **`host.docker.internal` doesn't resolve on Linux Docker** — use Compose
  service names instead (e.g. `node-exporter:9100`, `prometheus:9090`),
  since containers share the same Compose network.
- **node_exporter needs host `/proc`, `/sys`, `/` mounted in** (read-only)
  to report real host metrics — without this it only sees its own
  container's minimal filesystem.
- **Docker volume/command changes require `--force-recreate`**, not just
  `restart`, to take effect.
- **Mount whole config directories, not single files**, when a service
  needs multiple related config files (e.g. Prometheus needs both
  `prometheus.yml` and `alert_rules.yml` visible).
- **Loki auto-generates a `service_name` label** from container names
  (with a leading slash, e.g. `/grafana`) — this is the label to filter on,
  not a custom relabeled one.

## Status
Phases 1-4 complete. Full observability loop working end-to-end.
