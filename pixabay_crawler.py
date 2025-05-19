import json
import pixabay.core
import os
import time
import random

config = json.load(open('./pixabay_config.json', 'r'))
API_KEY = config['pixabay_api_key']
MAX_IMAGES = config.get('max_images', 500)  # Default to 500 if not specified

save_root = config['save_root']

keywords_file = open(config['keywords_file'], 'r')
keywords_tag_dic = json.load(keywords_file)
keywords = keywords_tag_dic.keys()

pb = pixabay.core(API_KEY)

for ikeyword in keywords:
    im_dir = os.path.join(save_root, 'Img', ikeyword)
    os.makedirs(im_dir, exist_ok=True)

    images_processed = 0
    for ipage in range(1, config['npage'] + 1):
        if images_processed >= MAX_IMAGES:
            break
            
        # Searching
        try:
            photos = pb.query(keywords_tag_dic[ikeyword])
            
            # download images
            for photo in photos:
                if images_processed >= MAX_IMAGES:
                    break
                    
                try:
                    # Download the image
                    image_path = os.path.join(im_dir, f"{photo.getId()}.jpg")
                    photo.download(image_path, "largeImage")
                    print(f"Downloaded image {images_processed + 1} for keyword '{ikeyword}'")
                    
                    images_processed += 1
                    time.sleep(3 * random.random())

                except Exception as e:
                    print(f'Error processing photo: {str(e)}')
                    continue

        except Exception as e:
            print(f'Error searching Pixabay: {str(e)}')
            continue