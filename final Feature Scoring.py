
import os
import pandas as pd

# Constants
label_dir = 🔁 Replace this Label path 
class_names = [ 'encroachment', 'footpaths', 'streetlights', 'tree']
image_size = 416  # assuming square image used during detection

data = []

for file in os.listdir(label_dir):
    if file.endswith(".txt"):
        file_path = os.path.join(label_dir, file)
        image_name = file.replace(".txt", "")
        
        # Initialize values
        tree_area_sum = 0.0
        has_streetlight = 0.0
        has_footpath = 0.0
        has_encroachment = 0.0
        
        with open(file_path, "r") as f:
            for line in f.readlines():
                parts = line.strip().split()
                class_id = int(parts[0])
                width = float(parts[3])
                height = float(parts[4])
                area = width * height  # normalized area
                
                if class_id == 4:  # tree
                    tree_area_sum += area
                elif class_id == 3:  # streetlight
                    has_streetlight += area
                elif class_id == 2:  # footpath
                    has_footpath += area
                elif class_id == 1:  # encroachment
                    has_encroachment += area
        
        # Total image area in normalized units is 1.0 (since width and height are normalized)
        score_tree = tree_area_sum
        score_streetlight = has_streetlight
        score_footpath = has_footpath
        score_encroachment = has_encroachment

        data.append({
            "image": image_name,
            "tree_score": round(score_tree, 3),
            "streetlight_score": score_streetlight,
            "footpath_score": score_footpath,
            "encroachment_score": score_encroachment
        })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("feature_scores_per_image.csv", index=False)

print("✅ Saved feature scores to 'feature_scores_per_image_2.csv'")
