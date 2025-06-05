# Developer Guide – Clarinet Repair Portal

## Overview
This Frappe v15 app powers Artisan Clarinets’ repair business. Maintain clarity, traceability, and automation. Keep fixture JSON and Python models in sync.

---

## File Structure
```
clarinet_repair_portal/
├── clarinet_repair_portal/
│   ├── doctype/
│   ├── public/js/
│   ├── patches/
│   ├── hooks.py
│   ├── config/
│   └── __init__.py
├── tests/
├── README.md
└── DEVELOPER.md
```

---

## Fixtures
- Always export fixtures after schema changes:
```bash
bench export-fixtures --app clarinet_repair_portal
```

- Keep `fixtures = […]` in `hooks.py` updated.

---

## Migrations
- Patch file: `bench make-patch --app clarinet_repair_portal`
- Run migration:
```bash
bench --site <site> migrate
```
- All patches must be **idempotent**.

---

## Frontend
- Custom JS: `public/js/…`
- Pad map SVG tools: click listeners, field injections
- Use Tailwind-style utility classes in Web Forms where needed

---

## Testing
- PyTest or `unittest` under `tests/`
- Target ≥90% coverage for:
  - Pad auto-fill
  - QA logic
  - Repair status transitions
  - Service logging

---

## DevOps
- CI-style commits:
```bash
git add -A && git commit -m "feat: add QA checklist links to Repair Request"
```
- Version using SemVer: `vX.Y.Z`
- All commits must include updated fixtures when schema changes occur

---

## Deployment Checklist
- `apps.txt` includes `clarinet_repair_portal`
- App import path: `clarinet_repair_portal.clarinet_repair_portal`
- Install into site:
```bash
bench --site <site> install-app clarinet_repair_portal
```
- Validate Python module loads:
```bash
python3 -c "import clarinet_repair_portal"
```

---

## Maintainers
Clarinet Repair Portal Dev GPT
MIT License