import requests
import json
import datetime
from yaml_loader import yaml_loader


def post_slack(data):
    args = yaml_loader()
    webhook_url = args['SlackHandler']['webhook_url']
    res = requests.post(webhook_url, data=data)
    print(res)

def create_attachments(pretext, color, params):
  data = {
    "attachments": [
      {
        "pretext": pretext,
        "color": color,
        "fields": []
      }
    ]
  }
  # データがある場合のみ追加
  if params:
    keys = params.keys()
    for key in keys:
      if params[key] == "":
        add_data = {
          "title": key,
          "short": False,
        }
        data["attachments"][0]["fields"].append(add_data)
      else:
        add_data = {
          "value": f'{key}: {params[key]}',
          "short": False,
        }
        data["attachments"][0]["fields"].append(add_data)
  
  return json.dumps(data)


if __name__ == '__main__':
    args = yaml_loader()
    blue = args['SlackHandler']['blue']

    post_params = {
      "Continue Copying": "",
      "Model": "MoCoGAN-HD",
      "Iterations": "50000",
      "FID": "20.3",
      "Time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    data = create_attachments("Study Finish Notification", blue, post_params)
    res = post_slack(data)