import csv
import requests
from bs4 import BeautifulSoup


def audit_url(url):
    """Run basic technical SEO checks for a single URL."""

    result = {
        "URL": url,
        "Status Code": "",
        "Final URL": "",
        "Title": "",
        "Title Length": 0,
        "Meta Description": "",
        "Meta Description Length": 0,
        "H1": "",
        "Canonical": "",
        "Meta Robots": "",
    }

    try:
        response = requests.get(
            url,
            timeout=15,
            allow_redirects=True,
            headers={
                "User-Agent": "Technical-SEO-Audit-Toolkit/1.0"
            },
        )

        result["Status Code"] = response.status_code
        result["Final URL"] = response.url

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return result

        soup = BeautifulSoup(response.text, "html.parser")

        # Page title
        if soup.title:
            title = soup.title.get_text(strip=True)
            result["Title"] = title
            result["Title Length"] = len(title)

        # Meta description
        meta_description = soup.find(
            "meta", attrs={"name": "description"}
        )

        if meta_description and meta_description.get("content"):
            description = meta_description["content"].strip()
            result["Meta Description"] = description
            result["Meta Description Length"] = len(description)

        # First H1
        h1 = soup.find("h1")

        if h1:
            result["H1"] = h1.get_text(" ", strip=True)

        # Canonical URL
        canonical = soup.find(
            "link", attrs={"rel": lambda value: value and "canonical" in value}
        )

        if canonical and canonical.get("href"):
            result["Canonical"] = canonical["href"]

        # Meta robots
        robots = soup.find(
            "meta", attrs={"name": "robots"}
        )

        if robots and robots.get("content"):
            result["Meta Robots"] = robots["content"]

    except requests.RequestException as error:
        result["Status Code"] = f"ERROR: {error}"

    return result


def run_audit(input_file="sample_urls.csv", output_file="sample_output.csv"):

    results = []

    with open(input_file, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            url = row.get("URL", "").strip()

            if not url:
                continue

            print(f"Auditing: {url}")

            results.append(audit_url(url))

    if not results:
        print("No URLs found.")
        return

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nAudit complete. Results saved to {output_file}")


if __name__ == "__main__":
    run_audit()
