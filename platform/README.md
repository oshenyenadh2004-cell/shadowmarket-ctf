# ShadowMarket Takedown — CTF Platform

## 1. Project Overview

ShadowMarket Takedown is a six-stage Capture The Flag (CTF) cybersecurity challenge platform. Participants investigate challenges across different cybersecurity areas and submit flags for validation.

The platform contains a participant portal, a flag-validation service, and a live web application for Stage 4.

## 2. Project Structure

```text
shadowmarket-ctf/
├── platform/
│   ├── portal/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── flag_validator.py
│   ├── reset.sh
│   ├── validation_log.txt
│   ├── architecture-notes.md
│   ├── resource-usage.md
│   ├── test-log.md
│   └── design-changes.md
├── stage1-osint/
├── stage2-stego/
├── stage3-crypto/
├── stage4-web/
├── stage5-forensics/
└── stage6-network/
```

## 3. Requirements

Before running the platform, install:

- Docker Desktop
- Docker Compose
- A web browser
- Git (if cloning the repository)

## 4. Setup and Installation

Clone the repository:

```bash
git clone https://github.com/oshenyenadh2004-cell/shadowmarket-ctf.git
```

Open the project directory:

```bash
cd shadowmarket-ctf
```

Build the images and start the services:

```bash
docker compose -f platform/docker-compose.yml up -d --build
```

Check the running containers:

```bash
docker ps
```

## 5. Accessing the Platform

### Participant Portal

Open the following URL in a web browser:

http://localhost:9090

### Stage 4 Web Application

The configured URL is:

http://localhost:5000

**Known issue:** Stage 4 currently starts inside Docker and responds to internal requests from the portal container, but host-browser access through port 5000 has not been resolved. Do not consider this access test successful until it has been fixed and verified.

## 6. Platform Services

| Service | Container name | Purpose |
|---|---|---|
| Participant portal | `shadowmarket-portal` | Provides the participant-facing interface |
| Flag validator | `shadowmarket-validator` | Validates submitted flags and records attempts |
| Stage 4 web application | `shadowmarket-stage4` | Runs the live Stage 4 challenge |

The Compose configuration defines a public-facing network and an internal network. The portal connects to both networks, while the validator and Stage 4 service connect to the internal network.

## 7. Challenge Stages

The repository contains six challenge stages:

1. Stage 1 — OSINT
2. Stage 2 — Steganography
3. Stage 3 — Cryptography
4. Stage 4 — Web security
5. Stage 5 — Digital forensics
6. Stage 6 — Network analysis

The intended challenge workflow and completion of every stage must be verified through testing.

## 8. Testing and Evidence

Integration testing is documented in:

- `platform/test-log.md` — test cases, observed results, defects, and outstanding tests.
- `platform/design-changes.md` — design changes, rationale, and current integration issues.
- `platform/architecture-notes.md` — architecture and service design.
- `platform/resource-usage.md` — recorded resource-usage information.

Only tests that have actually been executed and supported by evidence should be marked as passed.

## 9. Stopping the Platform

To stop and remove the Compose containers and networks, run:

```bash
docker compose -f platform/docker-compose.yml down
```

This command does not remove the project source files. However, container-managed state may be lost when containers are removed.

## 10. Resetting the Platform

The project includes a reset script at `platform/reset.sh`.

The script runs Docker Compose down and up, rebuilds the services, and archives and clears the validation log.

**Important:** The reset script has not yet been verified through a complete recovery test. Back up important data and coordinate with the team before running it, because it clears the current validation log after creating a backup.

## 11. Known Issues and Outstanding Work

- Stage 4 host access through `http://localhost:5000` is unresolved.
- End-to-end testing of all six stages remains to be completed.
- Incorrect and missing flag tests require completion.
- Reset and recovery require verification.
- Comprehensive network-isolation testing remains outstanding.

Refer to `platform/test-log.md` for the current test statuses.

## 12. Contributors

Add the names and contributions of all group members before final submission.
