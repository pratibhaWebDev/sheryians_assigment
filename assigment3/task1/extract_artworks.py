from PIL import Image
import os

def extract_artworks(input_path, output_dir):
    img = Image.open(input_path).convert('RGB')
    width, height = img.size
    
    names = [
        "monocular", "horns_mask", "light_moon", "skull_wire",
        "spiderman", "deadpool", "white_eye", "plastic_spinal"
    ]
    
    # Precise centers for the artwork squares based on visual inspection
    centers = [
        (163, 240), (442, 240), (722, 240), (1002, 240),
        (163, 715), (442, 715), (722, 715), (1002, 715)
    ]
    
    # Each artwork is roughly 220x220
    size = 224 // 2
    
    for i, (cx, cy) in enumerate(centers):
        # Add a small buffer to include the white border
        crop = img.crop((cx - size, cy - size, cx + size, cy + size))
        crop.save(os.path.join(output_dir, f"{names[i]}.png"))
        print(f"Saved {names[i]}.png at center ({cx}, {cy})")

if __name__ == "__main__":
    os.makedirs('/Users/pratibhayadav/assigment/assigment3/task1/crops', exist_ok=True)
    extract_artworks('/Users/pratibhayadav/assigment/assigment3/task1/image.png', '/Users/pratibhayadav/assigment/assigment3/task1/crops')
