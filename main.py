import sys
import os
sys.path.append(os.path.dirname(__file__))  # Ensure relative imports work

from core.engine import Engine

def main():
    print("[*] Enter the target (IP or Domain): ", end="")
    target = input().strip()

    engine = Engine()

    # Reconnaissance
    print(f"[+] Starting Recon on {target}")
    engine.run_module("recon", "advanced", domain=target)

    # Scan
    print(f"[+] Starting Scan on {target}")
    engine.run_module("scan", "stealth", target=target)

    # Threat Intelligence
    print(f"[+] Running Threat Intel Enrichment on {target}")
    engine.run_module("intel", "enrich", input="iocs.json", domain=target)

    # Analyze
    print(f"[+] Analyzing evidence for {target}")
    engine.run_module("analyze", "malware", ioc_file="hashes.txt")

    # Hunt
    print(f"[+] Threat Hunting across network")
    engine.run_module("hunt", "ai_hunt", network="192.168.0.0/16")

    # Simulate Red Team Attack
    print(f"[+] Simulating red team phishing attack")
    engine.run_module("simulate", "phishing", scenario="phishing-attachment", target_user="ceo@example.com", payload_type="pdf-exploit", c2_server="185.45.66.100", report_only=True)

    # Incident Response
    print(f"[+] Initiating response playbook for incident")
    engine.run_module("respond", "incident", incident_id="2025-0412")

    # AI-based Threat Prediction (APT Profile)
    print(f"[+] AI-assisted threat prediction")
    engine.run_module("ai_module", "predict", profile="apt29", domain=target)

    # Report Generation
    print(f"[+] Generating report...")
    engine.run_module("report", "generate", sources=["scan", "analyze", "hunt", "ai"], format="json", output="logs_report/full_assessment_example_com_0429.json")

    print("[✔] All modules executed successfully.\n[📁] Reports saved in logs_report/")

if __name__ == "__main__":
    main()
