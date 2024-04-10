# import requests
import json
import os, time
import sys, ast

pipeline_configs = os.getenv('CONFIG')
print (pipeline_configs)
pipeline_configs = ast.literal_eval(pipeline_configs)

print(pipeline_configs)

# pipeline_configs_deatails = []
# for config in pipeline_configs:
#     for key ,value in config.items():
#       defination_id = key
#       artifect_id = value
#       print (defination_id, artifect_id)
#       pipeline_configs_deatails.append({"defination_id": defination_id, "artifect_id": artifect_id })

# print("--------")
# print(pipeline_configs_deatails)

# release_ids = []

# def trigger_release_pipeline(defination_id, artifect_id):
#   #  return release_id
#   return 11

# for pipeline_config in pipeline_configs_deatails:
#   defination_id, artifect_id = pipeline_config['defination_id'], pipeline_config['artifect_id']
#   release_id = trigger_release_pipeline(defination_id, artifect_id)
#   release_ids.append(release_id)

# print (release_ids)


# session = requests.Session()

# url = "https://dev.azure.com/ajaycs1991/ajaycs1991/_apis/pipelines/1?api-version=7.1-preview.1"

# auth = session.get(url)

# payload = json.dumps({
#   "templateParameters": {
#     "name": "ac"
#   }
# })

# headers = {
#   'Content-Type': 'application/json',
# }

# response = session.post(url, headers=headers, data=payload)

# print("Here is the output")

# print(response.text)

# # we'll call GET Release API to get the information of above release.


# response = session.post(url, headers=headers, data=payload)



# release_id = 2323
# auth = session.post(url)

# def get_release_status(release_id):
#     url = f"https://vsrm.dev.azure.com/AmericanAirlines/AirportStaffManagement/_apis/release/releases/{release_id}?api-version=7.1-preview.8"
#     response = session.get(url, headers=headers)
#     return response
    

# retry = 5
# status = ""

# while len(release_ids) > 0:
#   for release_id in release_ids:
#     response = get_release_status(release_id)
#     json_res = json.loads(response.text)
#     status = json_res["environments"][0]["status"]
#     output_res = {"stag name":json_res["environments"][0]["name"],"status": status,"release_id": json_res["environments"][0]["releaseId"]}
#   if status in ["successed", "rejected"]:
#     index_of_release_id = release_ids.index(release_id)
#     del release_ids[index_of_release_id]
#   time.sleep(20)



# while len(release_ids) > 0:
#   for release_id in release_ids:
#     print(release_id)
#     index_of_release_id = release_ids.index(release_id)
#     del release_ids[index_of_release_id]