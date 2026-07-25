# osint-maggie
this is my first project :) i'd update it  soon.
# Maggie
OSINT tool – email breaches, DNS, WHOIS, IP geolocation, social scraping, and Google dorks. No API keys required.

## Installation

```bash
pip install requests dnspython python-whois
Usage
bash
python maggie.py <target>
Target can be:

Email: john.doe@gmail.com

IP: 8.8.8.8

Username: somehandle

Examples
bash
python maggie.py admin@example.com
python maggie.py 192.168.1.1
python maggie.py elonmusk
Output
JSON with:

breaches – breached databases (email only)

dns – A, MX, TXT, NS, CNAME records

whois – registrar, dates, organization

ip_geo – country, city, ISP, proxy status (IP only)

reverse_dns – hostname (IP only)

social – GitHub, Reddit, Instagram profiles (username only)

google_dorks – ready-to-copy search queries

Dependencies
Python 3.6+

requests

dnspython

python-whois
