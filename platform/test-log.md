# ShadowMarket Takedown — Integration Test Log

## 1. Purpose

This document records integration and functional testing of the ShadowMarket Takedown CTF platform. It tracks test results, observed defects, and outstanding verification tasks.

## 2. Test Environment

- Operating system: Windows host with Docker Desktop
- Project: ShadowMarket Takedown
- Portal URL: `http://localhost:9090`
- Stage 4 URL: `http://localhost:5000`
- Containers: `shadowmarket-portal`, `shadowmarket-validator`, `shadowmarket-stage4`

## 2.1 Tools Used for Testing


Visual Studio Code (VS Code)

To inspect project files, edit documentation, and use the terminal.

Docker

To run and inspect the platform's containers.

Docker Compose

To build, start, stop, and manage the platform services.


## 3. Test Results

| Test ID | Test Case | Expected Result | Observed Result | Status |
|---|---|---|---|---|
| INT-01 | Start the Docker Compose environment | Required containers start | Portal, validator, and Stage 4 containers were running | PASS |
| INT-02 | Open the participant portal | Portal is accessible | Portal accessible at `http://localhost:9090` | PASS |
| INT-03 | Submit the correct Stage 1 flag | Validator accepts the flag | Validation log records `result=CORRECT` | PASS |
| INT-04 | Submit the correct Stage 2 flag | Validator accepts the flag | Validation log records `result=CORRECT` | PASS |
| INT-05 | Submit the correct Stage 3 flag | Validator accepts the flag | Validation log records `result=CORRECT` | PASS |
| INT-06 | Access Stage 4 through the host | Stage 4 login page is accessible | Host port 5000 is not published by the running container | BLOCKED |
| INT-07 | Submit incorrect or missing flags | Validator rejects invalid submissions | Some incorrect submissions are recorded; complete negative testing remains outstanding | PARTIAL |
| INT-08 | Test reset and recovery | Services restart, state resets, and logs are backed up | Reset script reviewed; execution and recovery not yet verified | NOT TESTED |
| INT-09 | Verify network isolation | Internal services are not directly exposed to participants | Compose configuration reviewed; runtime isolation tests outstanding | NOT TESTED |
| INT-10 | Test Stages 5 and 6 | Challenge files and intended workflows operate correctly | Not yet verified | NOT TESTED |

## 4. Defects and Observations

### DEF-01: Stage 4 host port is not published

**Observation:** The Compose configuration declares port mapping `5000:5000`, but `docker ps` displays only `5000/tcp` for `shadowmarket-stage4`. The Stage 4 page cannot be accessed through `http://localhost:5000`.

**Impact:** Stage 4 end-to-end testing is blocked.

**Status:** Open — further investigation required.

### OBS-02: Architecture network-name discrepancy

The architecture notes refer to `platform_ctf-isolated`, while the actual Compose configuration names the internal network `platform_ctf-internal`.

**Status:** Requires confirmation and documentation update if appropriate.

### OBS-03: Limited disk headroom

The resource report states that 20 GB of a 24 GB VM disk is used, leaving approximately 4 GB available.

**Status:** Monitor storage during further testing.

## 5. Reset and Recovery

The reset script was reviewed but has not yet been executed and verified as part of a reset test.

Verification must cover container restart, Stage 4 database/session reset, validation-log backup, and successful recovery.

## 6. Outstanding Work

- Resolve Stage 4 host port publication.
- Complete end-to-end testing across all six stages.
- Test incorrect and missing flags.
- Verify reset and recovery.
- Verify network isolation and service exposure.
- Capture screenshots and command output as evidence.
- Confirm design changes against Assignment 01.
- Record final test results after actual execution.

## 7. Evidence and Test Integrity

Only tests that have actually been executed and supported by evidence should be marked PASS. Outstanding tests must remain clearly identified as blocked, partial, or not tested.