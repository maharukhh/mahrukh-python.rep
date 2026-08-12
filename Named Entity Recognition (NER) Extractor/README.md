# Named Entity Recognition (NER) Extractor (Rule-Based)

Extracts likely dates, organizations, locations, and person/place names from text using regex patterns and capitalization heuristics — no external model downloads required.

## How It Works
1. **Dates** are found with a regex pattern matching common formats (e.g. "5 August 2026", "August 5, 2026", "5/8/2026").
2. **Capitalized phrases** (sequences of consecutive capitalized words) are extracted as candidate proper nouns.
3. Each candidate phrase is classified by simple heuristics:
   - Ends in a known organization suffix (Inc, Corp, Ltd, University, etc.) → **ORGANIZATION**
   - Contains a location-related word (city, street, county, etc.) → **LOCATION**
   - Otherwise, short capitalized phrases are labeled **PERSON/PLACE** (ambiguous without a trained model)


## Requirements
- Python 3.x (standard library only — no installs needed)

Type or paste a sentence/paragraph. Type `quit` to exit.

## Notes & Limitations
- This is a **rule-based** approach — it will miss entities that don't follow expected capitalization/formatting, and can misclassify ambiguous phrases (e.g. it can't reliably tell a person's name from a place name without more context).
- Production NER systems typically use a trained model (e.g. spaCy's pretrained pipelines) that has learned entity patterns from large labeled corpora — this demo trades that accuracy for being fully offline and dependency-free.

## Possible Extensions
- Swap in spaCy's pretrained NER model (`pip install spacy` + download a language model) for much higher accuracy.
- Add more entity types (money amounts, percentages, product names).
- Add confidence scoring for ambiguous PERSON/PLACE classifications.
