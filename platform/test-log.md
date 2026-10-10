# ShadowMarket Takedown — Integration Test Log

## 1. Purpose

This document records integration and functional testing for all six stages of the ShadowMarket Takedown CTF platform as part of Member 4's Integration, Testing & Documentation responsibilities.

## 2. Test Environment

- Host: Windows with Docker Desktop
- Portal URL: `http://localhost:9090`
- Stage 4 URL: `http://localhost:5000`
- Services: Portal, flag validator, Stage 4 web application

## 2.1 Tools Used for Testing


Visual Studio Code (VS Code)

To inspect project files, edit documentation, and use the terminal.

Docker

To run and inspect the platform's containers.

Docker Compose

To build, start, stop, and manage the platform services.


## 3. Stage Testing Results

| Test ID | Test Case | Expected Result | Status |
|---|---|---|---|
| INT-01 | Start the Docker Compose environment | Required services start successfully | PASS |
| INT-02 | Open the participant portal | Portal is accessible | PASS |
| INT-03 | Test Stage 1 challenge and flag submission | Correct flag is accepted | PASS |
| INT-04 | Test Stage 2 challenge and flag submission | Correct flag is accepted | PASS |
| INT-05 | Test Stage 3 challenge and flag submission | Correct flag is accepted | PASS |
| INT-06 | Test Stage 4 internal connectivity | Portal container receives a successful HTTP response from Stage 4 | PASS |
| INT-07 | Test Stage 4 through the participant's browser | Login page is accessible through the host | Verify actual result |
| INT-08 | Test Stage 5 challenge file download | `seized_drive.img` downloads successfully | Verify actual result |
| INT-09 | Test Stage 6 challenge file download | `takedown.pcap` downloads successfully | Verify actual result |
| INT-10 | Submit an incorrect flag | Incorrect flag is rejected | Verify actual result |
| INT-11 | Submit an empty flag | Empty submission is rejected or blocked | Verify actual result |
| INT-12 | Test reset and recovery | Services recover and reset behavior matches the specification | Verify actual result |
| INT-13 | Verify network isolation | Internal services are not directly exposed to participants | Verify actual result |

## 4. Defects and Observations

### DEF-01 — Stage 4 host port publication

The Stage 4 Flask application starts inside Docker, and the portal container can reach it internally. However, the runtime port mapping for host port 5000 is empty, and the browser previously returned a connection-refused error.

**Status:** Open unless subsequently fixed and retested.

### OBS-01 — Network naming discrepancy

The architecture notes refer to `platform_ctf-isolated`, while the Compose configuration uses `platform_ctf-internal`.

**Status:** Requires confirmation.

## 5. Reset and Recovery

The reset script was reviewed. Its actual behavior must be verified through an execution test before reset and recovery can be marked PASS.

## 6. Evidence

Attach screenshots, validation-log excerpts, terminal outputs, and download results corresponding to each completed test. Each PASS result must be supported by evidence of the expected behavior.

## 7. Conclusion

The initial integration checks confirm that the Docker services start, the portal is accessible, the validator accepts the correct flags for Stages 1–3, and the portal can communicate with Stage 4 internally.

Final sign-off depends on verifying the remaining tests and resolving any outstanding defects.