# Microplastics Water Data Analyzer

The **Browse Records** edition is a browser-based research tool for exploring published microplastic measurements from selected U.S. waterways. It brings study results and sampling details together so readers can find measurements, interpret them in context, and trace them to the original sources.

## Browse the records

- Find study records by state and water body.
- Review reported measurements, units, and sample types, including water and sediment.
- Check sampling dates, collection methods, particle size ranges, and quality-control notes where available.
- Follow links to the original studies and data releases.

When comparing records, check the sample type, unit, particle size range, and sampling method. For example, particles per square kilometer describes abundance over a surface area, while particles per liter describes concentration in a volume of water. The records reflect the sites and dates sampled in the cited studies.

## Run locally

With Python 3 installed, open a terminal in the folder containing `index.html` and run:

```bash
python -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser. On Windows, use `py -m http.server 8000` if your Python installation uses the `py` launcher.

## Deployment

The Browse Records edition is intended for static hosting on Cloudflare Pages. Deploy the folder containing `index.html` and its supporting assets, preserving their relative paths.

## Data sources and citation

When using a measurement in a report or publication, cite the original study or data release linked in the record. Follow the source’s reuse terms for third-party data, figures, and images.

## License

Original project code is released under the MIT License. See [LICENSE](LICENSE). Third-party materials are subject to their respective source terms.
