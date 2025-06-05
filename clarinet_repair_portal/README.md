# Clarinet Repair Portal

A full-featured custom Frappe/ERPNext v15 app built for **Artisan Clarinets** to manage precision clarinet repairs, inspections, upgrades, and customer service.

---

## Overview
Tailored for a professional repair workflow, this app centralizes:
- Customer repair requests and tracking
- Visual inspections and service documentation
- Custom parts management (pads, corks, springs)
- Dynamic repair checklists
- QA procedures and technician logging
- Full client communication and historical traceability

---

## Features

### Repair Workflow
- **Repair Request**: Tracks all repair jobs with linked customer, instrument, status, parts, and invoices
- **Repair Inspection**: Embedded visual + condition checklist logging
- **Repair Service Category + Requested Services**: Modular repair menu by service type (e.g., Restoration, Setup)

### Pad Management
- **Clarinet Pad Library**: Pre-loaded pad specs by model (e.g., R13, Tosca)
- **Repair Pads Used**: Logs pads installed/replaced per job
- **Auto-fill Logic**: Pads loaded automatically from selected model

### Quality Assurance
- **Repair QA Checklist + Steps**: Custom QA templates per repair type (e.g., Restoration, Customization)
- **Auto-linked to repair type**, editable on each job

### Instrument Templates
- Standard presets for common models (e.g., Buffet R13)
- Apply standard service scope or parts

### Reporting & Visibility
- Status overview reports
- Time spent by technician
- Repair history per client
- Optional KPI dashboard integration

### Customer Portal
- `/repair-request/<ID>` page shows status, work, communications
- Customers can submit notes
- Linked to ERPNext Communications, Quotations, Invoices

### ERP Integration
- Sales Invoice, Quotation, Stock Entry references
- Communication Log
- Role permissions and access controls

---

## Installation
```bash
bench get-app clarinet_repair_portal https://github.com/ArtisanClarinets/clarinet_repair_portal.git
bench --site erp.artisanclarinets.com install-app clarinet_repair_portal
```

## Post Install
```bash
bench --site erp.artisanclarinets.com migrate
bench --site erp.artisanclarinets.com clear-cache
```

## Fixture Management
```bash
bench --site erp.artisanclarinets.com export-fixtures
```

## Workspace Access
- Appears in Desk as **Clarinet Repair Portal**
- Grouped sections: Repair Ops, Instrument Data, QA, Reports

---

## Planned Features

### Technician-Focused Enhancements
- Bore Scope Image Capture Integration
- Technician AI Assistant
- Condition-to-Recommendation Mapping
- Hotkey & Barcode Shortcuts

### Smart Diagnostic Tools
- Leak Test Result Logger (Magnahelic/Feeler Gauge)
- Intonation Deviation Logger
- Mechanical Resistance Logger
- Crack Progression Tracker

### AI & Automation
- AI-Generated Repair Notes
- Predictive Maintenance Alerts
- Automated Invoicing & Discounting Engine

### Inventory & Part Management
- Cross-Instrument Parts Interchange Table
- Smart Pad Selector
- Lot-Based Material Expiry Alerts

### Customer Portal Additions
- Pre-Repair Self-Diagnosis Wizard
- Service Recommendation Engine
- Appointment Scheduler Sync
- Loaner Instrument Management

### Business & Insights
- Technician Certification Tracker
- Technician Load Balancer
- Workshop Efficiency Metrics
- Reputation Tracker

### Field Use & Offline Support
- Offline Kiosk Mode
- Mobile Image Annotation Tool

### Marketing & Outreach
- Repair Journey Generator
- Custom Repair Certificates

### Existing Future Roadmap (Merged)
- Instrument Condition History (per serial over time)
- Technician Performance Dashboard
- Automated Repair Estimator (based on model + services)
- Service Tagging System for advanced filtering
- Customer Feedback Log (post-service ratings/comments)
- Serialized Multi-Instrument Tracker
- Custom Financial & QA Reports (Revenue by Service Type, QA Failure Rate)
- Live Pad Mapping Tool (visual SVG keymap with click-to-log pads)
- Interactive Repair Timeline (progress tracker with logs)
- Technician Time Logger Widget
- Mobile Technician Mode (iPhone/iPad kiosk view)
- Part Lookup & Recommendation Tool
- QA Walkthrough Wizard
- Audio Diagnostic Upload & Playback
- QR Repair Label Generator
- Calibration Reference Tool (spec charts, tolerances)

---

## Maintainers
Developed for Dylan Thompson by ArtisanClarinets GPT
MIT Licensed