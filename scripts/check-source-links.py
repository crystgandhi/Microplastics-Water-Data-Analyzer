"""Audit the external links in the public HTML pages before deployment."""
import html
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def check(url):
    result = subprocess.run(
        ["curl", "-LsS", "--max-time", "12", "-o", os.devnull,
         "-w", "%{http_code}", url],
        capture_output=True, text=True,
    )
    return url, result.stdout, result.stderr.strip()


def main():
    root = Path(__file__).resolve().parent.parent
    pages = [root / "index.html", *sorted(root.glob("water-lookup-*.html"))]
    sources = {}
    for page in pages:
        # Study links can occur in HTML anchors or embedded record data.
        for match in re.findall(r'https?://[^\s"\'<>]+', page.read_text(encoding="utf-8")):
            sources.setdefault(html.unescape(match.rstrip(".")), set()).add(page.name)

    with ThreadPoolExecutor(max_workers=8) as pool:
        failures = 0
        for url, status, error in pool.map(check, sorted(sources)):
            if not status.startswith("2") or error:
                failures += 1
                pages_using_link = ", ".join(sorted(sources[url]))
                print(f"{status or 'Error'} {url} ({pages_using_link}) {error}")
    print(f"{len(sources)} URLs checked; {failures} need review.")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
