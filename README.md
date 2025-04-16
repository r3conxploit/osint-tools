# 🕵️‍♂️ osint-tools
> Curated by `r3conxploit` – Silently watching. Always reconning.

## 📡 Recon Tools & Scripts
A collection of tools and one-liners for passive/active reconnaissance.

### 🔍 Subdomain Enumeration
- `assetfinder`
- `subfinder`
- `amass enum -passive`
- `dnsx` + `massdns`

### 🌐 IP/ASN Profiling
- `whois`, `asnlookup`, `bgpview`
- `ipinfo.io`, `shodan`, `censys`

### 📁 Metadata & File Analysis
- `exiftool`
- `pdf-parser`
- `strings`, `binwalk`

## 📂 Repo Structure
- `/tools/` → `custom bash/python recon tools`
- `/scripts/` → `one-liners, automations`
- `/wordlists/` → `target-specific wordlists`
- `/notes/` → `OSINT technique markdowns`

---

## ⚙️ Tools To Add

| Tool        | Type         | Notes                        |
|-------------|--------------|------------------------------|
| Amass       | Subdomains   | Active + passive modes       |
| GitHub Dork | Discovery    | Via `github-dork-scraper`    |
| FOCA        | Metadata     | PDF, DOCX, XLS scraping      |
| recon-ng    | Framework    | Modular, CLI-based OSINT     |
| theHarvester| Emails, Hosts| Good for initial mapping     |

---

## 👣 Footprinting Workflow (r3x-style)

```bash
subfinder -d example.com -o subdomains.txt
dnsx -l subdomains.txt -a -resp -o alive.txt
httpx -l alive.txt -title -tech -o webscan.txt



## 📬 Contact
- `r3conxploit@protonmail.com`  
- [PGP Fingerprint](https://keys.openpgp.org/search?q=r3conxploit): `3EBD 134C ... 549C`

---

> _“Information is power — gather it before they hide it.”_  
