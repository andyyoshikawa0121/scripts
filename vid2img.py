import cv2
import os
import glob
from tqdm import tqdm
import yaml


def save_all_frames(vid_path, dir_path, ext='jpg'):
    cap = cv2.VideoCapture(vid_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{dir_path}/img_{str(n).zfill(digit)}.{ext}', frame)
            n += 1
        else:
            return


if __name__ == '__main__':
    with open("./config.yaml") as f:
        args = yaml.safe_load(f)

    vid_dir = args["vid_dir"]
    vid_ext = args["vid_ext"]
    img_dir = args["img_dir"]
    img_ext = args["img_ext"]

    files = glob.glob(f'{vid_dir}/*.{vid_ext}')

    for index, file in enumerate(tqdm(files)):
        basedir = f'{img_dir}/vid_{str(index).zfill(5)}'
        save_all_frames(file, basedir, ext=img_ext)
