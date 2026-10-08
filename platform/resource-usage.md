# Resource Usage — Actual Measurements

Measured on the development/testing VM (Kali Linux, VirtualBox).

| Resource | Allocated (Assignment 01 estimate) | Actual Usage |
|---|---|---|
| vCPUs | 2 | 0.07% CPU utilization under idle/light load (Stage 4 container) |
| RAM | 4 GB | 22.55 MiB used / 4.779 GiB limit (0.46%) for Stage 4 container |
| Storage | 20–30 GB | 20 GB used of 24 GB VM disk (includes OS, tools, and all 6 stage files) |
| Network | N/A | Stage 4 container isolated on internal bridge network, no internet egress; 2.15 kB in / 1.05 kB out observed |

## Host VM totals

| Metric | Value |
|---|---|
| Total RAM (host VM) | 4.8 GiB |
| RAM used | 3.7 GiB |
| RAM available | 1.1 GiB |
| Disk used | 20 GB |
| Disk size | 24 GB |

## Notes

The Stage 4 container itself is extremely lightweight — under 1% CPU and under 25 MiB RAM at idle, far below the 2 vCPU / 4 GB allocation proposed in Assignment 01. The majority of VM disk usage (20 GB of 24 GB) comes from the base Kali OS and installed tooling (Wireshark, Autopsy, steghide, Docker images, etc.) rather than the CTF challenge files themselves, which total only a few hundred MB.

One point worth flagging for the final submission: available disk headroom is low (only 4 GB free on this VM). If additional stages, Docker layers, or test data are added, the VM disk size should be increased to comfortably stay within the 20–30 GB target with room to spare.
