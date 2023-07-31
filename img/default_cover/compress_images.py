from PIL import Image
import os

if __name__=='__main__':
    # List files of current directory
    files = os.listdir()
    # Iterate over JPG files
    for file in files:
        if os.path.isdir(file):
            continue
        size = os.path.getsize(file)
        if (file.endswith('.jpg') or file.endswith('.png')) and size >= 512 * 1024: # 512 KB
            img = Image.open(file)
            img = img.convert('RGB')
            img.save(file + '_compressed.jpg', optimize=True, quality=80)
            img.close()
            # Rename
            os.remove(file)
            os.rename(file + '_compressed.jpg', file.replace('.png', '.jpg'))