from PIL import Image
from pillow_heif import register_heif_opener
import argparse
import os

register_heif_opener()

parser = argparse.ArgumentParser()
parser.add_argument('input_path', type=str)
parser.add_argument('output_path', type=str)
args = parser.parse_args()

files = []
isdir = True
if os.path.isdir(args.input_path):
    _files = sorted(os.listdir(args.input_path))
    for f in _files:
        if f.lower().endswith('.heic'):
            files.append(f)
else:
    isdir = False
    files.append(args.input_path)
for file in files:
    if isdir:
        img = Image.open(os.path.join(args.input_path, file))
        target_path = os.path.join(args.output_path, os.path.splitext(file)[0] + '.jpg')
    else:
        img = Image.open(args.input_path)
        target_path = args.output_path
    exif = img.info.get('exif')
    icc_profile = img.info.get('icc_profile')
    img.save(target_path, exif=exif, icc_profile=icc_profile)