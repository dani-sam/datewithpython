# Lab 03 — Observability: Fundamentals

## Session 1 — [05/07/2026]

### Goal
Stand up Prometheus + Grafana via Docker Compose, confirm basic scraping works
before wiring in real metrics from Lab 01 (Containerlab FRR routers).

### What I did
- Created `observability/fundamentals/` as a new top-level category, sibling
  to `automation/` and `docker/`
- Added `docker-compose.yml` with Prometheus + Grafana services
- Added `prometheus/prometheus.yml` with a self-scrape job as a smoke test

### What I learned
- (fill in once you run it — e.g. what the targets page showed, any gotchas)

### Next
- Confirm Prometheus self-scrape target is UP at localhost:9090/targets
- Decide: node_exporter (host metrics) vs frr-exporter (routing metrics) first
- Add Grafana data source pointing to Prometheus

## Session 2 — [05/07/2026]

### What I did
- Confirmed Prometheus self-scrape target is UP at localhost:9090/targets
- Verified 1/1 targets healthy, 15s scrape interval working as configured

### Next
- Add node_exporter to expose host metrics
- Point Prometheus at node_exporter target
- Connect Grafana to Prometheus as a data source
