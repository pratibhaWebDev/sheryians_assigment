from PIL import Image
import os

def crop_assets(assets_dir):
    # Crop variants (3 bags in one image)
    variants = Image.open(os.path.join(assets_dir, 'variants.png'))
    w, h = variants.size
    # 3 bags horizontally
    bag1 = variants.crop((0, 0, w//3, h))
    bag2 = variants.crop((w//3, 0, 2*w//3, h))
    bag3 = variants.crop((2*w//3, 0, w, h))
    bag1.save(os.path.join(assets_dir, 'bag_black.png'))
    bag2.save(os.path.join(assets_dir, 'bag_yellow.png'))
    bag3.save(os.path.join(assets_dir, 'bag_orange.png'))

    # Crop flavor icons
    icons = Image.open(os.path.join(assets_dir, 'flavor_icons.png'))
    iw, ih = icons.size
    # 3 icons horizontally
    chili = icons.crop((0, 0, iw//3, ih))
    beef = icons.crop((iw//3, 0, 2*iw//3, ih))
    smoke = icons.crop((2*iw//3, 0, iw, ih))
    chili.save(os.path.join(assets_dir, 'icon_chili.png'))
    beef.save(os.path.join(assets_dir, 'icon_beef.png'))
    smoke.save(os.path.join(assets_dir, 'icon_smoke.png'))

if __name__ == "__main__":
    crop_assets('/Users/pratibhayadav/assigment/assigment3/task2/assets')
