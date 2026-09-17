# Technical SEO Audit Checklist

A practical checklist for reviewing the technical SEO health of a website.

This checklist can be used alongside the automated checks in this repository and tools such as Screaming Frog SEO Spider and Google Search Console.

## 1. Crawlability

- [ ] Important URLs return the expected HTTP status code
- [ ] No unnecessary redirect chains
- [ ] Broken internal links are identified
- [ ] Robots.txt is accessible
- [ ] Important sections are not accidentally blocked
- [ ] Internal links allow search engines to discover key pages

## 2. Indexability

- [ ] Important pages are indexable
- [ ] Meta robots directives are reviewed
- [ ] No important pages contain accidental `noindex` directives
- [ ] Google Search Console indexing reports are reviewed
- [ ] Duplicate or low-value URLs are evaluated
- [ ] Indexed URLs match the intended site structure

## 3. Canonicalization

- [ ] Canonical tags are present where appropriate
- [ ] Canonicals point to the preferred URL
- [ ] Important pages do not canonicalize to unrelated URLs
- [ ] HTTP/HTTPS and www/non-www versions are consistent
- [ ] Duplicate URL variations are handled correctly

## 4. XML Sitemap

- [ ] XML sitemap is accessible
- [ ] Sitemap contains indexable canonical URLs
- [ ] Redirected and broken URLs are excluded
- [ ] No `noindex` URLs are included
- [ ] Sitemap is submitted in Google Search Console

## 5. Status Codes & Redirects

- [ ] Important pages return 200 status codes
- [ ] Permanent redirects use appropriate 301 responses
- [ ] Redirect chains are minimized
- [ ] Redirect loops are identified
- [ ] 404 pages are reviewed
- [ ] Internal links point directly to final URLs where possible

## 6. On-Page Technical Elements

- [ ] Each important page has a relevant title
- [ ] Missing and duplicate titles are identified
- [ ] Meta descriptions are reviewed
- [ ] H1 headings are present where appropriate
- [ ] Duplicate H1s are investigated where relevant
- [ ] URLs are descriptive and consistent

## 7. Internal Linking

- [ ] Important pages receive internal links
- [ ] Orphan pages are investigated
- [ ] Broken internal links are fixed
- [ ] Anchor text provides useful context
- [ ] Internal links point to canonical URLs

## 8. Structured Data

- [ ] Relevant schema markup is implemented
- [ ] Structured data is valid
- [ ] Schema matches visible page content
- [ ] Required properties are present
- [ ] Google rich result eligibility is reviewed where applicable

## 9. Page Experience

- [ ] Mobile usability is reviewed
- [ ] Core Web Vitals are monitored
- [ ] Large images and resources are optimized
- [ ] Important templates are tested for performance issues

## 10. Final Validation

After fixes are implemented:

- [ ] Re-crawl the website
- [ ] Recheck important URLs manually
- [ ] Validate redirects
- [ ] Validate canonicals
- [ ] Validate robots directives
- [ ] Resubmit or verify sitemap if necessary
- [ ] Monitor Google Search Console for changes

---

## Recommended Tools

- Screaming Frog SEO Spider
- Google Search Console
- Google Analytics 4
- PageSpeed Insights
- Rich Results Test
- Ahrefs / Semrush
- This Technical SEO Audit Toolkit

---

Created as part of the **Technical SEO Audit Toolkit** by Fawad Abbas.
