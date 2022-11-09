import os
import glob
from tqdm import tqdm
import random
import shutil

from yaml_loader import yaml_loader
from slack_handler import create_attachments, post_slack


if __name__ == '__main__':
  args = yaml_loader()

  vid_dir = args['vid_dir']
  sample_dir = args['sample_dir']
  vid_ext = args['vid_ext']
  num_sample_vid_ratio = args['num_sample_vid_ratio']

  files = glob.glob(f'{vid_dir}*.{vid_ext}')
  num_vid = len(files)
  num_sample = int(num_vid / num_sample_vid_ratio)
  sample_files = random.sample(files, num_sample)
  try:
    for index, file in enumerate(tqdm(sample_files)):
      if index % int(sample_files / 10) == 0:
        post_params = [
          {
            "is_title": True,
            "name": "Continue Copying",
            "value": "",
          },
          {
            "is_title": False,
            "name": "Total",
            "value": f"{index}/{sample_files}",
          }
        ]
        data = create_attachments("Process Notify", args["SlackHandler"]["green"], post_params)
        post_slack(data)
      if os.path.exists(sample_dir):
        shutil.copy(file, sample_dir)
  except Exception as e:
    error_params = [
      {
        "is_title": False,
        "name": "Error",
        "value": e,
      }
    ]
    data = create_attachments("", args["SlackHandler"]["red"], error_params)
    post_slack(data)

  post_params = [
    {
      "is_title": True,
      "name": "Finish!",
      "value": "",
    }
  ]
  data = create_attachments("", args["SlackHandler"]["blue"], post_params)
  post_slack(data)


