# ShadowMarket Takedown — CTF Play Box

**IE3132 Penetration Testing — Assignment 02**
Group: IT24101268, IT24102491, IT24101595, IT24100528

A six-stage Capture The Flag challenge following a fictional dark web marketplace investigation. Participants trace a vendor's alias through OSINT, steganography, cryptography, web exploitation, digital forensics, and network analysis to confirm the marketplace's takedown.

## Prerequisites

- Docker and Docker Compose
- A web browser
- (Optional, for manual stage-solving) `exiftool`, `steghide`, Wireshark/`tshark`, `foremost` or Autopsy

## Setup and Running the Box

1. Clone this repository:
```bash
   git clone https://github.com/oshenyenadh2004-cell/shadowmarket-ctf.git
   cd shadowmarket-ctf/platform
```

2. Build and start all services:
```bash
   docker compose up --build -d
```

3. Confirm all three containers are running:
```bash
   docker ps
```
   You should see `shadowmarket-portal`, `shadowmarket-validator`, and `shadowmarket-stage4` all `Up`.

4. Open the CTF portal in a browser:
	http://localhost:9090/

   All 6 stages are accessible from this portal — download files, read challenge details, and submit flags directly through the web interface.

   Note: Stage 4 (the live web application) is also directly reachable at `http://localhost:5000` if needed.

## Architecture Overview

- **Portal** (`localhost:9090`) — unified web interface for all 6 stages, the only service exposed beyond the internal Docker network
- **Flag Validator** (internal, port 6001) — checks submitted flags against SHA-256 hashes, never stores flags in plaintext
- **Stage 4 Web App** (`localhost:5000`) — the live, intentionally vulnerable Flask application for the SQL injection challenge
- Stage 4 and the flag validator run on an isolated internal Docker network (`internal: true`) with no internet egress
- See `platform/architecture-notes.md` for full details and the reference diagram link

## Stage Overview

| Stage | Domain | Difficulty | Flag Format |
|---|---|---|---|
| 1 — The Vendor's Footprint | OSINT | Easy | `SHADOWMKT{DarkK1ng99}` |
| 2 — Buried in the Upload | Steganography | Easy | `SHADOWMKT{DarkNet_Chat_0x99}` |
| 3 — Coded Correspondence | Cryptography | Moderate | `SHADOWMKT{SRVNODE7EAST}` |
| 4 — The Mirror Login | Web Security | Moderate | `SHADOWMKT{SQL_BYP4SS_SUCC3SS}` |
| 5 — The Seized Drive | Digital Forensics | Moderate–Hard | `SHADOWMKT{UMBRA_NODE_9}` |
| 6 — Takedown | Networking | Hard | `SHADOWMKT{TAKEDOWN_CONFIRMED}` |

(Flags listed here for grading/testing reference — not shown to participants.)

## Solver / Exploit Scripts

Located in `scripts/`:
- `stage3_vigenere_solver.py` — automates the Vigenère cipher decode for Stage 3
- `stage4_sqli_exploit.py` — automates the SQL injection login bypass for Stage 4

Run with:
```bash
python3 scripts/stage3_vigenere_solver.py
python3 scripts/stage4_sqli_exploit.py
```

## Resetting the Box

To restore Stage 4 and the flag validator to a clean state:
```bash
cd platform
./reset.sh
```

This rebuilds the Stage 4 container (fresh database, fresh session state) and archives/clears the flag validation log. Static stages (1, 2, 3, 5, 6) require no reset since they're read-only files.

## Testing

See `platform/test-log.md` for functional, negative-validation, isolation, and reset test results, and `platform/design-changes.md` for documented changes from the Assignment 01 proposal.

## Group Contribution

| Member | Responsibility |
|---|---|
| Hinni Arachchi O.Y.E (IT24101268) | Platform & Architecture |
| Senadheera T.A (IT24102491) | Challenge Design A — Stages 1, 2, 3 |
| Abeywickrama M.M (IT24101595) | Challenge Design B — Stages 4, 5, 6 |
| WNS Karunarathne (IT24100528) | Integration, Testing & Documentation |

See repository commit history for individual contribution evidence.
