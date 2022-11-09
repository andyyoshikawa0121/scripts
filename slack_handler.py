import requests
import json
import yaml
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
    for param in params:
      if param["is_title"]:
        add_data = {
          "title": param["name"],
          "short": False,
        }
        data["attachments"][0]["fields"].append(add_data)
      else:
        add_data = {
          "value": f'{param["name"]}: {param["value"]}',
          "short": False,
        }
        data["attachments"][0]["fields"].append(add_data)
  
  return json.dumps(data)


if __name__ == '__main__':
    # args = yaml_loader()
    # webhook_url = args['SlackHandler']['webhook_url']

    # requests.post(webhook_url, data=json.dumps({
    #     "text": f"Test Post from Python",
    # }))

    # process_notify(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 100, "MoCoGAN-HD")
    # error_notify('Segmentation Fault', "MoCoGAN-HD")
    # finish_notify("MoCoGAN-HD")

    post_params = [
      {
        "is_title": True,
        "name": "Study Finished",
        "value": "",
      },
      {
        "is_title": False,
        "name": "Model",
        "value": "MoCoGAN-HD",
      },
      {
        "is_title": False,
        "name": "Iterations",
        "value": "50000",
      },
      {
        "is_title": False,
        "name": "FID",
        "value": "20.3",
      },
      {
        "is_title": False,
        "name": "Time",
        "value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      }
    ]
    data = create_attachments("Study Finish Notification", "#00BFE6", None)
    res = post_slack(data)