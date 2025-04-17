# 🕵️‍♂️ Username Enumeration Lab

> **r3conxploit OSINT Lab Series**  
> Focused on tracking digital footprints via usernames across the web.

---

## 🎯 Objective

Enumerate and track usernames across multiple platforms to correlate digital presence, social footprints, and threat attribution.

---

## 🛠️ Tools Used

| Tool     | Description                              |
|----------|------------------------------------------|
| [Sherlock](https://github.com/sherlock-project/sherlock) | Hunt usernames across 300+ platforms |
| [Maigret](https://github.com/soxoj/maigret)         | Collect detailed user profiles       |

---

## 🧰 Folder Structure

```bash
username-enum/
├── README.md              # Penjelasan topik & tools yang dipakai
├── tools/                 # Tools yang digunakan (cloned / symlink / catatan link)
│   ├── sherlock/
│   └── maigret/
├── scripts/               # Script custom kalau ada
│   └── hunter.py
├── screenshots/           # Dokumentasi hasil recon visual
├── wordlists/             # Username lists atau custom wordlist
│   └── common-usernames.txt
└── results/               # Output hasil recon / parsing
    └── sherlock_result.json


---

## ✅ Checklist

- [ ] 🔍 Identify target usernames
- [ ] 📥 Run `sherlock` and export results
- [ ] 🧠 Correlate data with `maigret`
- [ ] 💾 Store and visualize findings
- [ ] 📝 Document findings in markdown
- [ ] 📸 Capture screenshots (for reports)

---

## ⚙️ Example Command

```bash
# Run sherlock for username
python3 sherlock user123 --print-found --output results/sherlock_user123.txt

# Run maigret
maigret -d -j -o results/ user123
```

## 📚 Notes
Recommended to use VPN or Tor while scanning to avoid detection.

Enrich recon with reverse image search from avatars found.

📎 Related
📂 tools/: External OSINT tools.

🧠 scripts/: Your own automation.

📄 results/: Save your footprints.

Silently hunting. Always watching. Always enumerating.
— r3conxploit

---
