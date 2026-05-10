from PIL import Image
import os

def crop_assets(assets_dir):
    # Projects (3 panels vertically)
    projects = Image.open(os.path.join(assets_dir, 'projects.png'))
    w, h = projects.size
    p1 = projects.crop((0, 0, w, h//3))
    p2 = projects.crop((0, h//3, w, 2*h//3))
    p3 = projects.crop((0, 2*h//3, w, h))
    p1.save(os.path.join(assets_dir, 'project_hockey.png'))
    p2.save(os.path.join(assets_dir, 'project_genesis.png'))
    p3.save(os.path.join(assets_dir, 'project_mechanic.png'))

    # Icons (Grid of 3x3 roughly)
    icons = Image.open(os.path.join(assets_dir, 'icons_all.png'))
    # Controller, VR, Rocket
    # Chat, Target, Code
    # Target2, Lab, Star
    iw, ih = icons.size
    grid_w = iw // 3
    grid_h = ih // 3
    
    icon_names = [
        "icon_game.png", "icon_vr.png", "icon_rocket.png",
        "icon_chat.png", "icon_plan.png", "icon_code.png",
        "icon_test.png", "icon_lab.png", "star.png"
    ]
    
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            if idx < len(icon_names):
                icon = icons.crop((j * grid_w, i * grid_h, (j + 1) * grid_w, (i + 1) * grid_h))
                icon.save(os.path.join(assets_dir, icon_names[idx]))
                print(f"Saved {icon_names[idx]}")

if __name__ == "__main__":
    crop_assets('/Users/pratibhayadav/assigment/assigment3/task3/assets')
