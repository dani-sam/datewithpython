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

## Session 3 — [05/07/2026]

### What I did
- Added node-exporter service to docker-compose.yml
- Fixed prometheus.yml to scrape node-exporter via service name (not host.docker.internal, which only works on Docker Desktop, not Linux)
- Confirmed both node_exporter and prometheus targets showing 1/1 UP

### What I learned
- host.docker.internal doesn't resolve on Linux Docker — use the Compose service name instead, since containers share the same network

### Next
- Connect Grafana to Prometheus as a data source
- Build first dashboard using node_exporter metrics (CPU, memory, disk)

## Session 4 — [05/07/2026]

### What I did
- Fixed node-exporter to expose real host metrics by mounting /proc, /sys,
  and / (as /rootfs) into the container, with matching --path.* flags
  and a filesystem mount-point exclusion filter
- Confirmed node_exporter target UP in Prometheus after force-recreate
- Connected Grafana to Prometheus as a data source (http://prometheus:9090)
- Built and saved dashboard "Host Metrics — node_exporter" with 3 panels:
  - CPU Idle Rate: rate(node_cpu_seconds_total{mode="idle"}[5m])
  - Memory Available: node_memory_MemAvailable_bytes
  - Disk Usage: node_filesystem_avail_bytes{mountpoint="/"}
- Exported dashboard JSON to grafana/dashboards/host-metrics.json for
  version control

### What I learned
- host.docker.internal doesn't resolve on Linux Docker — use Compose
  service names instead (containers share the same network)
- node_exporter needs host /proc, /sys, / mounted in as read-only volumes
  to report real host metrics; without this it only sees its own
  container's minimal filesystem
- Docker Compose volume/command changes require --force-recreate, not
  just restart, to take effect

### Status
Phase 2 (Visualization) complete.

### Next
- Phase 3: Loki + Promtail for log aggregation
- Ship logs from health_check.py and containers into Loki
- Correlate a log spike with a metric spike in Grafana Explore

## Session 5 — [07/07/2026]

### What I did
- Added Loki + Promtail services to docker-compose.yml
- Created promtail-config.yml with Docker service discovery
- Connected Loki as a Grafana data source (http://loki:3100)
- Confirmed logs flowing via Explore — query {service_name=~".+"}
  showed 237 log lines from grafana container alone

### What I learned
- Loki auto-generates a `service_name` label from container names
  (with leading slash, e.g. "/grafana"), not the custom `container`
  label from my relabel_configs — use service_name for now
- Logs volume panel breaks down by level (error/info/warning) automatically

### Status
Phase 3 (Log aggregation) — basic Docker log shipping confirmed working.

### Next
- Try scoping a query to a single container, e.g. {service_name="/prometheus"}
- Ship logs from health_check.py (Lab 01) into Loki too
- Move to Phase 4: Alertmanager for actual alert rules
