# DevOps Automation with Python

## Introduction

This repository provides explanations of using Python for DevOps automation, focusing on standard libraries commonly utilized in the field.

## Standard Libraries

### OS

The `os` module interacts with the operating system, facilitating file and directory operations, process management, and environment variables.

### Platform

The `platform` module provides access to underlying platform data, such as hardware, operating system identification, and system version information.

### Subprocess

The `subprocess` module spawns new processes, connects to their input/output/error streams, and obtains their return codes, enabling interaction with system commands and external programs.

### SYS

The `sys` module accesses variables used by the Python interpreter and provides functions interacting with it.

### psutil

The `psutil` module facilitates system monitoring and management by providing functions to retrieve information on running processes, system utilization, and more.

### Regular Expression (re)

The `re` module provides support for regular expressions, enabling pattern matching and manipulation of strings based on specific search criteria.

### scapy

The `scapy` module is a powerful interactive packet manipulation tool, providing capabilities for packet crafting, sniffing, and analysis in networking tasks.

### Requests and urllib3

The `requests` and `urllib3` modules facilitate making HTTP requests, interacting with web APIs, and handling HTTP responses, essential for web-related automation tasks.

### Logging

The `logging` module enables logging messages at runtime, aiding in debugging, monitoring, and troubleshooting applications and automation scripts.

### Getpass

The `getpass` module provides functions for secure password input, useful when interacting with password-protected systems or services.

### Boto3

The `boto3` module is the official AWS SDK for Python, allowing interaction with various AWS services, facilitating cloud infrastructure automation and management.

### Paramiko

The `paramiko` module provides SSH protocol implementation, enabling secure communication and remote execution on servers, crucial for managing remote systems.

### JSON

The `json` module facilitates working with JSON (JavaScript Object Notation) data interchange format, essential for data serialization and deserialization tasks.

### PyYAML

The `PyYAML` module parses YAML (YAML Ain't Markup Language) configuration files, commonly used in infrastructure as code and configuration management.

### Pandas

The `pandas` module is a powerful data analysis and manipulation library, useful for working with structured data, including CSV files, in DevOps automation tasks.

### smtplib

The `smtplib` module provides an SMTP client session for sending emails, enabling notification and alerting mechanisms in automation workflows.

## Other Standard Libraries

- **socket**: For networking tasks, such as creating client-server applications and working with network sockets.
- **argparse**: For parsing command-line arguments and options, facilitating the creation of command-line interfaces.
- **os.path**: For common pathname manipulations, such as joining, splitting, and normalizing paths across different operating systems.
- **sqlite3**: For interacting with SQLite databases, useful for storing and retrieving structured data locally.

These libraries extend Python's capabilities for various automation tasks in the DevOps domain.

## Difference between Library and Module

| Criteria   | Module                                                  | Library                                                 |
|------------|---------------------------------------------------------|---------------------------------------------------------|
| Definition | A module is a single Python file that can be imported. | A library is a collection of modules packaged together. |
| Usage      | Modules are used to organize code within a project.     | Libraries are used to provide pre-written functionality.|
| Example    | `os.py`, `sys.py`                                       | Python Standard Library, NumPy, pandas                  |
