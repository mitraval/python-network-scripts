# Bulk Network Device Configuration & Log Parsing

## Overview
This repository contains a Python automation script designed to eliminate manual CLI workflows for enterprise network management. It automates the process of logging into multiple routing and switching devices, executing a standardized set of commands, and parsing the output for rapid troubleshooting and configuration validation.

## Enterprise Value & Technical Highlights
In a large-scale infrastructure environment, manually verifying configurations or pulling logs across hundreds of nodes is prone to human error and high mean-time-to-resolution (MTTR). This script solves that by:
* **Enterprise Security Architecture (Jump Server Integration):** The script is designed to navigate strict corporate security boundaries by establishing an initial connection to a Linux-based jump server (bastion host) before initiating secondary SSH sessions to the target end-devices. This mirrors standard production deployments where direct infrastructure access is restricted.
* **Handling Delay Variation (Send & Wait Logic):** Implements dynamic command timing. The script explicitly waits for the device prompt to return before dispatching the next command. This prevents buffer overruns and ensures reliable execution even across high-latency or fluctuating connections (such as microwave, UBR, or variable-route backhauls).
* **Scaling Operations:** Reads target IPs from an external `host` file, allowing automated execution across multiple remote devices in a single run.
* **Standardizing Output:** Automatically saves and organizes the parsed command outputs into a dedicated `ports` file for easy auditing, diffing, and review.
* **Reducing MTTR:** Drastically cuts down the time required to isolate network faults or verify configuration baselines during major incident management.

## Prerequisites
To run this script locally, ensure you have the following installed:
* Python 3.x
* Netmiko (Network automation library)
  `pip install netmiko`

## Usage
1. Update the `host` file with the target IP addresses (one per line).
2. Open the Python script and manually enter the target device credentials (username and password) into the designated variables.
3. Execute the script via the terminal:
   `python your_script_name.py`
4. The script will iterate through the inventory, execute the predefined commands intelligently accounting for network delay, and generate the parsed output in the `ports` file within the same directory.

> **Note on Security:** This repository serves as a portfolio demonstration based on a GNS3/CentOS lab environment. If adapting this script for a live production environment, ensure credentials are removed from the source code and managed via secure environment variables, a vault system, or interactive prompts.
