#!/usr/bin/env python3
# subenum.py - Subdomain enumerator (skeleton)

import requests

def enumerate_subdomains(domain):
    print(f"[*] Scanning subdomains for: {domain}")
    subdomains = ['www', 'mail', 'admin']
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=3)
            print(f"[+] Found: {url} ({res.status_code})")
        except requests.ConnectionError:
            pass

if __name__ == "__main__":
    target = input("Enter target domain: ")
    enumerate_subdomains(target)
