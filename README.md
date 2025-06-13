
# CyberScope - Cyber Threat Hunting and Intelligence Platform
[![Donate](https://img.shields.io/badge/Donate-Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/drrobot)

CyberScope is an open-source tool designed for advanced cyber threat reconnaissance, analysis, and reporting.

## Features:
- Passive DNS & WHOIS Collection
- Subdomain Enumeration
- Metadata Collection
- Threat Feed Correlation
- Playbook Automation (MITRE ATT&CK)
- Real-time Progress Reporting
- RESTful API Mode (Daemon)

## Requirements:
- Python 3.7+
- Flask, rich, PyYAML

## Installation:
```
git clone https://github.com/username/cyberscope.git
cd cyberscope
pip install -r requirements.txt
```

## Usage:
```
python cli/main.py recon --domain example.com
python cli/main.py --daemon
```

## Playbooks:
Custom attack and defense playbooks can be added to the playbooks directory.
