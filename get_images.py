import requests
import os
from pathlib import Path
from tqdm import tqdm

def download_coco_image(image_id, save_dir="coco_images", file_ext="jpg"):
    """
    Downloads a COCO image given its ID.
    
    Args:
        image_id (str): Image ID (e.g., "000000000389")
        save_dir (str): Directory to save images
        file_ext (str): File extension of the image
    """

    save_path = Path(save_dir)
    save_path.mkdir(exist_ok=True)
    
    url = f"http://images.cocodataset.org/train2017/{image_id}.jpg"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        output_path = save_path / f"{image_id}.{file_ext}"
        with open(output_path, "wb") as f:
            f.write(response.content)
        # print(f"Downloaded: {output_path}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {image_id}: {e}")

if __name__ == "__main__":

    with open("image_filenames.txt", 'r') as file:
        image_names = file.read().splitlines()

    for image in tqdm(image_names):
        download_coco_image(image, save_dir="trial")
