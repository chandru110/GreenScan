def process_barcode(barcode_data):
    """Process and display the barcode data."""
    print(f"Scanned barcode: {barcode_data}")

def scan_barcode_from_input():
    """Scan barcodes from keyboard input (used with barcode scanner)."""
    print("Scan a barcode (type 'stop' to exit):")
    while True:
        barcode_data = input().strip()
        if barcode_data.lower() == 'stop':
            print("Stopping barcode scanner...")
            break
        if barcode_data:
            process_barcode(barcode_data)

if __name__ == "__main__":
    scan_barcode_from_input()
