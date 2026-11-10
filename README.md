# Grocery Store Receipt Parser
An OCR pipeline that extracts and structures text from Swedish grocery receipts, built as a first hands-on project in computer vision and OCR.

## What it does
Given a photo of a receipt, the pipeline:
1. Runs OCR (EasyOCR, Swedish + English) to detect and read all text on the image
2. Extracts the bounding box coordinates of each detected text fragment
3. Sorts fragments top-to-bottom, left-to-right based on their position
4. Groups fragments that share a similar vertical position into single receipt lines

The result is a list of human-readable lines reconstructing the receipt's original layout.

A simple **Gradio web interface** wraps the pipeline: upload a receipt photo in the browser, get the parsed text back immediately — no code required.

## Example output
Ica supermarket
Datun Fors [el . 046-2118370 2009-01-31 8027 Ka Tid 2148 18.39
Beer 2,8x burk 0,50 6,50
Pant 287xgr€
'69,9Okr /ka 55,71
Kasear  Kolontal Kavlar Knackebrod Btbart Tarok IcA 12,50 2 25 15.90 8
Lattdcyck Citron Lok Vit onka atbort 2st*3,90 7,80 7,90
Mossnor Fjal Ib 18,90
Morot IcA_ 5,00
ENud ar blffsmak 3st*4,90 70
Rabatt Papr #Nud kaRod/GuI  ICA ar kyck Nudl ar smek 4st 15kr 10,00 60
astkasse 50
Russin 'pack 12,90
Standaran jolk 8,50
Sylta ICA 200g 90
Ägg Guidgula 23,90
App 0-svenskt 5,73
Total 281 29
12,00 Erha) Jen rabatt; 25,Do Monsk 29,98 Mons 0,30 4,60 249,81 Netto 1,20 279 ,79 Brutto 1,50



## Tech stack
- **OpenCV** — image preprocessing (grayscale conversion, global and adaptive thresholding)
- **EasyOCR** — pretrained text detection and recognition
- **PyTorch** — used both as EasyOCR's backend and separately, to train a first classifier (MNIST) as a learning exercise
- **Gradio** — web interface for uploading a receipt and viewing the parsed output
- **NumPy** — coordinate math and array manipulation

## Project structure
grocery store receipt parser/
├── data/
│ ├── raw/ # sample receipt photos (not all committed)
│ └── samples/ # a few examples for demonstration
├── pipeline.py # core functions: extract_text, to_sorted_items, group_into_lines
├── main.py # runs the pipeline on a single hardcoded receipt (for quick testing)
├── app.py # Gradio web interface
├── requirements.txt
└── README.md

## Current limitations

- OCR accuracy on this specific thermal-printer font isn't perfect — EasyOCR occasionally merges adjacent lines, misreads characters, or (on lower-quality photos) hallucinates entirely wrong words. This is a general-purpose model, not fine-tuned on receipt fonts.
- Image quality matters a lot: crumpled, blurry, or poorly lit receipts produce noticeably worse output than a clean, well-lit photo.
- The vertical-grouping threshold (10px) is fixed and tuned for one receipt's resolution; it may need adjustment for receipts of different sizes.
- Field parsing (extracting store name, date, total, individual items as structured data) is not yet implemented — the pipeline currently outputs readable text lines, not a structured object.

## Potential improvements

- Fuzzy-match recognized words against a vocabulary of known receipt terms (store names, "Total", "Moms", common product names) using edit distance (e.g. via `rapidfuzz`) to correct OCR misreadings
- Parse structured fields (store, date, line items, total) from the grouped lines using regex and a `Receipt` data model
- Add tests and package with Docker for a proper deployment
- Fine-tune a custom character recognition model on synthetic + real receipt data to improve accuracy on this specific font

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run once on a hardcoded receipt:
python main.py

# Or launch the web interface:
python app.py
```
