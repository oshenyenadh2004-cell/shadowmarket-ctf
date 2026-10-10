# ShadowMarket Takedown — Design Changes from Assignment 01

## 1. Introduction

This document describes the design differences between the original Assignment 01 proposal and the current ShadowMarket Takedown implementation. It also records the current integration status, including components that require further testing as development and integration continue.

## 2. Design Changes

### 2.1 Reverse Proxy

**Original proposal:** The Assignment 01 proposal included an Nginx reverse proxy in front of the portal.

**Current design:** According to the architecture notes, the current prototype exposes the portal and Stage 4 through their configured ports without the proposed Nginx reverse proxy.

**Reason for the change:** The architecture notes identify prototype simplicity as the reason for omitting the reverse proxy.

**Impact:** The architecture has fewer components. However, port configuration, participant access, and service isolation must be verified during integration testing.

**Current status:** The Stage 4 application starts inside Docker, but host-browser access through port 5000 remains blocked in the current environment. Further investigation is required.

### 2.2 Database Implementation

**Original proposal:** SQLite was proposed in Assignment 01.

**Current design:** The architecture notes state that Stage 4 uses the SQLite database file `ctf.db`.

**Design change:** No change from the original proposal is documented.

**Current status:** Database behavior and reset functionality require verification through integration testing.

### 2.3 Flag Validation Service

**Original proposal:** Flag validation was described conceptually in Assignment 01.

**Current design:** Flag validation is implemented as a separate Flask service. The service compares submitted flags against SHA-256 hashes and records submission attempts in `validation_log.txt`.

**Reason for the change:** The validation logic has been implemented as a dedicated service rather than remaining only a conceptual part of the design.

**Impact:** Validation is separated from the participant portal, and submission records are available for testing and troubleshooting.

**Current status:** Successful flag submissions for Stages 1–3 have been observed in the validation log. Further tests are required to verify invalid submissions, empty submissions, and complete integration behavior.

## 3. Architecture and Isolation

The current Compose configuration defines two Docker networks:

- `ctf-public`: the public-facing bridge network.
- `ctf-internal`: an internal bridge network configured with `internal: true`.

The portal is connected to both networks, while the flag validator and Stage 4 application are connected to the internal network.

The portal can communicate with Stage 4 internally. However, the host port mapping for Stage 4 has not been applied successfully in the current environment.

The architecture notes also use the network name `platform_ctf-isolated`, while the current Compose configuration uses `platform_ctf-internal`. This discrepancy should be reconciled in the documentation.

## 4. Integration Status

The current development and integration status is as follows:

| Component | Current Status |
|---|---|
| Participant portal | Starts and is accessible on port 9090 |
| Flag validator | Container starts; successful submissions for Stages 1–3 are recorded |
| Stage 4 application | Starts and responds to requests from the portal container |
| Stage 4 host access | Blocked by the missing runtime port mapping |
| Stages 1, 2, and 3 | Successful flag submissions observed |
| Stages 5 and 6 | Challenge files exist; full challenge and download verification remains necessary |
| Reset and recovery | Reset script reviewed; execution and recovery verification remain outstanding |
| Network isolation | Configuration reviewed; comprehensive security verification remains outstanding |

These statuses describe the current development environment and must be updated as teammates' changes are integrated and tested.

## 5. Pending Integration Work

The following work remains before final sign-off:

1. Integrate the latest changes from all group members.
2. Resolve the Stage 4 host-port publishing issue.
3. Verify the functionality of all six stages.
4. Test incorrect and empty flag submissions.
5. Verify database reset, session reset, and validation-log backup behavior.
6. Verify network isolation and ensure internal services are not unintentionally exposed.
7. Capture test evidence and update the integration test log.
8. Compare the implemented design against the original Assignment 01 proposal.

## 6. Conclusion

The current implementation retains SQLite, omits the proposed Nginx reverse proxy for prototype simplicity, and implements flag validation as a separate Flask service using hashed flag comparison and submission logging.

Some integration tests remain incomplete because the current environment does not provide working host-browser access to Stage 4 and the latest group changes may not yet be integrated. Final conclusions about system completeness and security should be made only after the remaining changes have been integrated and verified.