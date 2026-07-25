# Maggie 🕵️‍♂️

**Maggie** is a lightweight Python-based Open Source Intelligence (**OSINT**) reconnaissance tool. It automatically detects the type of input data (Email, IP address, or Username) and triggers specific investigative modules to gather a digital footprint.

## ✨ Features

The tool dynamically adapts its scanning logic based on your target:

*   **📧 Email Target:**
    *   Checks for data breaches using the HaveIBeenPwned API.
    *   Harvests domain DNS records (A, MX, TXT, NS, CNAME).
    *   Retrieves domain WHOIS information.
    *   Generates targeted Google Dorks.
*   **🌐 IP Address Target:**
    *   Fetches geolocation, ISP data, and proxy status via IP-API.
    *   Performs Reverse DNS lookup.
    *   Gathers WHOIS information for the resolved host.
*   **👤 Username Target:**
    *   Scrapes basic profile information from GitHub, Reddit, and Instagram.
    *   Generates Google Dorks to find mentions on LinkedIn, Pastebin, and Facebook.

## 🚀 Installation

1. Install the required dependencies:
   ```bash
   pip install requests dnspython python-whois
   ```

2. Download [Maggie Tool](https://githubusercontent.com/zverew/osint-maggie/refs/heads/main/MaggieTool.py) 

## 🛠 Usage

Run the script from your terminal by passing the target as an argument:

```bash
python maggie.py <email|ip|username>
```

### Examples:

*   **Investigating an Email:**
    ```bash
    python maggie.py test@example.com
    ```
*   **Investigating an IP Address:**
    ```bash
    python maggie.py 8.8.8.8
    ```
*   **Investigating a Username:**
    ```bash
    python maggie.py johndoe
    ```

## 📊 Output

The script outputs all gathered intelligence in a structured **JSON** format, making it easy to pipe into other tools. It also displays a dedicated list of **Google Dorks** ready for manual search.

## ⚠️ Disclaimer

This tool is developed strictly for educational purposes and legitimate penetration testing/security auditing. The author accepts no responsibility for any misuse or damage caused by this program.
