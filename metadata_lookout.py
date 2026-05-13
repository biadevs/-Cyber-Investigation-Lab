from PIL import Image
from PIL.ExifTags import TAGS
import datetime

def extract_metadata(image_path):
    print(f"--- INVESTIGATION REPORT: {image_path} ---")
    print(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        image = Image.open(image_path)
        # Extracting the Exif data
        info = image._getexif()
        
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                print(f"{decoded:25}: {value}")
        else:
            print("No Exif metadata found. (The suspect may have 'scrubbed' the file!)")

    except Exception as e:
        print(f"Error: {e}")

# Run the extractor
extract_metadata("suspect_photo.jpg")

"""
DAY 11 LOG:
Investigating hidden Exif metadata. 
This is critical for geographical tracking and device identification in forensic cases.
"""
