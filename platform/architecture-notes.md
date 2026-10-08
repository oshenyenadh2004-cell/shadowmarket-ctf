# Architecture Notes — As Built

Reference diagram: [Eraser.io architecture diagram](https://app.eraser.io/workspace/Y817YFmezYeWHhBCgpkZ)

## Components

**Participant access:** Participants connect to the CTF portal over HTTP(S) on the host machine. No direct access is given to internal services.

**Static challenges (Stages 1, 2, 3, 5, 6):** Served as downloadable files (images, text, disk image, pcap). No server-side logic required, so no additional isolation needed beyond normal file hosting.

**Stage 4 (live web app):** Runs as a Docker container (`shadowmarket-stage4`) on a dedicated internal Docker network (`platform_ctf-isolated`), defined with `internal: true` in `docker-compose.yml` — this means the container has no route to the internet, satisfying the isolation requirement. Only port 5000 is published to the host so participants/testers can reach the login page.

**Flag validation service:** A separate Flask service (`flag_validator.py`) running on port 6001. Correct flags are stored as SHA-256 hashes, never in plaintext, so inspecting the source code does not reveal answers. Every submission (correct or incorrect) is logged to `validation_log.txt` with a timestamp.

## Deviations from the Assignment 01 proposal

- The original proposal described an Nginx reverse proxy in front of the portal; the current implementation exposes the Stage 4 container's port directly for prototype simplicity. A reverse proxy can be added later without affecting challenge logic.
- SQLite was proposed for the database; Stage 4's `ctf.db` uses this as planned — no change.
- Flag validation was described conceptually in Assignment 01; it is now implemented as a dedicated Flask service with hashed flag comparison and attempt logging.

## Reset mechanism

`platform/reset.sh` tears down and rebuilds the Stage 4 container, restoring a clean database and session state, and archives the validation log before clearing it.

## Measured resource usage

See `platform/resource-usage.md` for actual CPU, RAM, and storage figures measured on the deployment VM.
