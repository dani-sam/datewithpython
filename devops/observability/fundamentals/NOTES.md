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

## Session 6 — [07/07/2026]

### What I did
- Added Alertmanager service to docker-compose.yml
- Created alertmanager/alertmanager.yml with a minimal default receiver
- Created prometheus/alert_rules.yml with NodeExporterDown rule
  (fires if up{job="node_exporter"} == 0 for 30s)
- Fixed prometheus volume mount to mount the whole prometheus/ folder
  instead of just prometheus.yml, so alert_rules.yml is visible too
- Triggered the alert manually by stopping node-exporter — confirmed
  full pipeline: INACTIVE -> PENDING -> FIRING in Prometheus UI
- Confirmed alert appeared in Alertmanager UI (localhost:9093)

### What I learned
- Docker volume mounts are file-specific unless you mount the whole
  directory — mounting just prometheus.yml hid alert_rules.yml from
  the container even though it existed on the host
- Alert states go INACTIVE -> PENDING -> FIRING, with PENDING lasting
  as long as the `for:` duration in the rule

### Status
Phase 4 (Alerting) — core alert pipeline confirmed working end-to-end.

### Next
- Add a second alert rule (e.g. disk space threshold, high CPU sustained)
- Consider a real notification channel (webhook/email) instead of
  Alertmanager's default no-op receiver
- Phase 5: wrap-up docs, final README polish, review full lab

## Session 7 — [09/07/2026]

### What I did
- Rewrote README.md to reflect the full stack as actually built:
  Prometheus, Grafana, node_exporter, Loki, Promtail, Alertmanager
- Documented all 4 phases with what each one demonstrates
- Captured key technical fixes as permanent reference notes (Docker
  networking, volume mounts, service naming)

### Status
Phase 5 (Wrap-up) complete.

---

## Lab 03 Summary

Built a complete observability stack from scratch on Docker Compose:

1. **Metrics** — Prometheus + node_exporter, scraping real host CPU/memory/disk
2. **Visualization** — Grafana dashboard with 3 panels, version-controlled as JSON
3. **Logs** — Loki + Promtail, auto-discovering and shipping all container logs
4. **Alerting** — Alertmanager + a rule that fires and resolves correctly,
   full lifecycle manually verified end-to-end

### Biggest lessons from this lab
- Docker networking on Linux differs from Docker Desktop conventions
  (no host.docker.internal) — always use Compose service names
- node_exporter needs explicit host filesystem mounts to see real system
  data, not just its own container
- Config-heavy services (Prometheus) need their whole config directory
  mounted, not individual files, when multiple config files reference
  each other
- The INACTIVE -> PENDING -> FIRING -> INACTIVE alert lifecycle is the
  core mental model for how Prometheus alerting actually behaves

### Next
- Observability lab complete as a learning milestone
- Future direction: either a second observability lab (deeper alerting,
  more rules, real notification channels) or move toward the next skill
  area (MLOps/AI integration as a thin layer on top of this stack)
- College project: revisit "AI-Assisted Observability and Incident
  Analysis for Containerized Infrastructure" framing, now that the
  underlying stack actually exists to build on
