import requests
import json
import yaml
import datetime


def slack(data, webhook_url):
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

def process_notify(time, index, modelname):
  with open('./config.yaml') as f:
    args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    data = json.dumps({
      "attachments": [
        {
          "pretext": "Study Notification.",
          "color": "#AAFFAA",
          "fields": [
            {
              "title": "Parameters",
              "short": False,
            },
            {
              "value": f"Model: {modelname}",
              "short": False,
            },
            {
              "value": f"Iterations: {index}",
              "short": False,
            },
            {
              "value": f"Time: {time}",
              "short": False,
            },
          ]
        }
      ]
    })
    slack(data, webhook_url)
  
def error_notify(error, modelname):
  with open('./config.yaml') as f:
    args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    data = json.dumps({
      "attachments": [
        {
          "pretext": "Error occurred",
          "color": "#E60033",
          "fields": [
            {
              "title": "Error",
              "short": False,
            },
            {
              "value": f"Model: {modelname}",
              "short": False,
            },
            {
              "value": error,
              "short": False,
            }
          ] 
        }
      ]
    })
    slack(data, webhook_url)

def finish_notify(modelname):
  with open('./config.yaml') as f:
    args = yaml.safe_load(f)
  
  webhook_url = args['SlackHandler']['webhook_url']
  
  data = json.dumps({
    "attachments": [
      {
        "pretext": "Study Finished",
        "color": "#00BFE6",
        "fields": [
          {
            "title": "Finish",
            "short": False,
          },
          {
            "value": f"Model: {modelname}",
            "short": False,
          },
        ]
      }
    ]
  })
  slack(data, webhook_url)


if __name__ == '__main__':
    with open('./config.yaml') as f:
        args = yaml.safe_load(f)

    webhook_url = args['SlackHandler']['webhook_url']

    # requests.post(webhook_url, data=json.dumps({
    #     "text": f"Test Post from Python",
    # }))

    # process_notify(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 100, "MoCoGAN-HD")
    # error_notify('Segmentation Fault', "MoCoGAN-HD")
    # finish_notify("MoCoGAN-HD")

    # post_params = [
    #   {
    #     "is_title": True,
    #     "name": "Study Finished",
    #     "value": "",
    #   },
    #   {
    #     "is_title": False,
    #     "name": "Model",
    #     "value": "MoCoGAN-HD",
    #   },
    #   {
    #     "is_title": False,
    #     "name": "Iterations",
    #     "value": "50000",
    #   },
    #   {
    #     "is_title": False,
    #     "name": "FID",
    #     "value": "20.3",
    #   },
    #   {
    #     "is_title": False,
    #     "name": "Time",
    #     "value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #   }
    # ]
    # data = create_attachments("Study Finish Notification", "#00BFE6", post_params)
    # res = slack(data, webhook_url)