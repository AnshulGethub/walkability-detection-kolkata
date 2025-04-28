import requests
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load CSV
data = pd.read_csv('kolkata_street_segments_500m.csv')

# Filter Segment_IDs 5001 to 10000
data_batch = data[(data['Segment_ID'] >= 20000) & (data['Segment_ID'] <= 22000)]

# Google Street View API Key
API_KEY =  🔁 Replace this API_KEY

# Image parameters20
IMAGE_SIZE = '600x400'
PITCH = 0
FOV = 90
RADIUS = 30
HEADING = 0

# Output directory for this batch
output_dir = 'kolkata_gsv_images_batch_5001_10000'
os.makedirs(output_dir, exist_ok=True)

# Function to download image if available
def process_point(row):
    lat = row['Latitude']
    lon = row['Longitude']
    segment_id = row['Segment_ID']

    # Step 1: Check availability via metadata API
    metadata_url = (
        f"https://maps.googleapis.com/maps/api/streetview/metadata?"
        f"location={lat},{lon}&radius={RADIUS}&key={API_KEY}"
    )
    meta_response = requests.get(metadata_url).json()

    if meta_response['status'] == 'OK':
        image_url = (
            f"https://maps.googleapis.com/maps/api/streetview?"
            f"size={IMAGE_SIZE}&location={lat},{lon}&heading={HEADING}&"
            f"pitch={PITCH}&fov={FOV}&radius={RADIUS}&key={API_KEY}"
        )
        response = requests.get(image_url)
        if response.status_code == 200:
            image_path = os.path.join(output_dir, f"{segment_id}.jpg")
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return f"✅ Downloaded Segment_ID {segment_id}"
        else:
            return f"⚠️ Failed to download Segment_ID {segment_id} (HTTP {response.status_code})"
    else:
        return f"❌ No image available for Segment_ID {segment_id} ({meta_response['status']})"

# Start parallel download
print("🚀 Starting batch 5001–10000 (10 downloads in parallel)...")
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_point, row) for _, row in data_batch.iterrows()]
    for future in as_completed(futures):
        print(future.result())

print("🎯 Batch 5001–10000 completed.")
