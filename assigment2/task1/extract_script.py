from PIL import Image
import os

def get_bbox_with_threshold(img, threshold=20):
    gray = img.convert('L')
    binary = gray.point(lambda p: 255 if p > threshold else 0)
    return binary.getbbox()

def extract_elements(input_path, output_dir):
    img = Image.open(input_path).convert('RGB')
    
    # 1. Logo
    logo = img.crop((0, 0, 300, 150))
    lb = get_bbox_with_threshold(logo)
    if lb:
        img.crop((lb[0], lb[1], lb[2], lb[3])).save(os.path.join(output_dir, 'logo.png'))

    # 2. Blog Images (Precise)
    # Martini
    img.crop((54, 448, 478, 733)).save(os.path.join(output_dir, 'image_martini.png'))
    # Chair
    img.crop((493, 448, 917, 733)).save(os.path.join(output_dir, 'image_chair.png'))
    # Cat
    img.crop((931, 448, 1355, 733)).save(os.path.join(output_dir, 'image_cat.png'))
    
    # 3. Category Tags (Inside cards)
    img.crop((71, 755, 125, 785)).save(os.path.join(output_dir, 'tag_tech.png'))
    img.crop((510, 755, 570, 785)).save(os.path.join(output_dir, 'tag_saas.png'))
    img.crop((948, 755, 1030, 785)).save(os.path.join(output_dir, 'tag_marketing.png'))

    print("All images extracted successfully.")

if __name__ == "__main__":
    os.makedirs('/Users/pratibhayadav/assigment/task1/extracted_images', exist_ok=True)
    extract_elements('/Users/pratibhayadav/assigment/task1/image.png', '/Users/pratibhayadav/assigment/task1/extracted_images')
