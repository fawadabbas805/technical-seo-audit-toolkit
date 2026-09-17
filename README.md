# Technical SEO Audit Toolkit

A practical Python-based Technical SEO toolkit for auditing URLs and identifying common crawling, indexing, metadata, canonicalization, redirect, and on-page SEO issues.

This project demonstrates how technical SEO checks can be automated and organized to support website audits alongside tools such as Screaming Frog SEO Spider and Google Search Console.

## 🔍 What This Toolkit Checks

The current audit script analyzes:

- HTTP status codes
- Redirected/final URLs
- Page titles
- Title length
- Meta descriptions
- Meta description length
- H1 headings
- Canonical URLs
- Meta robots directives

The results are automatically exported to a CSV file for further analysis.

## 📁 Project Structure

```text
technical-seo-audit-toolkit/
│
├── docs/
│   └── technical-seo-checklist.md
├── README.md
├── requirements.txt
├── sample_urls.csv
├── sample_output.csv
└── seo_audit.py
