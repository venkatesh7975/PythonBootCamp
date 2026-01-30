import pdfplumber

pdf_path = "python cheat sheets (2).pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        print("Metadata:")
        for key, value in pdf.metadata.items():
            print(f"{key}: {value}")
except Exception as e:
    print(f"Error: {e}")
