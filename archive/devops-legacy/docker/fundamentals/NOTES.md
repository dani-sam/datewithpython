# Docker Fundamentals

**Date:** 2026-06-27
**Goal:** Build real Docker fundamentals from scratch — Dockerfile, networking, Compose

## Session 1

### Environment
- Docker 29.6.1
- Docker Compose v5.2.0
- OS: Ubuntu (ProBook)

### Plan
- [x] Write first Dockerfile (Python script)
- [x] Build and run image, understand layers
- [x] Docker networking basics
- [x] Docker Compose — multi-container setup
- [x] Volumes — persistent data

### Notes
### What I did

- Wrote first Dockerfile from scratch
- Fixed WORKDIR (host path → /usr/local/app)
- Fixed COPY (script.py → .)
- Built image: `docker build -t sys-info .`
- Ran from a different directory — worked fine, image is stored in Docker not filesystem

### Key observations

**Container OS vs host OS**
- Output showed Linux 7.0.0-27-generic, not Ubuntu
- Container runs its own isolated OS layer
- `platform.system()` returns the container's OS, not the host

**Image layers (`docker image history sys-info`)**
- Every Dockerfile instruction = one layer
- Top 3 layers = mine (CMD, COPY, WORKDIR) — tiny, created minutes ago
- All layers below = inherited from python:3.14 base (~1GB, Debian + Python)
- Layers are cached — unchanged layers don't rebuild
- Instruction order matters: put stable things at top, changing things at bottom
- COPY is correctly at the bottom (changes most often)

### Docker Networking

**Default networks**
- bridge — default, containers isolated from host but can talk to each other
- host — container shares host network directly, no isolation
- none — no networking

**Bridge network**
- Subnet: 172.17.0.0/16, Gateway: 172.17.0.1
- Virtual interface: docker0 on host
- Containers get IPs automatically starting from 172.17.0.2

**Experiment**
- Ran nginx as webserver: got 172.17.0.2
- Ran alpine container, pinged 172.17.0.2 → 0% packet loss
- Two containers communicating over bridge network
- sys-info container showed empty in bridge inspect — exits immediately, no long-running process

**Key insight**
- Same concept as physical/virtual networking — just docker-managed
- Containers on same bridge can reach each other by IP
- Isolated from host by default

### Docker Compose

**What it is**
- Define and run multiple containers with a single file
- No need to install services locally — Docker pulls images automatically

**docker-compose.yml structure**
- `services:` — define each container
- `build: .` — build from local Dockerfile
- `image:` — pull from Docker Hub

**Experiment**
- Two services: app (Python script) + redis (redis:alpine)
- app ran script.py and exited cleanly (code 0)
- redis stayed running on port 6379/tcp
- `docker compose ps` shows status of each service

**Fix applied**
- Removed `version: "3.8"` — obsolete in modern Compose, causes warning

**Key commands**
- `docker compose up` — start all services
- `docker compose down` — stop and remove containers
- `docker compose ps` — check status

## Session 2

**Date:** 2026-06-28
**Goal:** Volumes + build a real multi-container app with Compose

### Plan
- [x] Understand volumes — why and when
- [x] Mount a volume, verify persistence
- [x] Build a real compose app (Python + Redis, actually connected)

### Volumes

**What they are**
- Containers are ephemeral — data inside is lost when container exits
- Volumes store data outside the container on the host
- Data persists across container restarts and removals

**Experiment**
- Without volume: wrote file inside container, fresh container couldn't find it
- With volume: `-v mydata:/data` — same data accessible from two different containers
- `mydata` = named volume managed by Docker
- `/data` = mount point inside container

**Key commands**
- `docker volume ls` — list volumes
- `docker volume inspect <name>` — see where data is stored on host
- `-v volumename:/path` — mount volume when running container

### Real App — Hit Counter (Python + Redis + Volume)

**What it does**
- Python app connects to Redis, increments a counter on every run
- Redis data persists via named volume across container restarts

**app.py**
- `redis.Redis(host='redis', port=6379)` — host is the compose service name, not an IP
- Docker handles DNS between containers automatically
- `r.incr('hits')` — creates key if not exists, increments by 1, returns new value

**Dockerfile changes**
- COPY app.py . (changed from script.py)
- Added `RUN pip3 install redis` to install redis library
- CMD runs app.py

**docker-compose.yml changes**
- Added volume mount to redis service: `redis-data:/data`
- Added top-level `volumes:` declaration

**Persistence proof**
- First run: Hit count 1
- After docker compose down + up: count continued (3, 4)
- Data survived container removal because it lives in the volume, not the container

**Key insight**
- `--build` flag forces Docker to rebuild image instead of using cache
- Without --build, Dockerfile changes are ignored


## Session 3

**Date:** 2026-06-29
**Goal:** GitHub Actions — automate building and testing Docker image on every push

### Plan
- [x] Understand what CI/CD is and why
- [x] Write first GitHub Actions workflow
- [x] Automate Docker build on push
- [x] Add a simple test step

### GitHub Actions — CI/CD

**What it is**
- Every push to master triggers automated build on GitHub's servers
- Workflow file lives at `.github/workflows/docker-build.yml`
- GitHub reads it automatically — no setup needed beyond the file

**Workflow structure**
- `name:` — workflow name shown in Actions tab
- `on:` — when to trigger (push, pull_request, branches)
- `jobs:` — what to run
- `runs-on:` — which OS to use (ubuntu-latest)
- `steps:` — ordered list of tasks

**Steps used**
- `actions/checkout@v4` — clones repo onto runner
- `docker build -t sys-info ./devops/docker/fundamentals` — builds image

**Fixes applied**
- `ubuntu-lastest` typo → `ubuntu-latest`
- `runs_on` → `runs-on` (hyphen not underscore)
- YAML indentation — `steps:` must be nested under job, not at job level

**Result**
- Workflow runs in ~28s on every push
- Green checkmark = Docker image builds successfully
