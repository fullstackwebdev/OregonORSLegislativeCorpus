# Oregon ORS Legislative Corpus

## Overview

This repository contains a comprehensive corpus of the Oregon Revised Statutes (ORS). It's a valuable resource for legal professionals, researchers, and anyone interested in analyzing Oregon law using computational methods.

## Corpus Description

This corpus is a collection of legal texts from the Oregon Revised Statutes, making it a domain-specific legal corpus. It has several beneficial features:

1. **Domain-specific**: Focused on Oregon law
2. **Structured**: Contains metadata like ORS number, chapter, title, etc.
3. **Machine-readable**: Stored in JSONL (JSON Lines) format

## Data Format

The corpus is stored in a JSONL (JSON Lines) file, where each line is a valid JSON object. Each object represents a statute and contains the following fields:

- `url`: The URL of the statute
- `page_id`: A unique numerical identifier
- `content`: The full text of the statute
- `ors`: The ORS (Oregon Revised Statute) number
- `chapter`: The chapter number
- `title`: The title number
- `volume`: The volume number

## Usage

Here's an example of how to load and use the corpus in Python:

```python
import json
import gzip

# Load the corpus
corpus = []
with gzip.open('output.jsonl.gz', 'rt', encoding='utf-8') as file:
    for line in file:
        corpus.append(json.loads(line))

# Example: Print the first 5 ORS numbers
for statute in corpus[:5]:
    print(statute['ors'])

# Example: Find all statutes in Chapter 10
chapter_10 = [statute for statute in corpus if statute['chapter'] == '10']
print(f"Number of statutes in Chapter 10: {len(chapter_10)}")

# Example: Search for a keyword in the content
keyword = "property"
matching_statutes = [statute for statute in corpus if keyword in statute['content'].lower()]
print(f"Number of statutes containing '{keyword}': {len(matching_statutes)}")
```

## Potential Applications

This corpus can be used for various purposes, including:

1. Legal research and analysis
2. Natural Language Processing tasks focused on legal text
3. Information retrieval systems for legal documents
4. Studying legal language and terminology
5. Training machine learning models for legal text understanding or generation

## Contributing

Contributions to improve the corpus or add analysis tools are welcome. Please submit a pull request or open an issue to discuss potential changes.

## License

[Include information about the license here]

## Acknowledgments

- Oregon State Legislature for making the statutes publicly available
- [Any other acknowledgments]

## Contact

[Your contact information or preferred method of contact]

---

We hope this corpus proves to be a valuable resource for your legal research and analysis needs. If you have any questions or suggestions, please don't hesitate to reach out or open an issue in this repository.
