from PIL import Image
import os

def crop_icons(input_path, output_dir):
    img = Image.open(input_path)
    # The icons are arranged horizontally
    # Grid is 1024x1024
    # Icons: Search, Bag, User, Heart
    
    icons = [
        (40, 380, 275, 620, "search.png"),
        (285, 380, 520, 620, "bag.png"),
        (530, 380, 765, 620, "user.png"),
        (775, 380, 1010, 620, "heart.png")
    ]
    
    for x1, y1, x2, y2, name in icons:
        crop = img.crop((x1, y1, x2, y2))
        crop.save(os.path.join(output_dir, name))
        print(f"Saved {name}")

if __name__ == "__main__":
    crop_icons('/Users/pratibhayadav/.gemini/antigravity/brain/389e6300-f0ce-43d0-9239-d2e1dcca298b/nft_icons_1778409528650.png', '/Users/pratibhayadav/assigment/assigment3/task1/assets')
