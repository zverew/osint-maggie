import requests, sys, re, dns.resolver, whois, socket
from concurrent.futures import ThreadPoolExecutor
import json

class Maggie:
    def __init__(self, target):
        self.target = target
        self.results = {}

    def detect_type(self):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.target):
            return "email"
        elif re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", self.target):
            return "ip"
        else:
            return "username"

    def email_breach(self, email):
        try:
            r = requests.get(f"https://haveibeenpwned.com/api/v2/breachedaccount/{email}",
                             headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200:
                self.results["breaches"] = [b["Name"] for b in r.json()]
            else:
                self.results["breaches"] = []
        except:
            self.results["breaches"] = []

    def dns_lookup(self, domain):
        recs = {}
        for rtype in ["A", "MX", "TXT", "NS", "CNAME"]:
            try:
                ans = dns.resolver.resolve(domain, rtype)
                recs[rtype] = [str(a) for a in ans]
            except:
                pass
        self.results["dns"] = recs

    def whois_lookup(self, domain):
        try:
            w = whois.whois(domain)
            self.results["whois"] = {
                "registrar": w.registrar,
                "creation": str(w.creation_date),
                "expiration": str(w.expiration_date),
                "org": w.org
            }
        except:
            pass

    def ip_info(self, ip):
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,region,city,isp,org,as,proxy")
            if r.status_code == 200 and r.json().get("status") == "success":
                self.results["ip_geo"] = r.json()
        except:
            pass

    def social_scrape(self, username):
        endpoints = {
            "github": f"https://api.github.com/users/{username}",
            "reddit": f"https://www.reddit.com/user/{username}/about.json",
            "instagram": f"https://www.instagram.com/{username}/?__a=1"
        }
        found = {}
        for site, url in endpoints.items():
            try:
                resp = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
                if resp.status_code == 200:
                    data = resp.json()
                    found[site] = data if site != "instagram" else data.get("graphql", {}).get("user", {})
                else:
                    found[site] = None
            except:
                found[site] = None
        self.results["social"] = found

    def google_dorks(self, query):
        dorks = [
            f'"{query}" site:linkedin.com',
            f'"{query}" site:pastebin.com',
            f'intitle:"{query}" filetype:pdf',
            f'"{query}" site:facebook.com'
        ]
        self.results["google_dorks"] = dorks

    def run(self):
        t = self.detect_type()
        if t == "email":
            domain = self.target.split("@")[1]
            self.email_breach(self.target)
            self.dns_lookup(domain)
            self.whois_lookup(domain)
            self.google_dorks(self.target)
        elif t == "ip":
            self.ip_info(self.target)
            try:
                host = socket.gethostbyaddr(self.target)[0]
                self.results["reverse_dns"] = host
                self.whois_lookup(host)
            except:
                pass
            self.google_dorks(self.target)
        else:
            self.social_scrape(self.target)
            self.google_dorks(self.target)

        print(json.dumps(self.results, indent=2, default=str))
        print("\n=== Google Dorks ===")
        for d in self.results.get("google_dorks", []):
            print(f"  {d}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python maggie.py <email|ip|username>")
        sys.exit(1)
    tool = Maggie(sys.argv[1])
    tool.run()